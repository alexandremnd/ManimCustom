import numpy as np

from manim import ORIGIN, UP, RIGHT, Mobject, AnimationGroup
from copy import deepcopy


def distance_between_points(point1: np.ndarray, point2: np.ndarray) -> float:
    return np.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)


def wiggle_around(radius: float, origin=ORIGIN) -> np.ndarray:
    rng = np.random.default_rng()
    rand_radius = rng.random() * radius
    rand_angle = rng.random() * 2 * np.pi
    x, y = rand_radius * np.cos(rand_angle), rand_radius * np.sin(rand_angle)
    return np.array([x, y, 0])

def elongate_two(scene, obj1, obj2, delta1, delta2, count):
    obj1_initial_pos = obj1.get_center()
    obj2_initial_pos = obj2.get_center()
    obj1_x1= obj1_initial_pos + delta1
    obj1_x2 = obj1_initial_pos - delta1
    obj2_x1 = obj2_initial_pos + delta2
    obj2_x2 = obj2_initial_pos - delta2

    for i in range(count):
        anim1 = obj1.animate.move_to(obj1_x1 if i % 2 == 0 else obj1_x2)
        anim2 = obj2.animate.move_to(obj2_x1 if i % 2 == 0 else obj2_x2)
        scene.play(anim1, anim2)

    scene.play(obj1.animate.move_to(obj1_initial_pos), obj2.animate.move_to(obj2_initial_pos))

    return None