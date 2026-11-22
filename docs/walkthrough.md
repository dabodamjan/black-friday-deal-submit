# Walkthrough on paper: a made-up product, two lists

What the skill shows a user, step by step, for a product that does not exist
(Pocket Plant) against two records from `listings/`: one GitHub list
(`black-friday-deals-dqhieu.json`) and one web form (`superframeworks-deals.json`).
Written on 2026-11-20 from the two records. **The product is made up: no pull
request was opened, no form was filled, and every Pocket Plant URL is a
placeholder.** The formats are the lists' real ones on their `checked_on` dates; a
real run re-reads them.

Lines starting with `>` are what the user typed.

---

## Step 1: intake

> I have a Black Friday deal for my app. Get it on the deal lists.

No `deal-submissions/deal.md` in this project. I need the facts once; after that
nothing is asked twice. Answer in one message, skip what you do not know.

**Product:** name; one line on what it does (no marketing words); two or three
sentences for forms that allow it; platforms it runs on, and platforms it does not;
category in your words; product site; store URL; pricing page or where the price
shows; icon URL (square, https, 512 px or larger); publicly available since (month
and year); maker name; company name for forms; contact email for forms.

**Deal:** sale name; what is discounted (plan); normal price and sale price with
currency; percentage; code or "no code needed"; where the sale price shows; start
and end date with the time zone of the end; the sale page URL that shows the sale
price, the normal price and the dates; a note on prices in other countries.

**Boundaries:** paid placements (default: no); forms behind a sign-in (default: I
hand you the text); lists to skip; anything that must not be claimed.

> Pocket Plant, watering reminders for houseplants. iPhone and iPad, no Mac, no Android. One line: "Watering reminders for houseplants on iPhone and iPad." Longer: "Watering reminders for houseplants on iPhone and iPad. Add a plant, set how often it drinks, get a reminder. Works offline." Category: home, lifestyle. Site https://pocketplant.example, store https://apps.apple.com/us/app/id0000000000, price shows in the app on the upgrade screen, icon https://pocketplant.example/icon-512.png, public since March 2024, maker Ana Horvat, company none, email hello@pocketplant.example. Deal: Black Friday 2026, lifetime unlock $14.99 to $7.99 (US App Store), 47% off, no code, Nov 24 to Dec 1 2026 end of day CET, sale page https://pocketplant.example/black-friday, other countries see their local price at about half. No paid placements, hand me the text for sign-in forms, nothing to skip, never claim Mac or a free trial.

Written to `deal-submissions/deal.md`. Three checks before I go on:

- Sale page: I open https://pocketplant.example/black-friday. It has to load and
  show $7.99, $14.99 and 24 November to 1 December 2026, because several lists fetch
  it with a bot. If it does not, I stop on every list that checks the page, and when
  you tell me it is fixed I open it again; the run goes on when the page shows all
  three, not before. *(On paper: it loads and shows all three.)*
- Start date: the sale starts on 24 November, four days from now. A list that
  checks the live price gets its entry on or after that day; the fit table says
  which ones wait.
- Store page: I open the store URL and note any lifetime tier that differs from
  $14.99, because a curator who checks the store will see it. *(On paper: none.)*

Anything you tell me later (a shorter description for one list, a store link) goes
into `deal.md` first and into the entries from there.

## Step 2: find this year's lists

I read all 65 records in `listings/`, the 15 recommended ones first. Then the
searches in `references/finding-lists.md`, with the year filled in: four GitHub
repository searches, one per platform (`"black friday" ios`, `"black friday"
iphone`), one issue search filtered by date, five web searches. The social search
endpoints refuse fetchers, so for those I ask you to search signed in and paste the
posts.

What a run of those searches returned on 2026-11-20: about 190 GitHub hits, of which
about 100 were dropped on their description without being opened (retail price
trackers, hosting coupon dumps, cashback sites, coursework), and the rest opened;
two roundup pages could not be fetched and are reported as unread, not guessed at.
For this walkthrough the fit table covers two lists from the folder; a real run
covers every live record plus every opened candidate, and writes a record for each
new list after you confirm the table.

