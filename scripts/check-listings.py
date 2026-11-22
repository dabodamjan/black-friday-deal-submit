#!/usr/bin/env python3
"""Check every record in listings/ and rebuild listings/INDEX.md.

Usage:
    python3 scripts/check-listings.py              # check, then write INDEX.md
    python3 scripts/check-listings.py --check      # check only, exit 1 on errors
    python3 scripts/check-listings.py --self-test  # run the checker over
                                                   # scripts/test-records/ and
                                                   # show that each bad record
                                                   # is caught

Standard library only. Each record is one JSON file; the schema is
described in listings/README.md. A record that is not a JSON object, or
has the wrong type in a field, produces an error line and never a crash.
"""
import datetime as dt
import json
import pathlib
import re
import sys
import urllib.parse

ROOT = pathlib.Path(__file__).resolve().parent.parent
LISTINGS = ROOT / "listings"
INDEX = LISTINGS / "INDEX.md"
TEST_RECORDS = ROOT / "scripts" / "test-records"

REQUIRED = [
    "name", "url", "type", "accepts", "cost", "how_to_submit",
    "status", "edition", "verification", "recommended", "checked_on",
]
OPTIONAL = [
    "cost_note", "entry_format", "rules", "status_note", "recommended_for",
    "sources",
]
STRING_FIELDS = [
    "name", "url", "type", "accepts", "cost", "cost_note", "how_to_submit",
    "entry_format", "status", "status_note", "edition", "verification",
    "recommended_for", "checked_on",
]
LIST_FIELDS = ["rules", "sources"]
TYPES = {"github-pr", "form", "email", "forum", "account", "none"}
COSTS = {"free", "free-with-paid-options", "paid-only", "unknown"}
STATUSES = {
    "live", "live-no-current-edition", "dead", "copy", "paid-only", "not-a-fit",
    "no-submission-route", "could-not-read",
}
VERIFICATIONS = {"verified", "partly", "unread"}
RECOMMENDABLE_COSTS = {"free", "free-with-paid-options"}
SLUG = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
DATE = re.compile(r"^\d{4}-\d{2}-\d{2}$")


def load(folder):
    """Return (records, errors). A record is (path, data) for every file
    that parsed as JSON, whatever its shape; check() judges the shape."""
    records = []
    errors = []
    for path in sorted(folder.glob("*.json")):
        if path.name.startswith("_"):
            continue
        if not SLUG.match(path.stem):
            errors.append(f"{path.name}: file name must be a lowercase slug")
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
        except (json.JSONDecodeError, UnicodeDecodeError) as exc:
            errors.append(f"{path.name}: invalid JSON ({exc})")
            continue
        records.append((path, data))
    return records, errors


def good_url(value):
    """https, a host, no whitespace."""
    if not isinstance(value, str) or not value.startswith("https://"):
        return False
    if any(ch.isspace() for ch in value):
        return False
    try:
        parts = urllib.parse.urlsplit(value)
    except ValueError:
        return False
    return bool(parts.hostname)


def good_date(value):
    """A real calendar date written YYYY-MM-DD, not in the future."""
    if not isinstance(value, str) or not DATE.match(value):
        return None
    try:
        return dt.date.fromisoformat(value)
    except ValueError:
        return None


