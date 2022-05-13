import numpy as np

from manim import ORIGIN, UP, RIGHT, Mobject, AnimationGroup, rgb_to_hex
from copy import deepcopy


def distance_between_points(point1: np.ndarray, point2: np.ndarray) -> float:
    return np.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)


def wiggle_around(radius: float, origin=ORIGIN) -> np.ndarray:
    rng = np.random.default_rng()
    rand_radius = rng.random() * radius
    rand_angle = rng.random() * 2 * np.pi
    x, y = rand_radius * np.cos(rand_angle), rand_radius * np.sin(rand_angle)
    return np.array([x, y, 0])

def wavelength_to_rgb(wavelength, gamma=0.8):

    '''This converts a given wavelength of light to an
    approximate RGB color value. The wavelength must be given
    in nanometers in the range from 380 nm through 750 nm
    (789 THz through 400 THz).

    Based on code by Dan Bruton
    http://www.physics.sfasu.edu/astro/color/spectra.html
    '''

    wavelength = float(wavelength)
    if wavelength >= 380 and wavelength <= 440:
        attenuation = 0.3 + 0.7 * (wavelength - 380) / (440 - 380)
        R = ((-(wavelength - 440) / (440 - 380)) * attenuation) ** gamma
        G = 0.0
        B = (1.0 * attenuation) ** gamma
    elif wavelength >= 440 and wavelength <= 490:
        R = 0.0
        G = ((wavelength - 440) / (490 - 440)) ** gamma
        B = 1.0
    elif wavelength >= 490 and wavelength <= 510:
        R = 0.0
        G = 1.0
        B = (-(wavelength - 510) / (510 - 490)) ** gamma
    elif wavelength >= 510 and wavelength <= 580:
        R = ((wavelength - 510) / (580 - 510)) ** gamma
        G = 1.0
        B = 0.0
    elif wavelength >= 580 and wavelength <= 645:
        R = 1.0
        G = (-(wavelength - 645) / (645 - 580)) ** gamma
        B = 0.0
    elif wavelength >= 645 and wavelength <= 750:
        attenuation = 0.3 + 0.7 * (750 - wavelength) / (750 - 645)
        R = (1.0 * attenuation) ** gamma
        G = 0.0
        B = 0.0
    else:
        R = 0.0
        G = 0.0
        B = 0.0
    R *= 255
    G *= 255
    B *= 255
    return (int(R), int(G), int(B))

def wavelength_to_hex(wavelength):
    if isinstance(wavelength, np.ndarray | tuple | list):
        hex = []
        for lam in wavelength:
            hex.append(wavelength_to_hex(lam))
        return hex
    return rgb_to_hex(wavelength_to_rgb(wavelength))



