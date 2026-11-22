# 001: lists are records in a folder, not lines in the skill

Date: 2026-11-20

## Decision

The skill text describes the process and names no list. Every list lives as one JSON
record in `listings/`, with a `checked_on` date, and the skill reads the folder at the
start of a run. New lists found during a run are written as records in the same format
into the user's project, and can be contributed back with a pull request.

## Why

- Lists change every year. A list name baked into the skill text would be wrong
  within a season, and nobody re-reads a skill to find out which line went stale. A
  record with a date says exactly how old the knowledge is.
- People add lists. A JSON file per list is something anyone can add in a pull
  request without touching the skill, and two contributors adding two lists do not
  conflict.
- The skill must search for new lists anyway. Keeping the known ones as data makes
  "known, re-check" and "new, read" the same kind of work.
- JSON over YAML or TOML because the check script runs on the Python standard library
  on any machine, and because several of the deal lists themselves take one JSON file
  per deal, so contributors here already know the shape.

## Consequences

- `listings/INDEX.md` is generated, never edited by hand.
- A skill copied without its repository fetches the records from GitHub at run time.
- The records carry public rules only. The content rules in `listings/README.md` are
  part of the schema, not advice.
