# Tracking: the status file

`deal-submissions/status.md` in the user's project. One file per project, one row
per list and product. It is the memory between runs and the answer to "where are we".
It is not the only guard against a duplicate: a later run on another machine has no
status file, which is why the pull request procedure also searches the list's open
and closed pull requests before anything is prepared.

## Format

```markdown
# Deal submissions: <sale name>

Updated: <YYYY-MM-DD HH:MM, time zone>

| List | Product | Sent | Date | Link | State | Note |
|---|---|---|---|---|---|---|
| <list name> | <product> | pull request, 1 row in README | 2026-11-18 | <pull request URL> | merged | row visible on the default branch |
| <list name> | <product> | form, 13 fields | 2026-11-18 | <page URL> | sent | "free listings go live in 5 to 7 days" |
| <list name> | <product> | email to <address> | 2026-11-19 | | no answer | list posted 20 Nov; check it |
| <list name> | <product> | nothing | | | prepared | waits on your approval of the diff |
| <list name> | <product> | nothing | | | prepared | from 2026-11-24: the list's bot checks the live price |
| <list name> | <product> | nothing | | | prepared | declined at approval 2 (the diff) |
| <list name> | <product> | nothing | | | prepared | the list's check fails: "description is 150 characters, must be under 120"; entry unchanged on your call |
| <list name> | <product> | pull request, 1 file | 2026-11-19 | <pull request URL> | sent | list check not run (your call); entry checked against the written rules by reading |
```

## States

- `prepared`: the entry exists, nothing has been pushed, submitted or sent. The note
  says why it stopped there: an approval still open, a start date, a "no" at an
  approval, a failing list check, or "list check not run" when the user chose not
  to run the list's script.
- `sent`: the pull request is open, the form was submitted, or the email was sent.
- `merged`: the pull request was merged. Not yet `live` until the row shows on the
  default branch or the rendered site.
- `live`: the entry is visible to visitors.
- `rejected`: closed without a merge, or the site said no. The note quotes the
  reason. A rejected entry is not resubmitted unless the list's live rules, read
  again, no longer contain the rule that caused the rejection.
- `no answer`: sent, and nothing has come back after the time the list named (or a
  week, if it named none).

A row moves forward only on evidence: a merge seen through `gh`, the row read on
the branch, the product name read on the page. "Probably live by now" is not a state.

## What goes in the note

Facts only: the review time the site stated, a maintainer comment (quoted, with the
link), a request that came with the merge (star, share, badge) marked as a request,
the date the list is posted, a deadline, a start date the entry waits for. No
opinions about maintainers.

## On a later run

1. Read the status file first.
2. For every `sent` pull request: `gh pr view <url> --json state,mergedAt,closedAt,comments`.
   Leave out comments whose author is the signed-in user (`gh api user --jq .login`);
   the user's own comments are not maintainer comments.
3. For every `sent` or `merged` entry: fetch the list's page or default branch and
   search for the product name; set `live` when found.
4. For every `sent` form or email past its stated review time: fetch the page; if
   the product is not there, set `no answer` and tell the user.
5. For every `prepared` row with a start date that has arrived: go back to Step 6
   for that list.
6. Show the user what changed and every new comment, verbatim, then continue with
   whatever the run was started for.

## Privacy

The status file lives in the user's project and may hold the user's own contact
details and links. Nothing from it is copied into a pull request, a record in the
listings folder, or a contribution to this skill's repository.
