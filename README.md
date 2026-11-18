# Outlier banners

Animated banner variants for the Outlier store (BigCommerce).

| # | Banner | Effect |
|---|--------|--------|
| 01 | [Red / blue glow](banners/01-smoke-glow/) | 16:9. The photo’s own blue and red light flickers chaotically across the background and on the suppressors, the smoke rolls closer and farther, and a low mist creeps across the floor. Colour and saturation stay within the original photo. No added colours. CSS only. |
| 02 | [Suppressors reveal](banners/02-sequence/) | 16:9, from photo 9645. A soft light edge sweeps from left to right and reveals the suppressors one after another; then they dim partly (not to full dark) and the same sweep starts again right away (6.4 s cycle, slower reveal, no pause). The camera zooms in a little with every reveal and holds while the scene dims, never zooming out (4 steps, then a quick reset in a moment of full dark). CSS only. |
| 03 | [Roll-in](banners/03-roll-in/) | 16:9 MP4 (13.4 s loop, 2.1 MB), from photo 9682. The suppressor from the photo itself rolls in from the far, dark end of the floor: 1 slow even turn over ~10.5 s (the body is unwrapped around its axis — rings, 8 flutes, 4 adapter recesses repeat, the single logo turns once per turn, the photo's light stays in place), grows and brightens, and stops exactly in the photo pose. |
| 04 | [Wet stone](banners/04-wet-stone/) | 16:9, from photo 9625. Glints on the wet stone shimmer in three zones the photo’s own specks of light on the wet stone twinkle like light on water (8 independent groups), the suppressors’ copper top highlight pulses in colour intensity and a richer glow passes down through it and back; otherwise the suppressors stay exactly as in the photo. No added shapes or area lighting. CSS only. |

## Using a banner in BigCommerce

1. Upload the banner's images (`bg.jpg` and the zone masks `b1–b3`, `r1–r3`, `ob`, `or` `.png`) to **Storefront → Image Manager** or WebDAV `/content/`.
2. Copy the `<style>` block and the markup between `BANNER START` and `BANNER END` into the banner's HTML.
3. Replace the image paths (`url(bg.jpg)` etc.) with the uploaded URLs and set the link in `href`.

## Viewing locally

```sh
python3 -m http.server 8790
```

Then open http://localhost:8790.