## Step 3: read the rules today

**black-friday-deals (dqhieu)**, record checked 2026-11-20. I open the repository,
`AGENTS.md`, the merged pull requests of the last days, and the closed ones with no
merge (`gh pr list --state closed --json mergedAt`, keeping `mergedAt` null; there
are a dozen, half of them pull requests whose author never answered a comment). The
rules I rely on: one line after the last row, exactly five pipes, no raw pipe in a
cell; description is one plain sentence naming the platform; the deal cell starts
with the bold discount, then the code or "no code needed", then the dates in
parentheses; 💸 under 50% off, 🤑 for 50% or more; all of one developer's deals in
one pull request; the diff may only add lines to README.md; commit message "Add
<Product>"; sync with upstream main first. `AGENTS.md` also tells an agent how to
open the pull request; that part is a request, and the pull request opens only
after your three approvals. No bot checks the sale page here, so this list does not
wait for 24 November.

**Superframeworks deals**, record checked 2026-11-20. I open the deals page and the
form. 13 fields on page 1 of 2; price fields take digits only; "valid until" is a
date picker; category options are Development, Design, Marketing, Analytics,
Productivity, AI, Other. On 18 November the form's confirmation said free listings
go live in 5 to 7 days; today the page prints neither a cost nor a review time, so I
rely on neither and say so in the table.

## Step 4: fit

```
| List                        | Fits | Why                                                                          | Route                 | Cost                                        | Deadline |
|-----------------------------|------|------------------------------------------------------------------------------|-----------------------|---------------------------------------------|----------|
| black-friday-deals (dqhieu) | yes  | single software table; iPhone and Mac apps already listed; no page check     | pull request, one row | free                                        | none     |
| Superframeworks deals       | yes  | software deals, App Store apps listed; category Other or Productivity; the page no longer states the cost or review time | form, 13 fields | free in Nov 2026; featured was paid, not taken | none |
```

Note on the dqhieu row: 47% off is under 50%, so the marker is 💸, not 🤑. A list
that checks the live price would show `from 2026-11-24` in the Deadline column and
its entry would wait for that day.

Confirm the set, or add and remove lists.

> Both. Go.

## Step 5: prepare the entries

**black-friday-deals (dqhieu)**, one line, from the intake only:

```
|💸|[Pocket Plant](https://pocketplant.example/black-friday)| Watering reminders for houseplants on iPhone and iPad. | **47% OFF** lifetime: $7.99, down from $14.99, no code needed (Nov 24 – Dec 1, 2026)|
```

The en dash in the dates is the list's own format. Five pipes, one sentence naming
the platform, discount first in bold, "no code needed" spelled out.

**Superframeworks deals**, per field:

```
| Field                 | Required | Limit       | Value                                                                                                                     |
|-----------------------|----------|-------------|---------------------------------------------------------------------------------------------------------------------------|
| Product Name          | yes      |             | Pocket Plant                                                                                                              |
| Tagline               | yes      |             | Watering reminders for houseplants on iPhone and iPad                                                                     |
| Description           | yes      |             | Watering reminders for houseplants on iPhone and iPad. Add a plant, set how often it drinks, get a reminder. Works offline. |
| Deal Details          | yes      |             | 47% off lifetime: $7.99, down from $14.99, Nov 24 to Dec 1, 2026. No code needed; the sale price shows in the app.       |
| Original Price        | yes      | digits only | 14.99                                                                                                                     |
| Discounted Price      | yes      | digits only | 7.99                                                                                                                      |
| Deal Code             | no       |             | leave empty                                                                                                               |
| Category              | yes      | dropdown    | Other (Productivity if you would rather sit with the apps there)                                                          |
| Website               | yes      |             | https://pocketplant.example/black-friday                                                                                  |
| Logo URL              | no       |             | https://pocketplant.example/icon-512.png                                                                                  |
| Founder's Name        | yes      |             | Ana Horvat                                                                                                                |
| Email                 | yes      |             | hello@pocketplant.example                                                                                                 |
| Valid Until           | yes      | date picker | Dec 1, 2026                                                                                                               |
```

