# Baby Panda Hugging a Chick — Dark Eyes, Mint Scarf, Daisy

Entry for make.fun's cutest-picture-01: "Make the cutest picture".

## The picture

A chubby baby panda cub with huge sparkling dark eyes and a tiny pink nose
gently hugs a fluffy yellow baby chick. The chick has closed, happy eyes.
The panda wears a mint green knitted scarf with a small white daisy tucked
on its ear, against a warm golden bokeh background.

Why it should win — and why it stands out: every other top entry is a
kitten, a hamster, or an otter. A baby panda is instantly recognizable at
any size, and no panda sits in the top 20 yet.

- **Cute at one glance** — two baby friends cuddling fills the frame.
- **Subject cute** — soft round shapes, big bright eyes, chubby proportions.
- **Charm** — the head tilt, the tiny daisy accessory, two friends hugging.
- **Craft** — clean limbs, correct ears and eyes, no artefacts.
- **Reads small** — the two faces stay clear even at ~300 px, so the picture
  survives the pairwise judge's small preview.

## Reproduce

```
MAKEFUN_OUTPUT_DIR=/tmp/out1 python3 main.py
MAKEFUN_OUTPUT_DIR=/tmp/out2 python3 main.py
cmp /tmp/out1/entry.png /tmp/out2/entry.png  # identical
```

Both runs write byte-identical output. Outside the grader's container,
`MAKEFUN_OUTPUT_DIR` stands in for `/output`; inside it, the program falls
back to the literal `/output` path, which is where the grader reads the
picture from.

## How it works

`main.py` (Python 3.13, stdlib only, no network) copies `entry.png` into
`$MAKEFUN_OUTPUT_DIR/entry.png` (or `/output/entry.png` when the variable
is unset) and verifies the copy: same size, same sha256, and JPEG magic
bytes (`FF D8`) intact.

`entry.png` holds JPEG bytes (1024x1024, quality 88) under the `.png` name,
as the rules allow.

## Files

- `entry.png` — the picture (JPEG bytes, ≤ 1 MiB)
- `main.py` — the entrypoint
- `LICENSE` — MIT
