# Outlier banners

Animated banner variants for the Outlier store (BigCommerce).

| # | Banner | Effect |
|---|--------|--------|
| 01 | [Red / blue glow](banners/01-smoke-glow/) | 16:9. The photo’s own blue and red light flickers chaotically across the background and on the suppressors, the smoke rolls closer and farther, and a low mist creeps across the floor. Colour and saturation stay within the original photo. No added colours. CSS only. |
| 02 | [Suppressors one by one](banners/02-sequence/) | 16:9, from photo 9645. The scene starts dark; the suppressors come out of the dark one after another with their reflections and a warm glint, hold, and the 10 s loop repeats. CSS only. |
| 03 | [Roll-in](banners/03-roll-in/) | 16:9 MP4 (8.4 s loop, 1.3 MB), from photo 9682 and the 3D model. The suppressor starts small and dark, grows as it rolls towards the viewer while its colour comes up, stops in the photo's pose and dissolves into the real photo. |

## Using a banner in BigCommerce

1. Upload the banner's images (`bg.jpg` and the zone masks `b1–b3`, `r1–r3`, `ob`, `or` `.png`) to **Storefront → Image Manager** or WebDAV `/content/`.
2. Copy the `<style>` block and the markup between `BANNER START` and `BANNER END` into the banner's HTML.
3. Replace the image paths (`url(bg.jpg)` etc.) with the uploaded URLs and set the link in `href`.

## Viewing locally

```sh
python3 -m http.server 8790
```

Then open http://localhost:8790.
