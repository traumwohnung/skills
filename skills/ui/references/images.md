# Images

## Photo quality is non-negotiable

A bad photo ruins a design even when everything around it is right. Great photography is lighting, composition, and color grading — skills, not equipment — so the options are:

1. **Hire a professional** when the project needs specific, on-brand imagery.
2. **Use high-quality stock** for generic needs; excellent free libraries exist alongside paid ones.

Never design around placeholder images planning to "swap in some phone photos later" — the swap always downgrades the design, and by then the layout depends on imagery you can't produce.

## Text over images

The headline-on-hero-image problem: photos contain both bright and dark regions, so white text drowns in the light areas and dark text drowns in the shadows. No text color fixes this, because the problem is the image's dynamic range, not the text. Reduce the range:

- **Overlay:** a semi-transparent black layer tames highlights so white text works; a white layer lifts shadows for dark text. Simple, but it lightens/darkens the whole image.
- **Lower the image's contrast** for finer control, compensating with a brightness adjustment so the image doesn't shift overall tone.
- **Colorize:** lower contrast, desaturate, then apply a solid brand color with a multiply blend. Kills the dynamics *and* makes any stock photo harmonize with the palette.
- **Text shadow:** a soft glow — large blur, no offset — adds contrast exactly where the text sits, letting you preserve more of the image's character. Best combined with a milder contrast reduction.

## Everything has an intended size

Scaling artwork away from the size it was drawn for degrades it — in both directions, and vector formats don't grant immunity:

- **Icons up:** a 16–24px icon enlarged 3–4× stays sharp as SVG but looks chunky and undetailed — it was drawn with the detail budget of a small size. To fill a large slot (feature sections, landing pages), keep the icon near its native size and enclose it in a colored shape (circle, rounded square). The shape fills the space; the icon keeps its proportions.
- **Icons down:** detail designed for larger sizes turns to mush when shrunk. The extreme case is the favicon: never shrink a full logo to 16px — redraw a radically simplified mark at the target size so you control what survives, not the browser's resampler.
- **Screenshots down:** a full-desktop screenshot shrunk ~70% to fit a marketing layout renders 16px UI text at ~4px — unreadable and squint-inducing. Alternatives: capture at a smaller viewport (the tablet layout) and give it generous space; crop to a partial screenshot shown at full size; or, when only the gestalt matters, draw a simplified mock with lines standing in for text so nobody is tempted to read it.

## User-uploaded content

You can't art-direct uploads — no cropping, color-correcting, or contrast-tuning in advance — so build the defenses into the layout:

- **Control shape and size:** render images into fixed containers, centered and cropped (`object-fit: cover` / `background-size: cover`). Letting intrinsic aspect ratios through wrecks any multi-image layout.
- **Prevent background bleed:** an upload whose background matches your UI background loses its silhouette and melts into the page. Don't reach for a border — borders clash with the image's own colors. Use a subtle **inner** box shadow, which reads as a boundary without competing; a semi-transparent inner border is a good alternative if the slight inset look bothers you.
