# Hierarchy

Visual hierarchy — making important things look important and everything else recede — is the single highest-leverage design skill. A noisy UI where everything competes for attention reads as "undesigned" regardless of fonts or colors.

## The three levers

Control emphasis with **size**, **weight**, and **color** — and don't lean on size alone. Oversized headlines plus microscopic captions is the classic symptom of size-only hierarchy.

- Bolding a heading lets it stay at a reasonable size and communicates importance better than making it huge.
- A softer color de-emphasizes supporting text without shrinking it into illegibility.

Practical limits:

- **3 text colors max:** dark (primary), mid grey (secondary), light grey (tertiary).
- **2 font weights max:** 400/500 for body, 600/700 for emphasis. Weights under 400 are for large display text only — never for de-emphasis. Use color or size instead.

## De-emphasis on colored backgrounds

Grey text works on white because it *reduces contrast* with the background. On a colored background, grey just looks dirty, and white-at-reduced-opacity looks washed out (and lets background images bleed through). Instead, hand-pick a color: keep the background's hue, then adjust saturation and lightness until it reads as "quieter" text.

## Emphasize by de-emphasizing

When the key element won't stand out no matter what you add to it, subtract from its rivals:

- Active nav item not popping? Soften the inactive items rather than decorating the active one.
- Sidebar competing with content? Remove its background color and let it sit on the page background.

## Weight vs. contrast balancing

Emphasis is really about surface area and contrast, and the two can compensate for each other:

- **Heavy element too loud** (e.g. a solid icon next to text): lower its contrast with a softer color.
- **Low-contrast element too faint** (e.g. a 1px border that disappears when light, but looks harsh when dark): keep the soft color and increase the weight (2px).

## Actions have a pyramid

Every screen has roughly one primary action, a few secondary, and some tertiary:

- **Primary:** solid, high-contrast fill. Obvious at a glance.
- **Secondary:** outline or low-contrast fill. Clear but quiet.
- **Tertiary:** styled like links. Discoverable, not distracting.

Semantics come second: a delete button is *not* automatically big and red. If deleting is a secondary action on the page, give it a secondary (or link) treatment; save the bold red fill for the confirmation dialog where deletion *is* the primary action.

## Labels and data

Displaying raw `label: value` pairs flattens hierarchy — everything looks equally important.

1. **Drop the label** when format (email, phone, price) or context (a role under a name) already identifies the data.
2. **Fold the label into the value:** "3 bedrooms", "12 left in stock", "Sent 2 hours ago".
3. **When labels are needed** (scannable dashboards), keep them secondary: smaller, lighter, quieter than the value.
4. **Invert only when users scan for the label** (spec sheets: people look for "Depth", not "7.6mm") — then darken the label slightly, but keep the value readable.

## Markup does not dictate style

Choose HTML elements for semantics, styles for hierarchy. Page titles marked up as `h1` frequently work best visually small — like labels — because the content under them is the real focus. It's even legitimate to visually hide a heading that exists only for accessibility.
