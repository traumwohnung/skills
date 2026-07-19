# Layout & Spacing

## White space: start with too much

The instinct is to add space only until things stop looking cramped — that produces the bare minimum of breathing room. Invert the process: give everything clearly too much space, then remove until it looks right. What feels excessive on one element usually reads as "just enough" in a full page.

Dense UIs (data-heavy dashboards) are valid, but density must be a deliberate choice, not the default.

## The spacing scale

Never nitpick between adjacent pixel values. Use a fixed scale built from a 16px base:

```
4, 8, 12, 16, 24, 32, 48, 64, 96, 128, 192, 256, 384, 512, 640, 768
```

Key property: adjacent values differ by ~25% or more. Small values sit close together (a 4px change to button padding is huge); large values spread out (a 20px change to a hero section is invisible). A naive "multiples of 4" rule fails because it still forces you to choose between 120 and 124.

To pick a value: guess, then compare against the neighbors above and below. The wrong ones are obvious side by side.

## Ambiguous spacing is a bug

When groups are separated only by whitespace (no borders/backgrounds), space *within* a group must be visibly smaller than space *around* it:

- Form labels must sit closer to their own input than to the field above.
- Section headings need more space above than below.
- List items need more space between items than between wrapped lines within an item.
- Horizontally grouped controls (e.g. icon + its label) must sit closer to each other than to neighboring groups.

If a user has to think about what belongs to what, the layout has failed — and it looks worse, too.

## Don't fill the screen

Wide canvas ≠ wide content. If content needs 600px, use 600px and let the margins breathe. Over-stretched interfaces are harder to read. Sections don't have to match each other's width either — a full-width nav doesn't obligate a full-width form.

- Struggling with a small component on a big canvas? Shrink the canvas. Designing mobile-first (~400px) forces good decisions that mostly survive the scale-up.
- Content too narrow for the page but shouldn't stretch? Split into columns (e.g. move a form's help text into a side column) instead of widening the form.
- Conversely, don't cram: if something genuinely needs width, take it.

## Grids are a tool, not a religion

Percentage-based grid columns are wrong for elements with content-driven sizes:

- **Sidebars:** fixed width sized to their content; let the main area flex.
- **Cards/modals/forms:** `max-width` at their optimal size; shrink only when the viewport forces it. A 50%-wide login card is too narrow on medium screens and too wide on huge ones — `max-width: 500px` is right everywhere.
- Within components: use percentages only for things that should actually scale.

## Relative sizing doesn't scale

Proportions that work at one size break at another:

- A 2.5× headline-to-body ratio on desktop becomes absurd on mobile; large text must shrink *faster* than small text. Define sizes per breakpoint instead of encoding ratios (`em`-based headlines).
- Within components: button padding should not be a fixed multiple of font size. Large buttons want disproportionately generous padding; small buttons want disproportionately tight padding. Fine-tune each size variant independently.
