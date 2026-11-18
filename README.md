# Outlier banners

Animated banner variants for the Outlier store (BigCommerce).

| # | Banner | Effect |
|---|--------|--------|
| 01 | [Red / blue glow](banners/01-smoke-glow/) | 16:9. The photo’s own blue and red light slowly and continuously brighten and dim in turn. No added colours. CSS only. |

## Using a banner in BigCommerce

1. Upload the banner's images (`bg.jpg`, `blue-mask.png`, `red-mask.png`) to **Storefront → Image Manager** or WebDAV `/content/`.
2. Copy the `<style>` block and the markup between `BANNER START` and `BANNER END` into the banner's HTML.
3. Replace the image paths (`url(bg.jpg)` etc.) with the uploaded URLs and set the link in `href`.

## Viewing locally

```sh
python3 -m http.server 8790
```

Then open http://localhost:8790.
