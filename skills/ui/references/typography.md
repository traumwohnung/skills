# Typography

## The type scale

Interfaces rot into a dozen arbitrary font sizes without a system. Use a hand-picked scale:

```
12, 14, 16, 18, 20, 24, 30, 36, 48, 60, 72
```

Why hand-picked instead of a modular ratio (4:5, golden ratio, etc.): ratio scales produce fractional pixels (rounding varies per browser) and leave gaps exactly where UI work needs sizes (between 12–16 and 16–21). Ratios suit long-form articles; interfaces need the denser small end.

**Units:** px or rem only. Never `em` for the scale — nested em values compound, so computed sizes silently drift off-scale.

## Choosing typefaces

- **Safe default:** a neutral sans-serif, or the system font stack (`-apple-system, Segoe UI, Roboto, Noto Sans, Ubuntu, Cantarell, Helvetica Neue`).
- **Quality filter:** prefer families with 5+ weights (10+ styles counting italics) — breadth of weights correlates with craftsmanship. Font directories let you filter by style count.
- **Legibility filter:** body/UI text wants a generous x-height and normal-to-wide letter-spacing. Avoid condensed, short-x-height display faces for anything small.
- **Popularity is signal:** widely-used fonts are usually good fonts; sorting by popularity is a legitimate shortcut, especially for personality faces (serifs, display).
- **Steal taste:** inspect what well-designed sites use.

## Line length

45–75 characters per line for comfortable reading; in CSS, roughly `max-width: 20–35em` on paragraphs. When a content area is wider (to fit images or other components), still cap paragraph width — mixed widths in one column look more polished, not less.

## Line height

Two proportionalities:

- **Line length ↑ → line height ↑.** Narrow columns read fine at ~1.5; wide text blocks may need up to 2 so eyes can find the next line.
- **Font size ↑ → line height ↓.** Small text needs extra leading; large headlines need almost none — line-height 1 is fine at display sizes.

Never treat 1.5 as a universal constant.

## Alignment

- Left-align by default (for LTR languages). Center only headlines or blocks of 2–3 lines max — if a centered block runs long, shorten the copy or left-align it.
- **Right-align numbers in tables** so decimal points line up for comparison.
- If you justify text, enable hyphenation, or rivers of whitespace appear. Justification is a print-flavored stylistic choice; left-aligned is always safe.

## Baseline alignment

When mixing font sizes on one line (card title + small action link), align to the shared **baseline**, not vertical centers. Centering mismatched sizes offsets their baselines and looks subtly sloppy; baselines are the alignment reference the eye actually uses.

## Letter-spacing

Leave it alone by default — the type designer already optimized it. Two exceptions:

- **Headlines:** slightly negative tracking gives a legible-at-small-sizes family the tighter look of a display face. (The reverse — tracking out a display face for body use — doesn't work.)
- **All-caps:** increase letter-spacing. Uniform-height capitals lose the distinguishing ascender/descender shapes, and extra tracking restores scannability.

## Links

In link-dense UIs, the loud blue-underline treatment overwhelms. Emphasize most in-app links with just weight or a darker color; truly ancillary links can stay plain and reveal affordance (color/underline) on hover only. Reserve high-visibility link styling for links embedded in prose.
