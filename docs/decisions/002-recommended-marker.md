# 002: a record can be recommended, by evidence, not by opinion

Date: 2026-11-20

## Decision

Every listings record carries `recommended: true` or `false`. A record is
recommended when, on its `checked_on` date, the route was free, the list was live
this season, and an entry from someone other than the maintainer demonstrably got
in (an outside pull request merged this season, or a page that says its entries
come from makers' form or email submissions and shows this season's entries). `recommended_for` says in a few words what kind of product the list
takes. The index opens with the recommended records, the skill reads them first, and
the README says how many there are.

## Why

- Sixty-odd records is too many to open in order. A reader with one afternoon wants
  the ones where a free entry gets in, for their kind of product, first.
- "Recommended" has to mean something checkable, or it decays into taste. Merged
  pull requests and listed entries can be seen by anyone; "good list" cannot.
- The test has three parts so that a live, free list nobody has tried is not
  recommended yet, and a paid or dead list never is. A list behind a sign-in can
  be recommended when a listing went live there; the skill hands over the text.
- The marker is a reading order, not a promise. The skill still re-reads every
  record on the day.

## Consequences

- The check script refuses `recommended: true` on a record that is not `live`,
  not `verified`, or has no free route, and requires `recommended_for`.
- Evidence for the marker goes in `status_note` with its date, and is something a
  reader can see on a public page; one submitter's own result does not count
  (amended 2026-11-22).
- A contributor who sees an entry get in flips the marker in the same pull request
  that updates `checked_on`.