def check(path, d):
    name = path.name
    out = []
    if not isinstance(d, dict):
        kind = "null" if d is None else type(d).__name__
        out.append(f"{name}: record must be a JSON object, got {kind}")
        return out
    for key in REQUIRED:
        if key not in d or d[key] in ("", None, []):
            out.append(f"{name}: missing required field '{key}'")
    for key in d:
        if key not in REQUIRED and key not in OPTIONAL:
            out.append(f"{name}: unknown field '{key}'")
    for key in STRING_FIELDS:
        if key in d and not isinstance(d[key], str):
            out.append(f"{name}: '{key}' must be a string, got {type(d[key]).__name__}")
    for key in LIST_FIELDS:
        if key in d:
            val = d[key]
            if not isinstance(val, list) or not all(isinstance(x, str) for x in val):
                out.append(f"{name}: '{key}' must be a list of strings")
    if "recommended" in d and not isinstance(d["recommended"], bool):
        out.append(f"{name}: 'recommended' must be true or false")

    # Everything below reads fields only when they have the right type, so
    # a wrong type produces the one error above and nothing else breaks.
    def s(key):
        v = d.get(key)
        return v if isinstance(v, str) else None

    if s("type") not in TYPES:
        out.append(f"{name}: type must be one of {sorted(TYPES)}")
    if s("cost") not in COSTS:
        out.append(f"{name}: cost must be one of {sorted(COSTS)}")
    if s("status") not in STATUSES:
        out.append(f"{name}: status must be one of {sorted(STATUSES)}")
    if s("verification") not in VERIFICATIONS:
        out.append(f"{name}: verification must be one of {sorted(VERIFICATIONS)}")
    if not good_url(d.get("url")):
        out.append(f"{name}: url must be https:// with a host and no spaces")
    sources = d.get("sources")
    if isinstance(sources, list):
        for src in sources:
            if isinstance(src, str) and not good_url(src):
                out.append(f"{name}: source '{src}' must be https:// with a host and no spaces")
    day = good_date(d.get("checked_on"))
    if day is None:
        out.append(f"{name}: checked_on must be a real calendar date written like 2026-11-18")
    elif day > dt.date.today():
        out.append(f"{name}: checked_on is in the future")
    if s("cost") == "paid-only" and s("status") not in ("paid-only", "dead"):
        out.append(f"{name}: a paid-only cost needs status 'paid-only'")

    rec = d.get("recommended")
    if rec is True:
        if s("status") != "live":
            out.append(f"{name}: a recommended record needs status 'live'")
        if s("cost") not in RECOMMENDABLE_COSTS:
            out.append(f"{name}: a recommended record needs a free route (cost free or free-with-paid-options)")
        if s("verification") != "verified":
            out.append(f"{name}: a recommended record needs verification 'verified'")
        rf = s("recommended_for")
        if rf is None or not rf.strip():
            out.append(f"{name}: a recommended record needs 'recommended_for' (a few words on what kind of product)")
        elif len(rf) > 120:
            out.append(f"{name}: 'recommended_for' is {len(rf)} characters, keep it under 120")
        note = s("status_note")
        if note is None or not note.strip():
            out.append(f"{name}: a recommended record needs evidence in 'status_note' (what got in, and when)")
    elif "recommended_for" in d:
        out.append(f"{name}: 'recommended_for' only belongs on a recommended record")
    return out


def duplicates(records):
    """Duplicate names and urls, comparing only string values so a record
    with a list where a string belongs cannot crash the comparison."""
    out = []
    seen = {"name": {}, "url": {}}
    for path, d in records:
        if not isinstance(d, dict):
            continue
        for key in ("name", "url"):
            val = d.get(key)
            if not isinstance(val, str):
                continue
            if val in seen[key]:
                out.append(f"{path.name}: duplicate {key}, also in {seen[key][val]}")
            else:
                seen[key][val] = path.name
    return out


def cell(text):
    """One table cell: pipes escaped, line breaks flattened, so a record
    cannot break the table or add rows to it."""
    text = str(text).replace("\r\n", " ").replace("\n", " ").replace("\r", " ")
    return text.replace("|", "\\|").strip()


def render_index(records):
    """The text of INDEX.md for these records."""
    recommended = [r for r in records if r[1]["recommended"]]
    live = [r for r in records if r[1]["status"] == "live" and not r[1]["recommended"]]
    other = [r for r in records if r[1]["status"] != "live"]

    def row(path, d, with_for=False):
        cells = [
            f"[{cell(d['name'])}]({cell(d['url'])})", cell(d["type"]), cell(d["cost"]),
            cell(d["status"]), cell(d["verification"]), cell(d["checked_on"]),
            f"`{path.name}`",
        ]
        if with_for:
            cells.insert(1, cell(d["recommended_for"]))
        return "| " + " | ".join(cells) + " |"

    by_name = lambda r: r[1]["name"].lower()
    lines = [
        "# Listings index",
        "",
        "Generated by `scripts/check-listings.py`. Do not edit by hand; edit the",
        "JSON records and run the script.",
        "",
        f"{len(records)} records. {len(recommended)} recommended. "
        f"{len(recommended) + len(live)} were live when last checked.",
        "",
        "## Recommended",
        "",
        "Free route, live in the last season, and an entry from someone other than",
        "the maintainer demonstrably got in. The second column says for what kind of",
        "product, in the list's own words. Re-read every one before preparing anything.",
        "",
        "| List | For | Type | Cost | Status | Verified | Checked on | Record |",
        "|---|---|---|---|---|---|---|---|",
    ]
    lines += [row(p, d, with_for=True) for p, d in sorted(recommended, key=by_name)]
    lines += [
        "",
        "## Live when last checked, not recommended",
        "",
        "Live, but no evidence yet that a free entry gets in, or the route needs an",
        "account, a sign-in or a forum post.",
        "",
        "| List | Type | Cost | Status | Verified | Checked on | Record |",
        "|---|---|---|---|---|---|---|",
    ]
    lines += [row(p, d) for p, d in sorted(live, key=by_name)]
    lines += [
        "",
        "## Paid only, not a fit, copies, dead, or unread",
        "",
        "| List | Type | Cost | Status | Verified | Checked on | Record |",
        "|---|---|---|---|---|---|---|",
    ]
    lines += [row(p, d) for p, d in sorted(other, key=by_name)]
    lines.append("")
    return "\n".join(lines)