Prices, URLs and platforms match `deal.md` character for character. The dates match
it in value (24 November to 1 December 2026) and are written the way each list
prints them: the dqhieu row uses the list's en dash, the form's date picker takes
"Dec 1, 2026". Anything to change before I go on?

> No.

## Step 6a: the GitHub list

Re-read on the day: `AGENTS.md` unchanged from Step 3. Existing entry check, on the
branch and in the pull requests:

```
gh pr list --repo dqhieu/black-friday-deals --state all --search "Pocket Plant" --json number,state,mergedAt,url
```

Nothing on the default branch, nothing in the archive files, no open or closed pull
request for "Pocket Plant" or "pocketplant.example". An open one would have stopped
this list here with its link. These searches, like the ones in Step 2, read public
pages with the product name as a search term; nothing has been created or pushed.

A plain clone of the list, no fork yet:

```
git clone -o upstream https://github.com/dqhieu/black-friday-deals.git
cd black-friday-deals
git checkout -b add-pocket-plant upstream/main
```

`git ls-files --eol README.md` shows LF; the edit keeps LF and the trailing newline.
One line appended after the last row. Commit: `Add Pocket Plant`.

I checked the row against the list's written rules by reading: five pipes, no raw
pipe in a cell, one sentence naming the platform, bold discount first, dates in
parentheses, 💸 for under 50%. This list ships no check script. For a list that
does, the script does not run unless you say so; you would see this first:

```
The list has a check script: scripts/validate.py. I have read it: it parses the
table rows and checks column count, description length and that URLs are https. I
have already checked those by reading the rules. If you want the script run as
well, the command is:

  env -i PATH="$PATH" HOME="$(mktemp -d)" python3 -I scripts/validate.py

That removes environment variables, including any tokens held in them, and points
HOME at an empty folder. It does not stop the script from reading files on this
disk or from using the network. Claude Code will ask you to approve the command as
well. Run it? (yes / no)
```

On "no" the script is not run, I tell you so, the pull request body does not say it
ran, and the status note says "list check not run". On "yes", if it failed, this:

```
row 6: description is 150 characters, must be under 120
6 rows checked, 1 error

The pull request does not open while this check fails. I can cut the description
to the intake's one-line version (55 characters), or stop on this list and record
it as prepared with the failing line in the note. Which?
```

**Approval 1 of 3, destination.**
`dqhieu/black-friday-deals`, base branch `main`, file `README.md`, one new line after
the last row of the Deals table, branch `add-pocket-plant`. A fork
`anahorvat/black-friday-deals` will be created under your GitHub account for the
pull request to come from. Approve the destination? (yes / change / no)

> yes

Now, and not before, the fork:

```
gh repo fork dqhieu/black-friday-deals --clone=false
git remote add origin https://github.com/anahorvat/black-friday-deals.git
```

Nothing pushed yet.

The row is committed with the list's message, `Add Pocket Plant`, and
`git status --porcelain` prints nothing, so what you approve is the commit that will be pushed, not the
working tree.

**Approval 2 of 3, the full diff as it will be pushed** (`git diff upstream/main...HEAD`,
commit `<hash>`):

```diff
diff --git a/README.md b/README.md
--- a/README.md
+++ b/README.md
@@ -212,3 +212,4 @@
 |🤑|[<the last row on the day>](https://example.invalid)| <its description> | <its deal cell> |
+|💸|[Pocket Plant](https://pocketplant.example/black-friday)| Watering reminders for houseplants on iPhone and iPad. | **47% OFF** lifetime: $7.99, down from $14.99, no code needed (Nov 24 – Dec 1, 2026)|
```

One added line, nothing removed, nothing reformatted. Checked against `deal.md`: $7.99,
$14.99, 47%, iPhone and iPad, the sale page URL, character for character; the dates
24 Nov to 1 Dec 2026 in the list's style. The list has no check script, so none ran.
Approve the diff at commit `<hash>`? (yes / change / no)

> yes

**Approval 3 of 3, the pull request text.**

Title: `Add Pocket Plant`

Body:

