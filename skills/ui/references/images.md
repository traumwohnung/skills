# Images

## Photo quality is non-negotiable

A bad photo sinks an otherwise good design. Either hire a professional or use high-quality stock (free sources exist). Never build around placeholders expecting to swap in casual phone photos later — it never holds up.

## Text over images

Photos have bright and dark regions, so no single text color survives across them. Fixes (combinable):

- **Overlay:** semi-transparent black layer for white text, white layer for dark text.
- **Lower the image contrast** (adjust brightness to compensate) — flattens the dynamic range so text contrast stays consistent.
- **Colorize:** lower contrast, desaturate, then apply a solid brand color with multiply blend. Also harmonizes arbitrary photos with the palette.
- **Text shadow:** a wide-blur, zero-offset "glow" adds contrast exactly where the text is, letting you preserve more of the image's dynamics.

## Everything has an intended size

- **Don't scale icons up.** A 16–24px icon blown to 3–4× looks chunky and undetailed even as SVG. Need to fill a large slot? Keep the icon near its intended size inside a colored shape (circle/square).
- **Don't scale icons down** either — detail turns to mush. Favicons and other tiny marks need a redrawn, simplified version at target size.
- **Don't shrink full screenshots.** A 70%-scaled app screenshot renders body text at ~4px. Options: screenshot at a smaller viewport (tablet layout), crop to a partial screenshot, or draw a simplified mock (blocks instead of text) when the big picture is all that matters.

## User-uploaded content

You can't art-direct what users upload, so defend the layout:

- **Fix shape and size:** render into fixed containers with center-crop (`object-fit: cover` or background-size cover). Never let intrinsic aspect ratios dictate layout.
- **Prevent background bleed:** when an uploaded image's background nearly matches the UI background, its silhouette dissolves. A subtle *inner* box shadow keeps the boundary visible — outer borders clash with image colors. A semi-transparent inner border works too.
