import numpy as np

from manim import ORIGIN, UP, RIGHT


def distance_between_points(point1: np.ndarray, point2: np.ndarray) -> float:
    return np.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)


def wiggle_around(radius: float, origin=ORIGIN) -> np.ndarray:
    rng = np.random.default_rng()
    rand_radius = rng.random() * radius
    rand_angle = rng.random() * 2 * np.pi
    x, y = rand_radius * np.cos(rand_angle), rand_radius * np.sin(rand_angle)
    return np.array([x, y, 0])
