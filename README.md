# Outlier banners

Animated banner variants for the Outlier store (BigCommerce).

| # | Banner | Effect |
|---|--------|--------|
| 01 | [Red / blue glow](banners/01-smoke-glow/) | 16:9. The photo’s own blue and red light flickers chaotically across the background and on the suppressors, the smoke rolls closer and farther, and a low mist creeps across the floor. Colour and saturation stay within the original photo. No added colours. CSS only. |
| 02 | [Suppressors reveal](banners/02-sequence/) | 16:9, from photo 9645. A soft light edge sweeps from left to right and reveals the suppressors one after another; then they dim partly (not to full dark) and the same sweep starts again right away (6.4 s cycle, slower reveal, no pause). The camera zooms in a little with every reveal and holds while the scene dims, never zooming out (4 steps, then a quick reset in a moment of full dark). CSS only. |
| 04 | [Wet stone](banners/04-wet-stone/) | 16:9, from photo 9625. Glints on the wet stone shimmer in three zones the photo’s own specks of light on the wet stone twinkle like light on water in a warm tint, the warm reflections on the stone glow in step with the suppressors, the suppressors’ copper top highlight pulses in colour intensity, a richer glint travels along it, and its lower edge keeps spreading down the body, then fades; otherwise the suppressors stay exactly as in the photo. No added shapes or area lighting. CSS only. |
| 06 | [Photo flyby](banners/06-photo-flyby/) | 16:9 MP4 from photo 9623, 60 fps, 1920×1080, 9.7 s loop. Three shots joined by a soft dip to dark: (1) left to right along the lying suppressor, (2) bottom to top along the standing one, (3) pull-back to the whole photo while the warm light from behind slowly comes up and the shadow lifts. In shots 1–2 the scene is in shadow and a soft light beam travels with the camera. `flyby.mp4` + `poster.jpg`, `<video autoplay muted loop playsinline>`. |
| 07 | [Product ad](banners/07-product-ad/) | 16:9 MP4, 1920×1080, 23 fps, 11 s: a 3D product film of the 6" suppressor; in every shot the product has the same satin black finish with lighter matte flutes, white logo and mirror reflection. (1) A thin line of light runs along the body in the dark. (2) The backlight comes on and the camera slowly moves towards the logo. (3) A close-up of the logo turned on its side, with a light passing over it. (4) A highlight slides across the back end face (the bore never faces the camera). (5) Photo 9646 with a push-in and a light band on the suppressor; in the video its suppressor is graded neutral and smoothed to match the 3D model (the photo file itself is unchanged). `ad.mp4` + `poster.jpg`, `<video autoplay muted loop playsinline>`. |

## Using a banner in BigCommerce

1. Upload the banner's images (`bg.jpg` and the zone masks `b1–b3`, `r1–r3`, `ob`, `or` `.png`) to **Storefront → Image Manager** or WebDAV `/content/`.
2. Copy the `<style>` block and the markup between `BANNER START` and `BANNER END` into the banner's HTML.
3. Replace the image paths (`url(bg.jpg)` etc.) with the uploaded URLs and set the link in `href`.

## Viewing locally

```sh
python3 -m http.server 8790
```

Then open http://localhost:8790.

## Site slides

| Slide | Files |
|---|---|
| [Upgrade your setup with a suppressor](site/upgrade-suppressor/) | `upgrade-suppressor-1920x1080.jpg` replaces `Why_Buy_From_Us.jpg` in slide 2 of the Home Page Carousel on backdraftsuppressors.com. Heading: *Upgrade your setup with a suppressor*, button: *Shop Now*. Built from photo 9666: the scene is at 75% on the right so the theme's text box on the left never covers the suppressors; the wall, smoke and the dark space under the table continue around it. Previews: `preview-desktop.jpg`, `preview-phone.jpg`, `mockup-site-desktop.png` and `mockup-site-phone.png` (the slide inside screenshots of the live home page). |

## GetOutlier landing → Backdraft (getoutlier.com/hush)

[Preview](site/getoutlier-landing/) — banner 02 animation with a Shop Now button. A click anywhere, or 7 seconds without a click, takes the visitor to https://backdraftsuppressors.com/suppressors/. Paste `site/getoutlier-landing/snippet.html` into an Ecwid Instant Site "Custom code" section on a page with the URL `hush`.

## Banner photos

Final retouched photos for static banners, full quality, in [`photos/`](photos/):

| Photo | Scene | Size |
|---|---|---|
| [IMG_9666](photos/IMG_9666.jpg) | three suppressors, glowing logo on the wall, smoke | 3162×1344 |
| [IMG_9644](photos/IMG_9644.jpg) | three suppressors, glowing logo on a concrete wall | 2752×1536 |
| [IMG_9679](photos/IMG_9679.jpg) | two suppressors on black with reflections | 2752×1536 |
| [IMG_9623](photos/IMG_9623.jpg) | lying and standing suppressor, warm backlight | 2752×1536 |
