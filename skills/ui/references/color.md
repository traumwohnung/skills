# Color

## Work in HSL

Hex/RGB obscure the relationships between colors; HSL encodes what the eye perceives:

- **Hue** (0–360°): position on the color wheel. 0° red, 120° green, 240° blue.
- **Saturation** (0–100%): vividness. 0% is grey regardless of hue.
- **Lightness** (0–100%): 0% black, 100% white, 50% = the pure hue.

Don't confuse HSL with HSB/HSV (common in design tools): 100% brightness in HSB is only white at zero saturation. Browsers speak HSL.

## Palette shape

A real interface needs far more than a five-swatch palette:

- **Greys:** 8–10 shades. Start near-black (true `#000` looks unnatural) and step to near-white. Most of the UI — text, backgrounds, panels, borders — is grey.
- **Primary:** 1–2 brand colors, 5–10 shades each. Ultra-light shades tint alert/badge backgrounds; dark shades work as text.
- **Accents / semantic:** red (destructive), yellow (warning), green (success/positive), plus attention-grabbers for highlights and however many categorical colors charts/tags need. Multiple shades each, used sparingly.

A complex UI legitimately ends up with ~10 hues × 5–10 shades.

## Defining shades

Never generate shades at runtime with lighten/darken functions — that's how 35 near-identical blues happen. Fix a 100–900 scale per color up front:

1. **Base (500):** for primaries, pick what would look right as a solid button background.
2. **Edges:** 900 = darkest usable (think text on a light tint); 100 = lightest (think tinted alert background). Keep the base hue, tune saturation/lightness by eye.
3. **Fill in:** pick 700 and 300 as visual midpoints, then 800/600/400/200 the same way.

Greys follow the same process; the base matters less than good edges (darkest text color, faint off-white background).

There is no formula that replaces judgment — tweak by eye, but resist adding new one-off shades once the scale exists.

## Saturation vs. lightness

Saturation's visual impact collapses near the lightness extremes: the same saturation looks vivid at 50% lightness and washed out at 90%. So as shades move away from 50% lightness, **raise saturation** to keep them from greying out.

**Perceived brightness trick:** hues differ in inherent brightness (yellow/cyan/magenta bright; red/green/blue dark). To lighten a color without desaturating toward white, rotate its hue up to 20–30° toward the nearest bright hue (60°, 180°, 300°); to darken, rotate toward 0°, 120°, or 240°. Example: dark yellows go rich orange instead of muddy brown. Beyond ~30° it reads as a different color.

## Greys have temperature

Saturating greys with a touch of blue makes a UI feel cool; a touch of yellow/orange makes it warm. Whatever the choice, boost the saturation on the very light and very dark greys so the temperature stays consistent across the scale.

## Accessibility without ugliness

Targets: 4.5:1 contrast for normal text, 3:1 for large text.

- **Flip the contrast:** white-on-color requires a surprisingly dark background that dominates the page. Instead use dark colored text on a light tint of the same hue (e.g. dark blue on pale blue) — accessible, and quieter in the hierarchy.
- **Colored text on colored backgrounds:** when raising lightness can't reach the ratio without hitting white, rotate the hue toward a brighter one (cyan/magenta/yellow direction) to gain contrast while staying colorful.

## Never color alone

Colorblind users can't parse meaning carried only by hue:

- Pair red/green deltas with icons or arrows (▲/▼).
- For chart lines, differentiate by lightness contrast (light vs. dark shades), not just by distinct hues.

Color reinforces information the design already states another way — it is never the sole channel.
