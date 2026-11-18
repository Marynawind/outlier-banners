# Outlier banners

Animated banner variants for the Outlier store (BigCommerce).

| # | Banner | Effect |
|---|--------|--------|
| 01 | [Red / blue glow](banners/01-smoke-glow/) | 16:9. The photo’s own blue and red light flickers chaotically across the background and on the suppressors, the smoke rolls closer and farther, and a low mist creeps across the floor. Colour and saturation stay within the original photo. No added colours. CSS only. |
| 02 | [Suppressors reveal](banners/02-sequence/) | 16:9, from photo 9645. A soft light edge sweeps from left to right and reveals the suppressors one after another; then they dim partly (not to full dark) and the same sweep starts again right away (4.6 s cycle, no pause). Calm product-ad camera: slow dolly in with a gentle drift across and back out (18 s loop). CSS only. |
| 03 | [Roll-in](banners/03-roll-in/) | 16:9 MP4 (13.4 s loop, 2.1 MB), from photo 9682. The suppressor from the photo itself rolls in from the far, dark end of the floor: 1 slow even turn over ~10.5 s (the body is unwrapped around its axis — rings, 8 flutes, 4 adapter recesses repeat, the single logo turns once per turn, the photo's light stays in place), grows and brightens, and stops exactly in the photo pose. |

## Using a banner in BigCommerce

1. Upload the banner's images (`bg.jpg` and the zone masks `b1–b3`, `r1–r3`, `ob`, `or` `.png`) to **Storefront → Image Manager** or WebDAV `/content/`.
2. Copy the `<style>` block and the markup between `BANNER START` and `BANNER END` into the banner's HTML.
3. Replace the image paths (`url(bg.jpg)` etc.) with the uploaded URLs and set the link in `href`.

## Viewing locally

```sh
python3 -m http.server 8790
```

Then open http://localhost:8790.
