# Depth

## One rule: light comes from above

Raised vs. inset is entirely about mimicking an overhead light source. Users view screens looking slightly downward, so:

**Raised element** (e.g. a button):
- Lighten the top edge — a light top border or an inset shadow with a small positive y-offset. Hand-pick the lighter color; overlaying semi-transparent white drains saturation.
- Cast a small, dark, sharp shadow below (small y-offset, blur of only a couple px). The element blocks light from reaching the surface under it.

**Inset element** (e.g. a well, text input, checkbox):
- Lighten the bottom lip (light bottom border or inset shadow with negative y-offset) — it faces up.
- Dark inset shadow at the top (small positive y-offset) — the surrounding surface shades the top of the recess.

Use these cues sparingly; chasing photo-realism produces busy, unclear interfaces.

## Shadows as elevation

Shadow size maps to z-position, and z-position maps to attention: the closer to the user, the more focus it draws.

- **Small/tight:** buttons, cards — noticeable, not dominant.
- **Medium:** dropdowns, popovers.
- **Large/soft:** modals — maximum separation from the page.

Define a fixed 5-step scale and stop improvising:

```
0 1px 3px rgba(0,0,0,.2)
0 4px 6px rgba(0,0,0,.2)
0 5px 15px rgba(0,0,0,.2)
0 10px 24px rgba(0,0,0,.2)
0 15px 35px rgba(0,0,0,.2)
```

Choose by asking "where does this sit on the z-axis?", never "which shadow looks nice?".

**Interaction cues:** raise an item's elevation while it's being dragged (it pops above its siblings); shrink or remove a button's shadow on `:active` so it feels pressed into the page.

## Two-part shadows

Refined shadows combine two layers with distinct jobs:

1. **Ambient/cast shadow:** larger y-offset, big blur, subtle — the shadow thrown by a direct light source.
2. **Contact shadow:** small y-offset, tight blur, darker — the dark crease directly under an object where ambient light can't reach.

This gives independent control: soft overall presence, crisp definition at the edges. As elevation increases, fade the contact shadow — objects far from a surface lose that tight dark edge; at the top elevation it can disappear entirely.

## Depth without shadows (flat design)

- **Color:** lighter than the surrounding background reads as raised; darker reads as recessed. Works in any style.
- **Solid shadows:** a short, vertically offset, zero-blur shadow adds lift while staying flat-aesthetic.

## Overlap creates layers

Overlapping elements is the strongest depth cue of all:

- Offset a card across a background-color transition.
- Make an element taller than its parent so it breaks out on both edges.
- Float controls (carousel arrows) half-over their content.
- Overlapping avatars/images: give each an "invisible border" matching the page background so they read as stacked, not colliding.
