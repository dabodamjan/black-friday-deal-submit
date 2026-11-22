# Contributing

The most useful contribution is a listings record: a deal list that is missing, one
that moved, one that changed its rules, or one that died. Lists change every year and
the records only stay useful if people who just submitted somewhere write down what
they read.

## Add or fix a listings record

1. Copy `listings/_template.json` to `listings/<slug>.json` (lowercase, hyphens), or
   open the existing record.
2. Fill it from the list's own page, read today. Set `checked_on` to today and list
   the pages you read under `sources`.
3. Set `recommended` by the test in [`listings/README.md`](listings/README.md): a
   free route, live this season, and an entry from someone other than the
   maintainer that demonstrably got in. Put the evidence and its date in
   `status_note`, and what the list takes in `recommended_for`. When in doubt,
   `false`; a later contributor who sees an entry get in can flip it.
4. Run `python3 scripts/check-listings.py` from the repository root. It checks the
   fields and regenerates `listings/INDEX.md`; commit both.
5. Open a pull request. Say in one line what you read and when.

The schema and the content rules are in [`listings/README.md`](listings/README.md).
The short version: public rules only, written rule and enforced rule each labelled as
what it is, no private correspondence, no opinions about maintainers, no data about
your own submissions, and a `verification` value that matches what you managed to
read.

## Change the check script

`python3 scripts/check-listings.py --self-test` runs the checker over the bad records
in `scripts/test-records/` and must end with `self-test ok`. A new rule in the script
gets a bad record there and a line in `_expected.json`.

## Change the skill

Keep the pull request to one change. The skill text names no list on purpose; lists
live in `listings/`. The user approval steps (destination, diff, pull request text;
text handed over for forms and emails) are the point of the skill, not a convenience
to trim.

## House style

Plain sentences, no em dashes, no emojis in prose, only facts that can be checked on
the page they came from.
