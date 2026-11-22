# Intake: the facts every entry is built from

Write the answers to `deal-submissions/deal.md` in the user's project. Ask for all of
them in one message. Where the user does not know a value, leave the field as `not
set`; never fill it in with a guess. A list that needs a `not set` field becomes a
question for the user in the fit table.

The file is the only source of facts for every entry. When the user supplies a fact
later in the run (a shorter description for one list, a store link that was `not
set`, a changed end date), it goes into this file first, with `Last confirmed`
updated, and into the entries from there. Text dictated for a single entry that is
not in the file is not used.

## Template

```markdown
# Deal intake: <product name>

Last confirmed: <YYYY-MM-DD>

## Product
- Name:
- One line, what it does (no marketing words, this is what most lists print):
- Longer description (two or three sentences, for forms that allow it):
- Platforms it runs on (exact: iPhone, iPad, Mac, Apple Watch, Android, Windows, web):
- Platforms it does NOT run on (so no entry ever claims them):
- Category, in the user's words (home inventory, QR codes, note taking):
- Product site URL:
- Store URL(s):
- Pricing page URL (or "the price is shown in the app, on the upgrade screen"):
- Icon URL (square, https, 512 px or larger, a link that does not expire):
- Publicly available since (month and year; some lists want six months or more):
- Maker name as it should appear:
- Company name, when a form asks for one:
- Contact email for forms:

## Deal
- Sale name (Black Friday 2026, spring sale, launch week):
- What is discounted (plan name: lifetime, yearly, Pro):
- Normal price, with currency:
- Sale price, with currency:
- Discount as a percentage:
- Code, or "no code needed":
- Where the sale price shows (in the app on the upgrade screen, at checkout, on the pricing page):
- Start date (YYYY-MM-DD):
- End date (YYYY-MM-DD), and the time zone of the end:
- Sale page URL that shows the sale price, the normal price and the dates:
- Price note for other countries, if prices differ by store region:

## Boundaries
- Paid placements: no (default) / ask me per list
- Forms that need an account or a sign-in: hand over the text (default) / skip
- Lists to skip, and why:
- Anything that must not be claimed:
```

One thing to say when asking: nothing is published, submitted, posted or pushed
without the user's yes, but the search for lists and the check for existing entries
read and search public pages and repositories before any approval, and the product
name, its domain and the maker's name are among the search terms.

## Checks before the intake is accepted

- Open the sale page. It must load without JavaScript tricks and show the sale price,
  the normal price and the dates. Several lists fetch it with a bot and fail the entry
  if any of the three is missing. If it does not load or a value is missing, say
  which, and open it again when the user says it is fixed; the user's word that the
  page is live does not stand in for the page loading.
- Compare today with the start date. Before the start, the sale page may show the
  normal price only; lists that check the live price get their entries on or after
  the start date, and the fit table says so.
- Open the store URL. If the store page shows a price that differs from the intake
  (a different lifetime tier, a regional price), note it in the intake under the deal,
  because a curator who checks the store will see it. The sale page is what entries
  link to in that case.
- The icon URL must be square, https and 128 px or larger (some lists want 256 or
  512). App Store CDN links change when the app ships a new icon; re-check the link
  on the day of submission.
- Dates carry the year. A list that prints "Nov 18 - Dec 4" still wants to know it is
  this year.

## What the intake is not

It is not a copy deck. Lists print a one-line description, a deal line and a link.
Marketing adjectives get cut by maintainers or get the entry closed. The one-line
description says what the product does and for which platforms, nothing else.
