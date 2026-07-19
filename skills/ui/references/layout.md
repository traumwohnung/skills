# Layout & Spacing

## White space: start with too much

The standard workflow adds space only when something looks cramped — which yields the bare minimum of breathing room everywhere, a design that merely avoids looking bad. Invert it: give elements clearly too much space, then pull space out until you're satisfied. What feels excessive zoomed into one element usually reads as "just enough" in the context of the full page.

Dense layouts (data-heavy dashboards where everything must fit one screen) are legitimate — but density must be a deliberate trade, never the default you drifted into. It's much easier to notice "too much space" and remove it than to notice "slightly too little" and add it.

## The spacing scale

Never deliberate between adjacent pixel values. Use a fixed scale built on a 16px base (also the browser default font size, and cleanly divisible):

```
4, 8, 12, 16, 24, 32, 48, 64, 96, 128, 192, 256, 384, 512, 640, 768
```

The defining property: adjacent values differ by at least ~25%, with the small end packed and the large end spread out. This is what "multiples of 4" misses: a 4px difference is enormous in button padding (12→16px is a 33% jump) and invisible in a card width (500→520px is 4%). Relative difference is what the eye perceives, so the scale must be relative too.

To pick a value: guess, then set the neighboring values beside it for comparison. Two of the three are usually obviously wrong; if an outer one wins, re-center on it and compare again.

## Ambiguous spacing is a bug

When groups are separated only by whitespace — no borders or background changes — the space *within* a group must be visibly smaller than the space *around* it. Violations force users to work out the grouping, and occasionally to get it wrong:

- A form label equidistant from its own input and the previous field visually belongs to neither — worst case, data lands in the wrong field.
- Section headings need clearly more space above than below, or they float between sections.
- List items whose gaps match the internal line-height read as one run-on blob.
- Horizontal arrangements have the same failure: an icon must sit closer to its own label than to the neighboring group.

Interfaces that are hard to parse always look worse, independent of styling.

## Don't fill the screen

A wide canvas is not an obligation. If the content needs 600px, use 600px — spreading content to fill 1200–1400px actively hurts comprehension, while margin never hurt anything. This holds per-section too: a full-width nav doesn't require the form below it to be full-width. Give each element the width its content wants, and don't degrade one element to make it match another.

- **Hard to design small on a big canvas? Shrink the canvas.** Design at ~400px first; real constraints make the decisions easier. Then port to desktop and fix only what felt like a compromise — usually less than expected.
- **Content too narrow for the page but shouldn't stretch? Split into columns.** A narrow form that looks unbalanced on a wide page keeps its optimal width when its supporting text moves into a side column — balance without sacrificing usability.
- **Don't force compactness either.** Needing lots of space is fine; cramming to no purpose is the same mistake mirrored.

## Grids are a tool, not a religion

A percentage grid outsources sizing decisions that some elements shouldn't delegate:

- **Sidebars:** a 25%-wide sidebar grows with the viewport, stealing width the content could use, and collapses below its minimum on small screens. Give it a fixed width sized to its contents and let the main area flex.
- **Cards, modals, forms:** fluid columns produce a paradox — a 6-column login card can be *narrower on a large screen* than an 8-column one on a medium screen. If 500px is the optimal width, nothing is gained by ever shrinking below it while space exists. Use `max-width` at the optimal size and let it compress only when the viewport truly forces it.
- **Inside components:** use percentages only for parts that should genuinely scale with their container.

## Relative sizing doesn't scale

Encoded proportions assume relationships stay constant across sizes; they don't:

- A headline at 2.5× body size works on desktop, but on mobile — body at 14px — 2.5em means a 35px headline, far too big. The right mobile headline (20–24px) is only ~1.5× body. Large elements must shrink *faster* than small ones, so the "relationship" was never real. Define sizes per breakpoint instead of encoding ratios.
- The same applies within components: if button padding is a multiple of font size, scaled variants merely look zoomed. Good large buttons carry disproportionately generous padding; good small buttons, disproportionately tight. Fine-tune each variant's properties independently.
