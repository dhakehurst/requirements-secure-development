#!/usr/bin/env python3
"""Consistency check for the requirement sets. Run from the repository root:

    python3 tools/check.py

It checks, for each set (libraries/, applications/):
  1. every requirement is defined once in the set;
  2. each document's checklist lists exactly the requirements defined in that document, with the
     same level and title;
  3. the one-person profile (applications, document 05) lists only requirements that exist in the
     document it names, with the same title;
  4. every requirement id mentioned anywhere in the set is defined in the set or retired (a line
     that says an id is "used only in the set for" the other set is skipped);
  5. every document of the set states the same version as the set's README;
  6. no line is longer than 100 characters, except table rows and lines in code blocks.

It exits with status 1 and lists the problems if any check fails.
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SETS = ["libraries", "applications"]
MAX_LINE = 100

ID = r"[A-Z]{2,4}-\d{2}"
DEFINITION = re.compile(rf"^- \*\*({ID}) \((MUST NOT|MUST|SHOULD NOT|SHOULD|MAY)\) (.+?)\.\*\*")
RETIRED = re.compile(rf"^- \*\*({ID}) \(retired in [0-9.]+\)\.\*\*")
GUIDANCE = re.compile(rf"^- \*\*({ID}) (.+?)\.\*\*")  # annex practices without a level
ROW = re.compile(rf"^\| ({ID}) \| ([A-Z ]+) \| (.+?) \|")
PROFILE_ROW = re.compile(rf"^\| ({ID}) \| ([A-Z ]+) \| (.+?) \| (\w+) \|")
MENTION = re.compile(rf"\b({ID})\b")
README_VERSION = re.compile(r"^Version ([0-9.]+ \(draft\)|[0-9.]+), ")
DOC_VERSION = re.compile(r"version ([0-9.]+ \(draft\)|[0-9.]+), ")

# Ids of other schemes that look like requirement ids (for example OSPS control ids).
FOREIGN = re.compile(rf"OSPS-{ID}|CWE-\d+|[A-Z]{{2,4}}-\d{{2}}\.\d{{2}}")

problems = []


def problem(path, line_no, text):
    problems.append(f"{path.relative_to(ROOT)}:{line_no}: {text}")


def sections(lines):
    """Yield (line number, line, current level-2 heading)."""
    heading = ""
    for no, line in enumerate(lines, 1):
        if line.startswith("## "):
            heading = line[3:].strip()
        yield no, line, heading


def check_lines(path, lines):
    in_code = False
    for no, line in enumerate(lines, 1):
        if line.lstrip().startswith("```"):
            in_code = not in_code
            continue
        if in_code or line.startswith("|"):
            continue
        if len(line) > MAX_LINE:
            problem(path, no, f"line has {len(line)} characters (more than {MAX_LINE})")


def check_set(name):
    folder = ROOT / name
    docs = sorted(folder.glob("*.md"))
    defined = {}  # id -> (doc, level, title)
    retired = set()
    checklists = {}  # doc -> {id: (level, title, line)}
    profile = []  # (doc, line, id, title, document number)
    text = {}

    for doc in docs:
        lines = doc.read_text(encoding="utf-8").splitlines()
        text[doc] = lines
        check_lines(doc, lines)
        checklists[doc] = {}
        for no, line, heading in sections(lines):
            m = DEFINITION.match(line)
            if m:
                rid, level, title = m.groups()
                if rid in defined:
                    problem(doc, no, f"{rid} is defined again (first in {defined[rid][0].name})")
                defined[rid] = (doc, level, title)
                continue
            m = RETIRED.match(line)
            if m:
                retired.add(m.group(1))
                continue
            m = GUIDANCE.match(line)
            if m and heading != "Checklist":
                rid = m.group(1)
                if rid in defined:
                    problem(doc, no, f"{rid} is defined again (first in {defined[rid][0].name})")
                defined[rid] = (doc, None, m.group(2))
                continue
            if heading == "Checklist":
                m = ROW.match(line)
                if m:
                    rid, level, title = m.groups()
                    if rid in checklists[doc]:
                        problem(doc, no, f"{rid} is in the checklist twice")
                    checklists[doc][rid] = (level.strip(), title.strip(), no)
            elif heading == "One-Person Profile":
                m = PROFILE_ROW.match(line)
                if m:
                    rid, _level, title, number = m.groups()
                    profile.append((doc, no, rid, title.strip(), number))

    # 2. Checklists match the definitions of their document.
    for doc, rows in checklists.items():
        own = {rid: d for rid, d in defined.items() if d[0] == doc and d[1] is not None}
        if not rows and not own:
            continue
        if not rows:
            if any(d[1] is not None for d in own.values()):
                problem(doc, 1, "document defines requirements but has no checklist")
            continue
        for rid, (_doc, level, title) in own.items():
            if rid not in rows:
                problem(doc, 1, f"{rid} is defined but missing from the checklist")
                continue
            row_level, row_title, no = rows[rid]
            if row_level != level:
                problem(doc, no, f"{rid} checklist level {row_level}, definition {level}")
            if row_title != title:
                problem(doc, no, f"{rid} checklist title '{row_title}', definition '{title}'")
        for rid, (_level, _title, no) in rows.items():
            if rid not in own:
                problem(doc, no, f"{rid} is in the checklist but not defined in this document")

    # 3. Profile rows point to existing requirements.
    for doc, no, rid, title, number in profile:
        if rid not in defined:
            problem(doc, no, f"profile lists {rid}, which is not defined")
            continue
        target = defined[rid][0].name
        if not target.startswith(number):
            problem(doc, no, f"profile says {rid} is in document {number}, it is in {target}")
        if defined[rid][2] != title:
            problem(doc, no, f"profile title '{title}' for {rid}, definition '{defined[rid][2]}'")

    # 4. Every mentioned id exists.
    known = set(defined) | retired
    for doc, lines in text.items():
        in_code = False
        for no, line in enumerate(lines, 1):
            if line.lstrip().startswith("```"):
                in_code = not in_code
            if in_code:
                continue
            following = lines[no] if no < len(lines) else ""
            if "only in the set for" in f"{line} {following}":  # a pointer to the other set
                continue
            for rid in MENTION.findall(FOREIGN.sub("", line)):
                if rid not in known:
                    problem(doc, no, f"{rid} is mentioned but not defined in the {name} set")

    # 5. Versions agree.
    readme = folder / "README.md"
    version = None
    for line in text.get(readme, []):
        m = README_VERSION.match(line)
        if m:
            version = m.group(1)
            break
    if version is None:
        problem(readme, 1, "no 'Version x.y' line near the top")
    else:
        for doc, lines in text.items():
            if doc == readme:
                continue
            head = " ".join(lines[:4])
            m = DOC_VERSION.search(head)
            if not m:
                problem(doc, 3, "no 'version x.y' near the top")
            elif m.group(1) != version:
                problem(doc, 3, f"version {m.group(1)}, README says {version}")


for top in sorted(ROOT.glob("*.md")):
    check_lines(top, top.read_text(encoding="utf-8").splitlines())
for s in SETS:
    check_set(s)

if problems:
    print("\n".join(problems))
    print(f"\n{len(problems)} problem(s) found.")
    sys.exit(1)
print("All checks passed.")
