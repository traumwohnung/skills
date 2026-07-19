# Color

## Work in HSL

Hex and RGB hide relationships — two colors that look obviously related can have completely unrelated hex codes. HSL encodes the attributes the eye actually perceives:

- **Hue** (0–360°): position on the color wheel; what makes two different blues both read as "blue". 0° red, 120° green, 240° blue.
- **Saturation** (0–100%): vividness. At 0% everything is grey and hue is meaningless.
- **Lightness** (0–100%): distance from black (0%) to white (100%); 50% is the pure hue.

Don't confuse HSL with the HSB/HSV mode common in design tools: HSB's 100% brightness only means white at zero saturation — at full saturation it equals HSL's 50% lightness. CSS speaks HSL, so for web work HSL is the working format.

## Palette shape

Five swatches from a palette generator cannot build a real interface. A production palette has three tiers:

- **Greys — 8–10 shades.** Text, backgrounds, panels, borders: most of a UI is grey, and three or four steps run out immediately. Pure black looks unnatural; start from a very dark grey and step to near-white in even perceptual increments.
- **Primary — one or two colors, 5–10 shades each.** These define the product's identity and drive primary actions and active states. Ultra-light shades tint alert and badge backgrounds; dark shades work as text on those tints.
- **Accents — several colors, multiple shades each, used sparingly.** Semantic states need their own hues: red for destructive, yellow for warnings, green for success/positive. Add an eye-catcher for highlights (new-feature callouts) and however many categorical hues charts, calendars, or tags demand.

A complex UI legitimately lands near ten hues × 5–10 shades. That's not palette bloat; it's the real requirement.

## Defining shades

Runtime `lighten()`/`darken()` calls are how a codebase accumulates dozens of near-identical blues. Shades are design decisions: fix them up front on a 100–900-style scale (nine steps divide the range conveniently).

1. **Base (500) first.** For a primary or accent: the shade you'd use as a solid button background is a reliable anchor. There's no numeric rule ("start at 50% lightness") that survives contact with real hues — judge by eye.
2. **Edges next.** 900 = the darkest useful version (imagine it as text on a pale tint of the same hue); 100 = the lightest (imagine it as that pale alert background). An alert component exercises both at once, making it a good test bench. Hold the base hue; tune saturation and lightness.
3. **Fill the gaps.** 700 and 300 should each feel like the perceptual midpoint of their gap; that leaves 800, 600, 400, 200, filled the same way.

Greys use the same procedure, except the edges matter more than the base: darkest grey = your darkest text color, lightest = a barely-off-white background.

Expect to nudge shades once they're in use — eyes beat arithmetic. But hold the line on adding *new* shades ad hoc; an undisciplined palette is no palette.

## Saturation vs. lightness

Saturation loses visual force near the lightness extremes: identical saturation values look vivid at 50% lightness and bleached at 90%. So as a shade moves away from mid-lightness in either direction, **raise its saturation** to keep the color alive. Subtle per-shade, but across a whole tinted UI region the difference is obvious.

**Perceived brightness.** Hues are not equally bright: at identical saturation/lightness, yellow looks far lighter than blue. Perceived brightness is computable from RGB, and around the wheel it has three dark troughs (red 0°, green 120°, blue 240°) and three bright peaks (yellow 60°, cyan 180°, magenta 300°). This yields a second lightening lever:

- **Rotate hue instead of (or alongside) lightness.** Toward the nearest bright peak to lighten; toward the nearest dark trough to darken. Unlike pushing lightness, this doesn't drag the color toward white or black — intensity survives.
- Classic application: yellows. Darkening yellow by lightness alone turns it brown; rotating toward orange while darkening keeps the dark shades warm and rich.
- Stay within 20–30° of rotation, or the shade stops reading as the same color.

## Greys have temperature

"Grey" in real palettes is rarely 0% saturation. A touch of blue makes greys feel cool and technical; a touch of yellow/orange makes them warm and inviting — the same warm/cool split as light bulbs. Two rules:

- Pick a temperature and apply it to the whole grey scale, not individual shades.
- Boost saturation on the very light and very dark ends (see above), or those shades drift back toward neutral and the temperature looks inconsistent.

The amount is taste: barely tint for a hint, saturate harder to push the whole interface warm or cool.

## Accessibility without ugliness

Contrast targets: 4.5:1 for normal text, 3:1 for large text (~18px+).

- **Flip the contrast.** White text on a colored background needs a surprisingly dark background to hit 4.5:1 — and a big dark slab hijacks the page hierarchy. Invert: dark text of the hue on a light tint of the hue (dark blue on pale blue). Same ratio, same color identity, a fraction of the visual weight.
- **Colored text on colored backgrounds** (e.g. secondary text inside a dark panel): pushing lightness up often can't reach the ratio without arriving at white. Rotate the hue toward a bright peak (cyan/magenta/yellow direction) instead — contrast rises while the text stays colorful.

## Never color alone

Color must reinforce information, never solely carry it — otherwise colorblind users lose the message:

- Green-up/red-down metrics need a second channel: add directional icons or arrows.
- Multi-line charts distinguished only by hue are unreadable under red-green blindness; differentiate lines by *lightness* contrast (light vs. dark shades), which survives any color vision deficiency.