def write_index(records):
    INDEX.write_text(render_index(records), encoding="utf-8")


def unescaped_pipes(line):
    """Column separators: pipes not preceded by a backslash."""
    return len(re.findall(r"(?<!\\)\|", line))


def run(folder):
    """Check one folder. Returns (records, errors)."""
    records, errors = load(folder)
    for path, d in records:
        errors += check(path, d)
    errors += duplicates(records)
    return records, errors


def self_test():
    """Every file in scripts/test-records/ is a bad record except the ones
    whose name starts with 'ok-'. Each bad one must produce at least one
    error line, and the error must name the file. Nothing may crash."""
    expected = json.loads((TEST_RECORDS / "_expected.json").read_text(encoding="utf-8"))
    records, errors = run(TEST_RECORDS)
    for e in errors:
        print("ERROR", e)
    print()
    failed = []
    for path in sorted(TEST_RECORDS.glob("*.json")):
        if path.name.startswith("_"):
            continue
        mine = [e for e in errors if e.startswith(path.name + ":")]
        want = expected.get(path.name)
        if want is None:
            failed.append(f"{path.name}: no entry in _expected.json")
        elif want == "":
            if mine:
                failed.append(f"{path.name}: expected no errors, got {len(mine)}")
        elif not any(want in e for e in mine):
            failed.append(f"{path.name}: expected an error containing '{want}', got {mine or 'nothing'}")
    for name in expected:
        if not (TEST_RECORDS / name).exists():
            failed.append(f"{name}: listed in _expected.json but missing")
    # The generated index must survive each good record's content (a pipe
    # and a line break in its name). Render the index for that record alone
    # and look at its row: one line, the separator count of a recommended
    # row (8 columns, 9 separators) or another row (7 columns, 8), and the
    # record's own pipe written as \|.
    good = [(p, d) for p, d in records if p.name.startswith("ok-")]
    for p, d in good:
        index_lines = render_index([(p, d)]).split("\n")
        rows = [l for l in index_lines if l.startswith("| [")]
        want = 9 if d["recommended"] else 8
        if len(rows) != 1:
            failed.append(f"{p.name}: expected one index row starting '| [', got {len(rows)}")
            continue
        row = rows[0]
        if p.name not in row:
            failed.append(f"{p.name}: the row was split, its file name is not on the line it starts on")
        if unescaped_pipes(row) != want:
            failed.append(f"{p.name}: row has {unescaped_pipes(row)} unescaped separators, expected {want}")
        if "|" in d["name"] and "\\|" not in row:
            failed.append(f"{p.name}: the pipe in the name is not escaped as \\| in the row")
    if failed:
        for f in failed:
            print("SELF-TEST FAILED", f)
        return 1
    bad = sum(1 for p in TEST_RECORDS.glob("*.json") if not p.name.startswith(("_", "ok-")))
    print(f"self-test ok: {bad} bad records each caught, {len(good)} good record(s) clean, no crash")
    return 0


def main(argv):
    if "--self-test" in argv:
        return self_test()
    check_only = "--check" in argv
    records, errors = run(LISTINGS)
    if errors:
        for e in errors:
            print("ERROR", e)
        print(f"{len(errors)} error(s) in {len(records)} record(s)")
        return 1
    oldest = min(d["checked_on"] for _, d in records) if records else "n/a"
    rec = sum(1 for _, d in records if d["recommended"])
    live = sum(1 for _, d in records if d["status"] == "live")
    print(f"ok: {len(records)} records, {rec} recommended, {live} live, no errors, oldest checked_on {oldest}")
    if not check_only:
        write_index(records)
        print(f"wrote {INDEX.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
