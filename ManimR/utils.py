import numpy as np

from manim import ORIGIN, UP, RIGHT, Mobject, AnimationGroup


def distance_between_points(point1: np.ndarray, point2: np.ndarray) -> float:
    return np.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)


def wiggle_around(radius: float, origin=ORIGIN) -> np.ndarray:
    rng = np.random.default_rng()
    rand_radius = rng.random() * radius
    rand_angle = rng.random() * 2 * np.pi
    x, y = rand_radius * np.cos(rand_angle), rand_radius * np.sin(rand_angle)
    return np.array([x, y, 0])


def elongate(obj: Mobject, delta, count):
    initial_position = obj.get_center()
    x1 = initial_position + delta
    x2 = initial_position - delta

    animations = []

    for i in range(count):
        anim = obj.animate.move_to(x1 if i % 2 == 0 else x2)
        animations.append(anim)

    animations.append(obj.animate.move_to(initial_position))
    return animations

def elongate_two(obj1, obj2, delta1, delta2):
    initial_position1 = obj.get_center()
    x1_1 = initial_position + delta
    x2 = initial_position - delta

    animations = []

    for i in range(count):
        anim = obj.animate.move_to(x1 if i % 2 == 0 else x2)
        animations.append(anim)

    animations.append(obj.animate.move_to(initial_position))
    return animations
