# Depth

## One rule: light comes from above

Everything about raised vs. inset elements follows from a single physical fact: interfaces simulate an overhead light source. Surfaces angled toward the light get lighter; surfaces angled away, or shaded by an overhang, get darker. Real-world door panels read as raised purely because their top bevel is lit and their bottom bevel is shadowed; cabinet insets read as recessed because the top of the recess is shadowed by the lip above and the bottom lip catches light. Reproduce those cues and the brain infers the geometry automatically.

Users also view screens looking slightly downward — so of a raised element's two flat edges (top and bottom), only the top should be visible; of an inset's edges, only the bottom lip.

**Raised element** (e.g. a button):
- Lighten the top edge: a lighter top border, or an inset shadow with a small positive y-offset. Hand-pick the lighter color rather than overlaying translucent white — white overlays drain the saturation out of the underlying color.
- Add a small dark drop shadow with a slight downward offset — the element blocks light from the surface beneath it. Keep the blur tight (a couple of px): real contact shadows, like the one under a wall outlet or window sill, have sharp edges.

**Inset element** (e.g. a well, text input, checkbox):
- Lighten the bottom lip: light bottom border, or inset shadow with a small negative y-offset — that lip faces the light.
- Dark inset shadow at the top with a small positive y-offset — the surrounding surface shades the top of the recess. Size it so it doesn't leak out at the bottom.

Use these cues in moderation. Simulating light is a rabbit hole; chasing photo-realism produces busy, unclear interfaces. Borrow just enough physics to signal the geometry.

## Shadows as elevation

Shadow size positions an element on a virtual z-axis, and z-position maps directly to attention: the closer something floats to the user, the more focus it demands.

- **Small, tight shadows:** buttons and cards — slightly lifted, noticeable without dominating.
- **Medium shadows:** dropdowns and popovers — clearly above the page.
- **Large, soft shadows:** modal dialogs — closest to the user, demanding full attention.

Define a fixed elevation scale instead of improvising per element. Five steps covers virtually everything: set the smallest and largest first, then fill the middle with roughly linear growth:

```
0 1px 3px rgba(0,0,0,.2)
0 4px 6px rgba(0,0,0,.2)
0 5px 15px rgba(0,0,0,.2)
0 10px 24px rgba(0,0,0,.2)
0 15px 35px rgba(0,0,0,.2)
```

Choose by asking "where should this sit on the z-axis?", never "which shadow looks nice?" — that reframing makes the decision near-automatic.

**Interaction cues.** Elevation changes communicate state:
- Raise an item's shadow when the user grabs it in a sortable list — it visibly pops above its siblings and signals draggability.
- Shrink or remove a button's shadow on `:active` so it feels physically pressed into the page.

## Two-part shadows

Polished shadows are usually two shadows doing two different jobs:

1. **Cast shadow:** larger vertical offset, generous blur, relatively subtle — the diffuse shadow a direct light source throws behind an object.
2. **Contact shadow:** small offset, tight blur, darker — the dark crease directly beneath an object where even ambient light can't reach.

Splitting them gives independent control: the overall presence stays soft while the element's lower edge stays crisply defined — impossible to achieve with one shadow.

Elevation interacts with the contact shadow: lift an object off a surface and the tight dark crease fades (verifiably true of any object on a desk). So on the elevation scale, the contact shadow should be distinct at the lowest step and nearly or fully gone at the highest.

## Depth without shadows (flat design)

Flat aesthetics reject blur and gradients, not depth itself:

- **Color:** among related shades, lighter reads as closer and darker as further away. Lighter-than-background = raised card; darker-than-background = inset well. (This lever works in non-flat designs too.)
- **Solid shadows:** a short, vertically offset, zero-blur shadow lifts a card or button while keeping the crisp flat look.

## Overlap creates layers

Overlap is the strongest depth cue available — it makes a design read as physically layered:

- Offset a card so it straddles the boundary between two background colors.
- Make an element taller than its parent so it breaks out of both edges.
- Float controls (e.g. carousel arrows) half-on, half-off their content.
- Overlapping avatars or images clash easily; give each an "invisible border" in the page background color so a clean gap separates the layers.
