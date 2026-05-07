"""comfyui-image-of-the-day — fetch images from 8 daily / random sources."""

from .nodes import ImageOfDayLoader

NODE_CLASS_MAPPINGS = {
    "ImageOfDayLoader": ImageOfDayLoader,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "ImageOfDayLoader": "Image of the Day",
}

__all__ = ["NODE_CLASS_MAPPINGS", "NODE_DISPLAY_NAME_MAPPINGS"]
