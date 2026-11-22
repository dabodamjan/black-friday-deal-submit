# Forms, emails and forum posts

The skill prepares the text. The user submits it. No exceptions for a form that
"needs no account": the user still presses the button, because the submission goes
out under their name and email.

## Which route, when a list has more than one

A list may offer an email address and a sign-in form, or a form and a forum thread.
The route with no sign-in and no account comes first: email over a form behind a
sign-in, a plain form over an account. Both are named in the fit table's Route
column; the entry is prepared for the first one.

## Web forms

For each form, hand over a table the user can work down the page with:

```
| Field (as labelled on the form) | Required | Limit | Value |
```

- Field names and order follow the live form. If the fields could not be read
  (JavaScript only, behind a sign-in), say which ones are unread and give values for
  the ones that were.
- Values come from the intake. Where a form wants a shorter text than the intake has,
  cut the intake text; do not write new sentences.
- Price fields often want digits only (`29.99`, not `$29.99`). Date pickers want a
  date, not a range. Say so next to the field.
- Dropdowns: name the option to pick from the ones read on the page. When the options
  could not be read, say "pick the option closest to <category>" and name the fallback.
- File uploads (an icon, a screenshot): give the file path on disk or the URL to
  download from, and the size the form wants. The skill does not upload.
- Forms that draft fields from the product's website and overwrite typed text: warn
  the user to enter the values after the draft loads and to read them back before
  sending.
- After the user submits, ask for the confirmation text the site showed (review
  time, a share link) and put it in the status file.

The skill does not create accounts, does not sign in, does not tick terms boxes, does
not pay for an expedited review or a featured slot, and does not subscribe the user
to a newsletter to reach a form. A form behind any of these is handed over with the
values and the note "behind a sign-in; your call". A free listing with paid upsells
is a free route; the upsells are named in the fit table and never taken.

## Emails

Plain text, no Markdown, ready to paste:

```
To: <address as published on the list's own page>
Subject: <sale name> deal: <Product>

<body>
```

The body carries, in this order: who is writing and what the product is in one
line, the offer line (plan, sale price, normal price, discount), the dates, the code
or "no code needed", where the price shows, the sale page URL, the store URL, and a
one-line sign-off with the user's name. No pitch, no attachments unless the list
asks, no follow-up email unless the user asks.

The address must come from the list's own public page or call for deals, never from
memory and never from a private message. An email to a person who runs a list (a
blogger's yearly call for deals) is the same route with the same rules. The user
sends from their own account; the skill records `sent` with the date once they
confirm.

## Forum posts

A forum thread is someone else's living room, and posting there needs an account the
skill never creates; the fit table says `forum post, needs an account`. Before
drafting, read the forum's rules page and the thread itself: does the forum allow
makers to post their own product, and have others done so in this thread without
objection? If the rules forbid it, or the forum has a rule against posts written with
AI help, the skill drafts nothing and says why.

When a post is allowed, the draft follows what the thread already accepts: a
disclosure line first ("I'm the developer, so this is self-interested."), one line
on what the product does, the plain price and dates, one link. Short. The user posts
it from their own account.

## Direct messages and social replies

Not a submission route. A list that takes deals only by DM is handed over with the
draft text, and the user sends it.
