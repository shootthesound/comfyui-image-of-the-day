<h1 align="center">Image of the Day for ComfyUI</h1>

<p align="center">
  Fetch a fresh image straight into your workflow from 8 daily / random sources.<br>
  Useful for prompt testing, style references, daily-image automations, or just kicking off a workflow with something interesting.
</p>

<p align="center">
  <a href="https://buymeacoffee.com/lorasandlenses"><img src="https://img.shields.io/badge/Buy%20me%20a%20coffee-FFDD00?style=for-the-badge&logo=buy-me-a-coffee&logoColor=black" alt="Buy Me A Coffee"></a>
</p>

---

## Sources

| Source | API key needed? | Notes |
|---|---|---|
| **Lorem Picsum** | No | Random photo at any size — use `width` / `height` inputs |
| **Bing Daily** | No | Microsoft Bing's daily wallpaper (with metadata) |
| **Wikimedia POTD** | No | Wikimedia Commons "Picture of the Day" |
| **Random Dog** | No | Random dog photo (Stanford Dogs Dataset via dog.ceo) |
| **Random Cat** | No | Random cat photo (TheCatAPI) |
| **NASA APOD** | Yes (free) | NASA Astronomy Picture of the Day. Free key at [api.nasa.gov](https://api.nasa.gov) |
| **Unsplash** | Yes (free) | Random Unsplash photo. Free key at [unsplash.com/developers](https://unsplash.com/developers) |
| **Pexels** | Yes (free) | Random Pexels photo. Free key at [pexels.com/api](https://www.pexels.com/api/) |

API keys are saved automatically the first time you use them — you don't have to re-enter on each workflow load. They're stored locally in a `.image_of_day_config.json` next to the node file (and gitignored, so you can't accidentally commit one to a fork).

## Outputs

| Output | Type | Description |
|---|---|---|
| `image` | IMAGE | The fetched image (RGB) |
| `title` | STRING | Image title (where the source provides one) |
| `description` | STRING | Image description / caption |
| `source_url` | STRING | URL of the source page |
| `copyright` | STRING | Attribution / copyright string |

The four metadata strings are useful for overlaying source attribution onto the output image, building daily-archive workflows, or feeding into prompts ("style of {title}").

## Install

1. Drop the `comfyui-image-of-the-day` folder into `ComfyUI/custom_nodes/`.
2. Restart ComfyUI.
3. Add the **Image of the Day** node from the `image` category.
4. Pick a source. Plug a free API key in if needed (it'll be remembered).
5. Wire the `image` output wherever you'd normally use a `LoadImage`.

No pip installs needed — the node only uses Python stdlib (`urllib`, `xml`, `json`) plus `PIL`/`numpy`/`torch` which ComfyUI already requires.

## Caching

Responses are cached for 1 hour in your system temp folder so repeated queues don't hammer the APIs unnecessarily. The cache is keyed per source / per date / per API key, so changing any of those bypasses the cache.

## Notes

- **Lorem Picsum** uses the `width` / `height` and `seed` inputs. The other sources ignore those — they always return their own size, and a `seed` of 0 means "random" for the random-image sources.
- **NASA APOD** sometimes serves a video instead of an image on the day's actual page. The node automatically falls back up to 3 days backwards to find an image entry.
- API keys are stored unencrypted in plain text on your disk. Don't share the config file. The `.gitignore` blocks accidental commits if you fork this repo.

## Support

If this saves you a daily LoadImage hassle, consider buying me a coffee:

<a href="https://buymeacoffee.com/lorasandlenses"><img src="https://img.shields.io/badge/Buy%20me%20a%20coffee-FFDD00?style=for-the-badge&logo=buy-me-a-coffee&logoColor=black" alt="Buy Me A Coffee"></a>
