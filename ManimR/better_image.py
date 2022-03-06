import numpy as np
from PIL import Image
from manim import hex_to_rgb, WHITE, ImageMobject, QUALITIES, DEFAULT_QUALITY, RESAMPLING_ALGORITHMS
import pathlib


class BetterImage(ImageMobject):
    def __init__(self,
                 filename_or_array,
                 color: str = WHITE,
                 scale_to_resolution=QUALITIES[DEFAULT_QUALITY]["pixel_height"],
                 invert=False,
                 image_mode="RGBA",
                 **kwargs, ) -> None:
        if isinstance(filename_or_array, (str, pathlib.PurePath)):
            img_array = BetterImage.load_png(filename_or_array, color)
            super().__init__(img_array, scale_to_resolution, invert, image_mode, **kwargs)
            self.set_resampling_algorithm(RESAMPLING_ALGORITHMS["cubic"])
        else:
            super().__init__(filename_or_array, scale_to_resolution, invert, image_mode, **kwargs)

    @staticmethod
    def load_png(filename: str, color: str = WHITE) -> np.ndarray:
        img: Image = Image.open(filename)
        img_array = np.array(img)

        factor_r, factor_g, factor_b = hex_to_rgb(color)
        factor = np.array([factor_r, factor_g, factor_b, 1])

        # Needs to cast array into uint8 or Manim fucks everything. Fuck my life
        img_array = np.array(np.multiply(img_array, factor), dtype="uint8")

        return img_array