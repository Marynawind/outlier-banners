# Outlier banners

Animated banner variants for the Outlier store (BigCommerce).

| # | Banner | Effect |
|---|--------|--------|
| 01 | [Red / blue glow](banners/01-smoke-glow/) | 16:9. The photo’s own blue and red light flickers chaotically across the background and on the suppressors, the smoke rolls closer and farther, and a low mist creeps across the floor. Colour and saturation stay within the original photo. No added colours. CSS only. |
| 02 | [Suppressors reveal](banners/02-sequence/) | 16:9, from photo 9645. A soft light edge sweeps from left to right and reveals the suppressors one after another; then they dim partly (not to full dark) and the same sweep starts again right away (6.4 s cycle, slower reveal, no pause). The camera zooms in a little with every reveal and holds while the scene dims, never zooming out (4 steps, then a quick reset in a moment of full dark). CSS only. |
| 04 | [Wet stone](banners/04-wet-stone/) | 16:9, from photo 9625. Glints on the wet stone shimmer in three zones the photo’s own specks of light on the wet stone twinkle like light on water in a warm tint, the warm reflections on the stone glow in step with the suppressors, the suppressors’ copper top highlight pulses in colour intensity, a richer glint travels along it, and its lower edge keeps spreading down the body, then fades; otherwise the suppressors stay exactly as in the photo. No added shapes or area lighting. CSS only. |
| 05 | [Camera glide](banners/05-camera/) | 16:9, from photo 9623. A slow camera glides over the photo: flutes → logo → rings → up the standing suppressor → pull back to the whole scene → back in (22 s loop); the warm backlight breathes. No text. CSS only. |
| 06 | [Photo flyby](banners/06-photo-flyby/) | 16:9 MP4 from photo 9623, 60 fps, 1920×1080, 8.8 s loop. Three shots joined by a flash of light: (1) left to right along the lying suppressor, (2) bottom to top along the standing one, (3) pull-back to the whole photo while the warm light from behind slowly comes up and the shadow lifts. In shots 1–2 the scene is in shadow and a soft light beam travels with the camera. `flyby.mp4` + `poster.jpg`, `<video autoplay muted loop playsinline>`. |
| 07 | [Product ad](banners/07-product-ad/) | 16:9 MP4 1920×1080 (5.9 s loop), product-ad style with play of light in the black, neutral look of photo 9679: a light streak sweeps the body in the dark, backlight reveal, rotated logo close-up, side pass along the rings (3D model) — quick dips to black — then the real photo 9679 with a slow push-in and a light pass. The bore never faces the camera. |

## Using a banner in BigCommerce

1. Upload the banner's images (`bg.jpg` and the zone masks `b1–b3`, `r1–r3`, `ob`, `or` `.png`) to **Storefront → Image Manager** or WebDAV `/content/`.
2. Copy the `<style>` block and the markup between `BANNER START` and `BANNER END` into the banner's HTML.
3. Replace the image paths (`url(bg.jpg)` etc.) with the uploaded URLs and set the link in `href`.

## Viewing locally

```sh
python3 -m http.server 8790
```

Then open http://localhost:8790.
