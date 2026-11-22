# Listings

One JSON file per deal list. The skill reads this folder at the start of a run,
recommended records first, and re-checks every live record on the day; people add and
correct records with pull requests. `INDEX.md` is generated from the records by
`scripts/check-listings.py` and opens with the recommended ones.

The current records are a **November 2026 snapshot**. Every one carries a
`checked_on` date. Lists change every year: a record tells you where to look and what
the rules were on that date, not what they are today.

## Recommended records

A record is `recommended` when all three hold on its `checked_on` date:

1. the route is free (`cost` is `free` or `free-with-paid-options`);
2. the list is `live` this season;
3. an entry from someone other than the maintainer demonstrably got in, in a way a
   reader can see on a public page: a pull request from an outside author was merged
   this season, or the list's own page says its entries come from makers' form or
   email submissions and shows this season's entries.

The evidence goes in `status_note` with its date. `recommended_for` says what kind of
product the list takes, in a few words from the list's own rules, so a reader can
skip the ones that do not fit before opening anything. A recommended record is still
re-read on the day; the marker orders the reading, it does not replace it.

A list that is live and free but whose pages do not show an outside entry getting in
is not recommended until they do. Lists behind a sign-in can be recommended when
their public page shows that; the skill hands over the text for them.

## Add or update a record

1. Copy `_template.json` to `<slug>.json` (lowercase, hyphens).
2. Fill it from the list's own page, read today. Not from a tweet about the list,
   not from memory.
3. Run `python3 scripts/check-listings.py` from the repository root. It checks the
   fields and rewrites `INDEX.md`.
4. Open a pull request with the record and the regenerated index.

What a record carries, and what it never carries:

- **Public rules only.** What the list's own README, contributing file, issue,
  form or FAQ says. A rule a maintainer or a merge bot stated in a public pull
  request comment counts, labelled as a comment ("the bot asked a three-app pull
  request to drop one row"). Private emails, direct messages and anything a
  maintainer said in private do not.
- **Written rule and enforced rule, both as what they are.** When a bot or a
  maintainer enforces something the written rules do not say, the record quotes
  the written rule and describes the enforcement next to it, and says which is
  which.
- **No opinions about people.** "Closes products under six months old" is a rule.
  Anything about the person is not.
- **No submitter data.** No product names of whoever added the record, no contact
  details, no account names, no links to their own submissions, and no notes on how
  their own entries fared. "38 pull requests from outside authors merged since
  1 Oct 2026" is evidence; one submitter's own result is not.
- **The verification you did, not the one you wish you had.** `verified` means you
  read the submission rules on the list's own page. `partly` means some of it
  (a page behind JavaScript, a form behind a sign-in). `unread` means the page did
  not load.

## Fields

| Field | Required | Values |
|---|---|---|
| `name` | yes | The list's name, with the owner for GitHub lists |
| `url` | yes | The list's main page, https |
| `type` | yes | `github-pr`, `form`, `email`, `forum`, `account` (a form behind a sign-in), `none` (no submission route) |
| `accepts` | yes | Who it is for: platforms, product types, minimum discount, product age |
| `cost` | yes | `free`, `free-with-paid-options`, `paid-only`, `unknown` |
| `cost_note` | no | What the paid options are, in words; no prices that will go stale unless they matter |
| `how_to_submit` | yes | The route in one or two sentences, with the submit URL |
| `entry_format` | no | The row, file or field list, close to verbatim |
| `rules` | no | List of strings: what gets an entry closed, limits, position rules, bot checks |
| `status` | yes | `live`, `live-no-current-edition`, `dead`, `copy`, `paid-only`, `not-a-fit`, `no-submission-route`, `could-not-read` |
| `status_note` | no | One line of evidence for the status, and for `recommended` |
| `edition` | yes | The season the record describes, for example `Black Friday 2026` |
| `verification` | yes | `verified`, `partly`, `unread` |
| `recommended` | yes | `true` or `false`, by the three-part test above; `true` needs `status: live`, a free route and `verification: verified` |
| `recommended_for` | when recommended | What kind of product, in a few words from the list's own rules, under 120 characters |
| `checked_on` | yes | `YYYY-MM-DD`, the day the pages in `sources` were read |
| `sources` | no | The URLs that were read |

`not-a-fit` means the list exists and takes submissions, but not the kind of product
this skill is usually run for (indie apps and small software); it is kept so nobody
has to visit it again to learn that. `paid-only` lists are kept for the same reason.
`copy` means a fork or near copy of another list; the record names the original.
One rule for forks: a fork with its own merged outside pull requests this season and
its own submission rules is a list and gets a record of its own; a fork with neither
is a `copy`.

## Where the 2026 seed came from

The records were written in November 2026. Every list was read on the date in its
`checked_on`, and the dead, paid and off-topic ones were kept with that date. The
recommended marker follows what the lists' own pages showed on those dates. Several of the newer sites were found through public "N places to list your
deal" posts on X between late October and mid November 2026:
[Ram Patra](https://x.com/rampatra_/status/2115391340812849642),
[Tushar Gugnani](https://x.com/tushargugnani/status/2117852828610056664),
[Tom Han](https://x.com/tomhan245/status/2120109966761832484),
[Manish](https://x.com/ideasbymanish/status/2123000009108910475) and
[Atta](https://x.com/attacomsian/status/2121189787822592116). Those posts are starting
points; the records describe what the sites themselves said.
