# Typography

## The type scale

Without a system, interfaces accumulate every size from 10px to 24px — inconsistent and slow to work with. Use a hand-picked scale:

```
12, 14, 16, 18, 20, 24, 30, 36, 48, 60, 72
```

**Why hand-picked, not ratio-generated.** Modular scales (a base times a repeated ratio like 4:5, 2:3, or the golden ratio) look mathematically satisfying but fail for UI work in two ways:

1. **Fractional pixels.** A 16px base with a 4:5 ratio yields values like 31.25 and 39.06; browsers round subpixels inconsistently, causing off-by-one artifacts. If you insist on a ratio, at least round every value yourself when defining the scale.
2. **Wrong gaps.** Interface work needs the small end dense — you *will* want sizes between 12 and 16 and between 16 and 21, which typical ratios skip. Tightening the ratio until the gaps close is just hand-picking with extra steps. Ratio scales suit long-form editorial content; interfaces need direct control.

**Units: px or rem, never em.** Em is relative to the *current* font size, so nesting compounds: inside a 1.25em (20px) element, a 0.875em child computes to 17.5px — a value that exists nowhere in your scale. Px and rem are the only units that guarantee the system holds.

## Choosing typefaces

- **Safe default:** a neutral sans-serif, or simply the system font stack (`-apple-system, Segoe UI, Roboto, Noto Sans, Ubuntu, Cantarell, Helvetica Neue`) — unadventurous, but familiar to every user.
- **Weight-count filter:** prefer families offering 5+ weights (10+ styles counting italics). It's an imperfect proxy, but families with many weights tend to be crafted with more care. Font directories can filter by style count — on a large library this one filter eliminates the vast majority of weak options.
- **Legibility filter:** families are designed for a purpose. Headline faces run tight letter-spacing and short x-heights; text faces run open spacing and tall lowercase letters. For UI text, avoid condensed short-x-height faces — they fall apart at small sizes.
- **Popularity is signal:** a widely-used font is rarely a bad font. Sorting a directory by popularity is a legitimate shortcut, especially when picking a personality face (a serif, a display font) where judging quality is harder.
- **Steal taste:** inspect the font choices of sites whose design you admire — strong design teams have already done the vetting, and they surface options no safe heuristic finds.

Intuition builds fast once you start paying attention; the heuristics are scaffolding, not a permanent crutch.

## Line length

45–75 characters per line is the readable range; in CSS, `max-width` of roughly 20–35em lands there. Two traps:

- Sizing paragraphs to the layout instead of to reading comfort — the usual result is lines far too long.
- Widening paragraphs to match wider siblings. When text mixes with images or wide components, cap the paragraph width anyway; mixed widths inside one content column look more polished, not less.

Slightly past 75 characters can survive, but it's risky territory.

## Line height

Line spacing exists so the eye can find the next line after the return sweep — read the same line twice, or skip one, and the leading was too small. Two proportional relationships govern it:

- **Line length ↑ → line height ↑.** The longer the horizontal jump back, the easier it is to get lost. Narrow columns read fine at ~1.5; wide blocks may need up to 2.
- **Font size ↑ → line height ↓** (inverse). Small text needs generous leading; large display text needs none — line-height 1 is fine for headlines.

Treating 1.5 as a universal constant is the common mistake; it's only the midpoint of a range.

## Alignment

- **Left-align by default** — text alignment should match its language's reading direction, and centering fights it.
- **Center only short text:** headlines and independent blocks of 2–3 lines. If one block in a centered set runs long, the best fix is usually editing the copy shorter — solves the alignment and tightens the message.
- **Right-align numbers in tables** so decimals line up vertically and magnitudes compare at a glance.
- **Justify only with hyphenation on**, or gaps open up between words. Justification is a print-flavored look for formal contexts; left-aligned is never wrong.

## Baseline, not center

When mixing font sizes on one line — a card title beside a small action link — align them by their shared **baseline**, not by vertical centers. Center-aligning offsets the baselines, which looks subtly wrong, and obviously wrong once the sizes sit close together. The baseline is the alignment reference the eye already uses; matching it produces the clean version for free.

## Letter-spacing

Default stance: leave it alone — the type designer tuned it for the face's intended size. Two justified interventions:

- **Tighten headlines.** A text face used at display sizes carries its small-size letter-spacing up with it; slightly negative tracking recovers the condensed look of a purpose-built headline face. The reverse fails — display faces don't become readable at small sizes by tracking out.
- **Open up all-caps.** Default spacing is tuned for sentence case, where ascenders and descenders differentiate letterforms. Uniform-height capitals lose those cues, so extra tracking restores scannability for labels and small caps headers.

## Links

The loud treatment (bright color + underline) exists to make a link stand out inside prose. In interfaces where most things are clickable, it turns the page into noise:

- Emphasize most in-app links subtly — heavier weight or a darker shade of the text color.
- Truly ancillary links can look like plain text, revealing color or underline on hover; discoverable without competing against primary actions.
- Reserve the full prose treatment for actual links-in-paragraphs.
