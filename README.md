# Outlier banners

Animated banner variants for the Outlier store (BigCommerce).

| # | Banner | Effect |
|---|--------|--------|
| 01 | [Red / blue glow](banners/01-smoke-glow/) | 16:9. The photo’s own blue and red light flickers chaotically across the background and on the suppressors, the smoke rolls closer and farther, and a low mist creeps across the floor. Colour and saturation stay within the original photo. No added colours. CSS only. |
| 02 | [Suppressors reveal](banners/02-sequence/) | 16:9, from photo 9645. A soft light edge sweeps from left to right and reveals the suppressors with their reflections, while the camera pans left to right and zooms in and out; 9 s loop with a short pause. CSS only. |
| 03 | [Roll-in](banners/03-roll-in/) | 16:9 MP4 (9.2 s loop, 1.6 MB), from photo 9682 and the 3D model (colour-matched to the photo). The suppressor rolls in from the far, dark end of the floor (~3.5 turns), grows and brightens, and stops in the photo pose. No dissolve. |

## Using a banner in BigCommerce

1. Upload the banner's images (`bg.jpg` and the zone masks `b1–b3`, `r1–r3`, `ob`, `or` `.png`) to **Storefront → Image Manager** or WebDAV `/content/`.
2. Copy the `<style>` block and the markup between `BANNER START` and `BANNER END` into the banner's HTML.
3. Replace the image paths (`url(bg.jpg)` etc.) with the uploaded URLs and set the link in `href`.

## Viewing locally

```sh
python3 -m http.server 8790
```

Then open http://localhost:8790.