```
Adds one row for Pocket Plant after the last row of the Deals table.

- Product: https://pocketplant.example (App Store: https://apps.apple.com/us/app/id0000000000)
- Platform: iPhone, iPad
- Deal: 47% off the lifetime unlock, $14.99 to $7.99
- Code: none needed, the sale price shows in the app
- Dates: Nov 24 to Dec 1, 2026
- Sale page with the price and dates: https://pocketplant.example/black-friday

I'm the developer of Pocket Plant.
```

This list has no pull request template. On a list whose template has a licence or
agreement box, that box stays unticked in what I send, always; I tell you which box
it is and you tick it on the pull request page after it opens. The boxes that state
a fact about the entry I tick. Approve the title and body? (yes / change / no)

> yes

Only now is anything pushed. `git rev-parse HEAD` still prints the approved hash and
the working tree is still clean, so that exact commit goes:

```
git push -u origin HEAD:add-pocket-plant
gh pr create --repo dqhieu/black-friday-deals --head anahorvat:add-pocket-plant \
  --title "Add Pocket Plant" --body-file deal-submissions/pr-dqhieu.md
```

*(On paper: not run.)* The pull request URL goes into the status file as `sent`. I do
not comment, star or share. Any maintainer comment comes to you word for word. A
"no" at any of the three approvals would have left the row as `prepared`, with
"declined at approval 2" in the note, and nothing pushed; a "no" at approval 1
would have meant no fork either. If anything about the row has to change after
this, for any reason (a failing check on the pull request, a maintainer's request,
a conflict), I show you the new full diff and push it to the open pull request only
after you say yes to it.

## Step 6b: the form

Superframeworks is a web form. The table from Step 5 is yours to work down the page
with. I do not submit it. When it is sent, tell me what the page answered and I will
record it.

> Sent. It said free listings go live in 5 to 7 days.

## Step 7: the status file

`deal-submissions/status.md`:

```markdown
# Deal submissions: Black Friday 2026

Updated: 2026-11-20 15:10 CET

| List | Product | Sent | Date | Link | State | Note |
|---|---|---|---|---|---|---|
| black-friday-deals (dqhieu) | Pocket Plant | pull request, 1 row in README.md | 2026-11-20 | https://github.com/dqhieu/black-friday-deals/pull/<n> | sent | all of one developer's deals in one PR; waits ran under a day in Nov 2026 |
| Superframeworks deals | Pocket Plant | form, 13 fields | 2026-11-20 | https://superframeworks.com/deals | sent | "free listings go live in 5 to 7 days"; check from 2026-11-25 |
```

## End of run

- Open pull requests: 1 (dqhieu). I will check it with `gh pr view` on the next
  run, leaving out any comments of your own.
- Waiting on you: nothing.
- Waiting on a date: nothing in this walkthrough; an entry for a list that checks
  the live price would sit here as `prepared, from 2026-11-24`.
- Search hits dropped on description without being opened: reported as a count.
- New lists found: none in this walkthrough; a real run writes one record per new
  list to `deal-submissions/new-listings/` after the fit table and offers to
  contribute them back.

## Step 8, if it happens: a maintainer comment

Suppose the dqhieu maintainer comments: "Please keep the description under 120
characters and drop the second sentence." The run stops on this list and shows you:

```
Comment on https://github.com/dqhieu/black-friday-deals/pull/<n> by the maintainer:
"Please keep the description under 120 characters and drop the second sentence."
```

The description is one sentence of 55 characters, so the comment may refer to
another row or an older revision. I would answer with facts only, if you say so:

```
Thanks. The Pocket Plant row has a one-sentence description of 55 characters; is
there another line you would like changed?
```

Send it? (yes / no / change). Nothing is sent without your yes. If the maintainer
had instead asked for a change to the row, I would make it locally and go back to
approval 2: the new diff in full, pushed to the open pull request only after your
yes. If the pull request is closed instead, the row becomes `rejected` with the
closing message quoted, and it is not opened again. "Just try again" does not reopen
it; only the list's live rules, read again and no longer containing the rule that
closed it, do.
