# Hierarchy

Visual hierarchy — making important things look important and everything else recede — is the single highest-leverage design skill. It has nothing to do with artistic flair: when every element competes at equal volume, a UI reads as a noisy wall of content; deliberately de-emphasize the secondary and tertiary material and the same layout, in the same colors and fonts, suddenly looks designed.

## The three levers

Control emphasis with **size**, **weight**, and **color** — and don't lean on size alone. Size-only hierarchy is self-defeating: primary content balloons past what it needs while secondary content shrinks into illegibility.

- Bolding a heading lets it stay at a reasonable size, and weight usually communicates importance better than area anyway.
- A softer color de-emphasizes supporting text without the readability cost of tiny type.

Practical limits:

- **3 text colors max:** dark for primary content (a headline), mid grey for secondary (a publish date), light grey for tertiary (footer fine print).
- **2 font weights max:** 400/500 for body, 600/700 for emphasis. Weights below 400 are for large display text only — at UI sizes they're unreadable. To mute text, reach for a lighter color or a smaller size, never a thinner weight.

## De-emphasis on colored backgrounds

Grey text works on white because what it actually does is *reduce contrast with the background*. Move to a colored background and grey stops working — it reads as dingy, not quiet. Reduced-opacity white is the other tempting shortcut, and it fails too: the text looks washed out or disabled, and over an image or pattern the background bleeds through the letters.

The correct move: hand-pick the muted color. Keep the background's hue and adjust saturation and lightness until the text recedes the right amount. Contrast drops without the faded look.

## Emphasize by de-emphasizing

When the key element won't stand out and there's nothing left to add to it, subtract from its competitors instead:

- Active nav item not popping despite its accent color? Soften the inactive items so they fall back.
- Sidebar visually competing with the main content? Strip its background panel and let it sit directly on the page background — less structure, clearer focus.

## Weight vs. contrast are interchangeable

Emphasis is fundamentally about how much surface area an element claims and how hard it contrasts. Bold text feels emphasized because more pixels per letter are ink rather than background. The two properties can compensate for each other:

- **Heavy element too loud:** solid icons sitting next to text grab attention like bold type — and icons have no "regular weight" variant. Rebalance by lowering their contrast with a softer color.
- **Faint element too weak:** a 1px border can be too subtle in a light grey but harsh in a dark one. Keep the soft color and add weight — 2px of the light grey emphasizes without harshness.

## Actions form a pyramid

Nearly every screen has one true primary action, a few secondary, and some rarely-used tertiary ones. Style by position in that pyramid:

- **Primary:** solid, high-contrast fill. Unmissable.
- **Secondary:** outline or low-contrast fill. Clear but quiet.
- **Tertiary:** link styling. Discoverable, unobtrusive.

Semantics come second to hierarchy. A destructive button is *not* automatically big, red, and bold — if deletion is a secondary action on this screen, give it a secondary or even link treatment. Save the alarming red fill for the confirmation dialog, where the destructive action genuinely is primary. Hierarchy-first action design collapses a busy row of screaming buttons into a page that communicates.

## Labels and data

Dumping fields as `label: value` pairs flattens everything to equal importance and makes real hierarchy impossible.

1. **Skip the label when format identifies the data.** An email address, a phone number, a price — the shape says what it is.
2. **Skip it when context identifies the data.** A department name below a person's name in a directory needs no "Department:" prefix.
3. **Fold the label into the value:** "3 bedrooms", "12 left in stock", "Sent 2 hours ago". One styled unit instead of a label/value pair.
4. **When labels are genuinely needed** — dashboards where similar metrics must be scannable — treat them as supporting content: smaller, lower contrast, lighter weight, or all three. The value is the point.
5. **Invert only when users hunt for the label.** On dense spec pages, people scan for "Depth", not for "7.6mm" — there, darken the label slightly and lighten the value slightly. Keep the value clearly readable; it's still the information.

## Markup does not dictate style

Semantics and styling are separate decisions. An `h1` is often best rendered small: page and section titles frequently function as labels for the content below, which is the real focus — a big bold "Manage Account" title steals attention from the settings it introduces. At the limit, keep the heading in the markup for accessibility and hide it visually. Pick elements for meaning; style them for hierarchy.
