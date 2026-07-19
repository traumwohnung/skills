---
name: ui
description: Practical visual design guidance for building polished user interfaces. Use whenever creating, styling, reviewing, or refining any UI — web pages, app screens, components, dashboards, landing pages, forms, emails — or when the user mentions layout, spacing, typography, color palettes, shadows, hierarchy, or says something "looks off", "looks bland", or "needs polish", even if they don't explicitly ask for design help.
---

# UI Design

Make interfaces look deliberately designed without needing artistic talent. The core insight: most of what makes a UI "look good" is not decoration — it's hierarchy, spacing, and constraint. Get those right with the systems below and the rest is refinement.

## Core mindset

1. **Design features, not shells.** Never start with the navigation, header, or page chrome. Start with one piece of real functionality (the search form, the data card, the checkout step) and let the shell grow around it. You can't make good navigation decisions before real features exist.
2. **Low fidelity first, grayscale first.** Sketch layouts before polishing details. Even in high fidelity, hold off on color: design in grayscale so spacing, contrast, and size carry the hierarchy, then layer color on top. Ship the smallest useful version — don't design UI for functionality you aren't ready to build.
3. **Systems kill decision fatigue.** Never hand-pick pixel values or colors ad hoc. Define constrained scales up front (below) and pick from them. When choosing between scale values, take a guess, then compare against the neighbors on either side — two of the three will usually be obviously wrong.
4. **Personality is concrete.** Serious vs. playful is determined by four levers: typeface (serif = classic, rounded sans = playful, neutral sans = plain), color (blue = safe, gold = sophisticated, pink = playful), border radius (none = formal, large = friendly — pick one and stay consistent), and the tone of your copy. Decide the personality once, then apply the levers consistently.

## The default systems

Use these unless the project already has its own. All values in px (or the rem equivalent).

**Spacing & sizing scale** (base 16, ~25%+ jumps, denser at the small end):

```
4, 8, 12, 16, 24, 32, 48, 64, 96, 128, 192, 256, 384, 512, 640, 768
```

**Type scale** (hand-picked, not ratio-generated; use px or rem, never em):

```
12, 14, 16, 18, 20, 24, 30, 36, 48, 60, 72
```

**Font weights:** two are enough — normal (400/500) for most text, heavy (600/700) for emphasis. Never go below 400 in UI text; de-emphasize with a lighter color or smaller size instead of a thin weight.

**Text colors:** three levels — dark for primary content, mid grey for secondary, light grey for tertiary. (On colored backgrounds, see `references/color.md`.)

**Color palette:** greys (8–10 shades), one or two primaries (5–10 shades each), and accent colors for semantic states (red/destructive, yellow/warning, green/positive) plus any categorical needs. Define every shade up front on a 100–900 scale; never generate shades with lighten/darken functions at runtime.

**Shadow elevation scale** (5 steps, small = barely raised, large = floating):

```
0 1px 3px rgba(0,0,0,.2)
0 4px 6px rgba(0,0,0,.2)
0 5px 15px rgba(0,0,0,.2)
0 10px 24px rgba(0,0,0,.2)
0 15px 35px rgba(0,0,0,.2)
```

Buttons get small shadows, dropdowns medium, modals large. Pick the shadow by deciding where the element sits on the z-axis, not by eyeballing.

## Fast heuristics (apply everywhere)

- **Start with too much white space, then remove.** Cramped is the default failure mode. Dense layouts are fine, but only as a deliberate choice.
- **More space around groups than within them.** If the gap between a label and its input equals the gap between form fields, the grouping is ambiguous and the UI reads as noise.
- **Emphasize by de-emphasizing.** If the important thing doesn't stand out, mute its competitors (softer color, no background) instead of making it louder.
- **Don't fill the screen.** Give elements the width their content needs — a 600px form on a 1400px canvas is correct. Constrain with max-width; use fixed widths for sidebars, not grid percentages.
- **Hierarchy beats semantics.** One primary action per page (solid, high contrast), secondary actions quieter (outline/soft), tertiary as links. Destructive actions are only big-red-bold when they're the primary action (e.g. in a confirmation dialog).
- **Visual hierarchy ≠ document hierarchy.** An `h1` can be styled small; section titles are usually labels, not headlines.
- **Labels are a last resort.** Formats and context usually identify data ("12 left in stock", not "In stock: 12"). When you need labels, style them as supporting text.

## References

Read the relevant file when working in that area:

- `references/hierarchy.md` — controlling emphasis with size, weight, color, and contrast
- `references/layout.md` — spacing, sizing, grids, responsive scaling
- `references/typography.md` — fonts, line length/height, alignment, letter-spacing
- `references/color.md` — building palettes in HSL, shades, greys, accessibility
- `references/depth.md` — light-source logic, shadows, layering
- `references/images.md` — photos, text-over-image, icon sizing, user-uploaded content
- `references/polish.md` — finishing touches for bland-but-correct designs, empty states, borders

## Review checklist

When reviewing or refining an existing UI, check in this order:

1. Is there a clear primary element per screen/section, with everything else visibly subordinate?
2. Is spacing generous, from the scale, and unambiguous about grouping?
3. Are font sizes/weights from the scales, with at most 3 text-color levels?
4. Are colors from a defined palette with hand-picked shades?
5. Do shadows/depth match each element's importance?
6. Could a border be replaced with spacing, a background-color change, or a shadow?
7. Does the empty state sell the feature instead of showing a blank table?
