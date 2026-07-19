# Process

How to approach a design from a blank canvas. Getting the process right prevents most downstream styling problems.

## Start with a feature, not the shell

"Designing the app" usually means agonizing over chrome: top nav or sidebar, container or full-width, where the logo goes. That's backwards — an app is a collection of features, and until several features exist you lack the information to make shell decisions. That's why starting there feels stuck and frustrating.

Instead pick one concrete piece of functionality and design only it. For a flight-booking product, that's the search interaction: origin field, destination field, two date fields, a search button. Design that. Navigation, headers, and page framing can come once real content exists to organize — and sometimes you'll discover you barely need them.

## Detail comes later

In the earliest phase, decisions about typefaces, shadows, and icons are a distraction.

- **Work low-fidelity.** Paper and a thick marker is a genuinely good medium precisely because it makes detail-obsessing impossible — you can only explore layout ideas, fast.
- **Hold the color.** Even in high fidelity, design in grayscale first. Forced to express hierarchy through spacing, contrast, and size alone, you end up with a clearer interface that color then enhances rather than rescues.
- **Don't over-invest in mockups.** Wireframes are disposable thinking tools. Users can't do anything with a static picture — decide, build, and throw the sketch away.

## Work in short cycles

Don't design every screen up front. Imagining every edge case in the abstract (2000 contacts, two events at the same time, where errors appear in this form) is much harder than fixing problems in a working interface.

1. Design a simple version of the next feature.
2. Build it for real.
3. Iterate on the working version until the problems are gone.
4. Return to design mode for the next feature.

Real usage does the heavy lifting your imagination would otherwise have to do.

## Be a pessimist

Expect every feature to be harder to build than it looks, and never imply functionality you aren't ready to ship. If a comment box design includes an attachments area, attachments become a blocker — and a comment system without attachments would still have been worth shipping. Design the smallest useful version first; add nice-to-haves as separate, later designs. That way there is always something shippable.

## Choose a personality deliberately

Every interface projects a personality — a bank wants secure and professional, a social app wants fun. This sounds fuzzy but it's set by four concrete levers:

- **Typeface:** serif = elegant/classic; rounded sans = playful; neutral sans = plain, letting other elements speak.
- **Color:** blue = safe and familiar; gold = expensive, sophisticated; pink = fun, unserious. Psychology matters less than how the color feels — but it helps explain why a choice fits.
- **Border radius:** none = formal; small = neutral; large = friendly. Whatever you pick, never mix square and rounded corners in one UI.
- **Language:** formal, distant copy reads professional; casual copy reads friendly. Words are everywhere in a UI — tone is as much a design decision as color.

Not sure which personality? Look at the sites your target users already use and match their register — without imitating direct competitors closely enough to look like a knock-off.

## Limit your choices

Unlimited options make every minor decision torture: 12px or 13px, 10% or 15% shadow opacity, medium or semibold. When several options are all defensible, confident decisions become impossible.

**Define systems in advance** so the hard choice is made once, not on every element:

- font size, font weight, line height
- color
- margin, padding
- width, height
- box shadows, border radius, border width, opacity

**Decide by elimination.** With a constrained scale, picking a value is fast: guess (say 16px for an icon), then compare against the neighbors (12px and 24px). Usually two of the three are obviously wrong. If an outer value wins, repeat with it as the new middle until the neighbors are clearly worse.

You don't need every system on day one — approach design with a system-building mindset, and whenever you catch yourself re-making the same low-level decision, turn it into a scale.
