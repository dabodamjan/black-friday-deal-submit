# Examples: finished entries from the November 2026 run

Three iPhone, iPad and Mac apps by the author ran the same deal, each 50% off its
lifetime purchase from 18 November to 4 December 2026, no code needed, with a public
sale page per app ([Itemlist](https://getitemlist.app/black-friday),
[QRGenie](https://qrgenie.app/black-friday),
[BarcodeCraft](https://barcodecraft.com/black-friday)). The entries below are what
went into each list, in that list's own format, and were merged there in November
2026. They show what a finished entry looks like; the facts in them come from one
intake file, and the format from each list's rules as read that day. Prices, URLs
and platform names match the intake character for character; the dates match it in
value and take each list's own style (an en dash on one list, "to" on another, ISO
dates in the JSON files).

Itemlist and BarcodeCraft run on iPhone and iPad only; QRGenie also has a Mac app.
That is why the Mac-only lists carry QRGenie alone.

## The intake behind the entries (QRGenie)

```markdown
## Product
- Name: QRGenie
- One line, what it does: QR code generator for iPhone, iPad and Mac
- Longer description: QR code generator for iPhone, iPad and Mac. Codes are made on your device and never expire. Export PNG, JPG, PDF or SVG with no watermark.
- Platforms it runs on: iPhone, iPad, Mac
- Platforms it does NOT run on: Android, Windows, web
- Category: QR codes (utilities)
- Product site URL: https://qrgenie.app
- Store URL: https://apps.apple.com/us/app/qr-code-generator-qrgenie/id6740281687
- Pricing page URL: the price is shown in the app, on the upgrade screen
- Publicly available since: January 2025
- Maker name as it should appear: Damjan Dabo

## Deal
- Sale name: Black Friday 2026
- What is discounted: lifetime
- Normal price: $19.99 (US App Store)
- Sale price: $9.99
- Discount: 50%
- Code: no code needed
- Where the sale price shows: in the app, on the upgrade screen
- Start date: 2026-11-18
- End date: 2026-12-04
- Sale page URL: https://qrgenie.app/black-friday
- Price note for other countries: prices are for the US App Store; other countries see their local price, at about half the normal one
```

## Markdown table rows

**black-friday-deals (dqhieu)**, one line per product after the last row, exactly five
pipes, 🤑 for 50% or more, the list's own en dash in the dates:

```
|🤑|[Itemlist](https://www.getitemlist.app/black-friday/)| Home inventory for iPhone and iPad. | **50% OFF** lifetime PRO: $29.99, down from $59.99, no code needed (Nov 18 – Dec 4, 2026)|
|🤑|[QRGenie](https://qrgenie.app/black-friday)| QR code generator for iPhone, iPad and Mac. | **50% OFF** lifetime: $9.99, down from $19.99, no code needed (Nov 18 – Dec 4, 2026)|
|🤑|[BarcodeCraft](https://www.barcodecraft.com/black-friday)| Barcode generator for iPhone and iPad. | **50% OFF** lifetime: $4.99, down from $9.99, no code needed (Nov 18 – Dec 4, 2026)|
```

**Awesome Black Friday / Cyber Monday (trungdq88)**, end of the "Productivity Mobile
Apps" table, bold discount and sale price, old price struck through. The list's merge
bot holds makers to two apps, so only two rows went in:

```
| 📦 | [Itemlist](https://www.getitemlist.app/black-friday/) | Home inventory for iPhone and iPad. Track what you own by location, room and container, with photos, values and search across every field. | **50% OFF lifetime PRO**: ~~$59.99~~ **$29.99**, Nov 18 to Dec 4, 2026. No code needed |
| 🔳 | [QRGenie](https://qrgenie.app/black-friday) | QR code generator for iPhone, iPad and Mac. Codes are made on your device and never expire. Export PNG, JPG, PDF or SVG with no watermark. | **50% OFF lifetime**: ~~$19.99~~ **$9.99**, Nov 18 to Dec 4, 2026. No code needed |
```

**Awesome Black Friday & Cyber Monday Deals (twf-nikhila)**, one row at the end of the
category table, 💸 for 50% or more, ♾️ for lifetime, dates with a spaced hyphen:

```
| [Itemlist](https://www.getitemlist.app/black-friday/) | Home inventory for iPhone and iPad | 💸 ♾️ **50% OFF** lifetime PRO: $29.99, down from $59.99 · no code needed | Nov 18, 2026 - Dec 4, 2026 |
| [QRGenie](https://qrgenie.app/black-friday) | QR code generator for iPhone, iPad and Mac | 💸 ♾️ **50% OFF** lifetime: $9.99, down from $19.99 · no code needed | Nov 18, 2026 - Dec 4, 2026 |
| [BarcodeCraft](https://www.barcodecraft.com/black-friday) | Barcode generator for iPhone and iPad | 💸 ♾️ **50% OFF** lifetime: $4.99, down from $9.99 · no code needed | Nov 18, 2026 - Dec 4, 2026 |
```

**rare-big-deal**, bottom of the "iOS Apps > Productivity" table, with an expiry date
column:

```
| 📦 | [Itemlist](https://www.getitemlist.app/black-friday/) | Home inventory for iPhone and iPad. Track what you own by location, room and container, with photos, values and search across every field. | **50% OFF** lifetime PRO: $29.99, down from $59.99, Nov 18 to Dec 4. No code needed | 2026-12-04 |
| 📱 | [QRGenie](https://qrgenie.app/black-friday) | QR code generator for iPhone, iPad and Mac. Codes are made on your device and never expire. Export PNG, JPG, PDF or SVG with no watermark. | **50% OFF** lifetime: $9.99, down from $19.99, Nov 18 to Dec 4. No code needed | 2026-12-04 |
| 📱 | [BarcodeCraft](https://www.barcodecraft.com/black-friday) | Barcode generator for iPhone and iPad. Makes Code 128, Code 39, Code 93, EAN-13, EAN-8, PDF417 and Aztec codes and shares them as PNG. | **50% OFF** lifetime: $4.99, down from $9.99, Nov 18 to Dec 4. No code needed | 2026-12-04 |
```

**black-friday-deals (Pimjo)**, end of the "Productivity Tools" table, name bold inside
the link, the list's own en dash. The README is stored with Windows line endings and
the edit kept them:

```
| [**Itemlist**](https://www.getitemlist.app/black-friday/) | Home inventory for iPhone and iPad. Track what you own by location, room and container, with photos, values and search across every field. | **50% OFF** lifetime PRO: $29.99, down from $59.99 (no code needed) | Nov 18 – Dec 4, 2026 |
| [**QRGenie**](https://qrgenie.app/black-friday) | QR code generator for iPhone, iPad and Mac. Codes are made on your device and never expire. Export PNG, JPG, PDF or SVG with no watermark. | **50% OFF** lifetime: $9.99, down from $19.99 (no code needed) | Nov 18 – Dec 4, 2026 |
| [**BarcodeCraft**](https://www.barcodecraft.com/black-friday) | Barcode generator for iPhone and iPad. Makes Code 128, Code 39, Code 93, EAN-13, EAN-8, PDF417 and Aztec codes and shares them as PNG. | **50% OFF** lifetime: $4.99, down from $9.99 (no code needed) | Nov 18 – Dec 4, 2026 |
```

## One file per deal

**Indie Goodies (onmyway133/blackfriday)**, `2026/qrgenie.json`, description without a
trailing period, platforms from the schema's list:

```json
{
  "name": "QRGenie",
  "url": "https://qrgenie.app/black-friday",
  "description": "QR code generator for iPhone, iPad and Mac. Codes are made on your device and never expire. Export PNG, JPG, PDF or SVG with no watermark",
  "category": "utilities",
  "platforms": ["ios", "ipad", "mac"],
  "deal": "50% off lifetime: $9.99, down from $19.99, Nov 18 to Dec 4. No code needed",
  "pricing": "lifetime",
  "price": { "regular": 19.99, "sale": 9.99, "currency": "USD" },
  "discount": 50,
  "startDate": "2026-11-18",
  "endDate": "2026-12-04",
  "icon": "<square https icon URL, 128 px or larger>"
}
```

**Mac and iOS Black Friday Deals (longseespace/mac-black-friday)**, `deals/qrgenie.json`
from the list's template, `url` pointing at the page that shows the sale price:

```json
{
  "name": "QRGenie",
  "url": "https://qrgenie.app/black-friday",
  "platforms": ["macOS", "iOS", "iPadOS"],
  "category": "utilities",
  "description": "QR code generator for iPhone, iPad and Mac. Codes are made on your device and never expire. Export PNG, JPG, PDF or SVG with no watermark",
  "discount": "50% off lifetime: $9.99",
  "prices": [{ "plan": "Lifetime", "before": 19.99, "after": 9.99 }],
  "terms": "You don't need a code. The sale price shows on the upgrade screen in the app.",
  "starts": "2026-11-18",
  "ends": "2026-12-04",
  "maker": "Damjan Dabo",
  "makerUrl": "https://qrgenie.app/",
  "icon": "<square https icon URL, 256 px or larger>"
}
```

**Black-Friday-Deals (mRs-)**, `deals/2026/utility-software/qrgenie.yml`; the README
there is generated and is never edited:

```yaml
name: "QRGenie"
url: "https://apps.apple.com/us/app/qr-code-generator-qrgenie/id6740281687"
description: "QR code generator for iPhone, iPad and Mac. Codes are made on your device and never expire. Export PNG, JPG, PDF or SVG with no watermark"
discount: "50% off lifetime: $9.99, down from $19.99"
percent: 50
terms: "No code needed. The sale price shows on the upgrade screen in the app."
starts: "2026-11-18"
ends: "2026-12-04"
```

**awesome-black-friday-for-developers (tushargugnani)**, one list item in
`deals/2026.yaml`, then the list's own `validate.py` and `build_readme.py` were run and
both files committed:

```yaml
  - name: QRGenie
    url: https://qrgenie.app/black-friday
    category: design
    offer: "Black Friday 2026: 50% OFF lifetime, $19.99 to $9.99, no code needed (Nov 18 - Dec 4, 2026)"
    description: QR code generator for iPhone, iPad and Mac. Codes are made on your device and never expire. Export PNG, JPG, PDF or SVG with no watermark.
```

## An HTML table row

**Awesome Black Friday / Cyber Monday for Mac Apps (s1ntoneli)**, end of the
Productivity table; the README uses an HTML table, 🔥 for 50% or more:

```html
    <tr>
      <td align="center">🔥</td>
      <td><a href="https://qrgenie.app/black-friday">QRGenie</a></td>
      <td>QR Code Generator (macOS, iPhone, iPad)</td>
      <td>QR code generator for iPhone, iPad and Mac. Codes are made on your device and never expire. Export PNG, JPG, PDF or SVG with no watermark</td>
      <td><strong>50% OFF</strong> Lifetime · $19.99 → $9.99, one payment · No code needed</td>
      <td>Nov 18 - Dec 4, 2026</td>
    </tr>
```

## A pull request body

The body that went with the s1ntoneli row, following what that list's contributing
file asks for:

```
Adds QRGenie to Productivity, at the end of the table.

- Product: https://qrgenie.app (App Store: https://apps.apple.com/us/app/qr-code-generator-qrgenie/id6740281687)
- Platform: macOS, iPhone, iPad
- Deal: 50% off the lifetime purchase, $19.99 to $9.99, one payment
- Code: none needed, the sale price shows in the app
- Dates: Nov 18 to Dec 4, 2026
- Sale page with the price and dates: https://qrgenie.app/black-friday

I'm the maker of QRGenie. No affiliate or referral compensation.
```

## What changed after submission

- The trungdq88 list's merge bot asked for one of three rows to come out ("The list
  allows at most 2 apps per maker",
  [comment](https://github.com/trungdq88/Awesome-Black-Friday-Cyber-Monday/pull/2838#issuecomment-6985347503)).
  The written rule in the list's rules issue says
  something softer (more than two closely related deals go in as a single entry);
  the bot enforces a cap of two. One row was removed in a new commit and the pull
  request merged. The record carries both, each labelled as what it is.
- Indie Goodies added a two-deals-per-maker-per-year rule to its contributing file
  on 18 November, the same day these entries went in, and its pull request template
  carries a licence-agreement box. That box is the submitter's to tick, not the
  skill's.
- The twf-nikhila maintainer moved one row to a different category when merging, and
  asked for a star and a share in the
  [merge comment](https://github.com/twf-nikhila/Awesome-Black-Friday-Cyber-Monday-deals/pull/676#issuecomment-7000254872).
  The row stayed as merged; the
  request was noted and not acted on by the skill.
- A deal site with no edit route still showed an entry from an earlier year with an
  outdated line in it. It was left alone rather than duplicated; the record notes
  that entries there cannot be edited.
