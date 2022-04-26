import numpy as np

from ManimR import *
from object import *

class Spring(VGroup):
    def __init__(self, atom1: Atom, atom2: Atom, points_count: int, amplitude: float) -> None:
        super(Spring, self).__init__()

        atom1_center = atom1.get_center()
        atom2_center = atom2.get_center()
        atom1_radius = atom1.radius
        atom2_radius = atom2.radius

        d = distance_between_points(atom1_center, atom2_center)
        a1_a2 = atom2_center - atom1_center
        ur = a1_a2 / d
        up = np.array([-ur[1], ur[0], 0])

        p1 = atom1_center + atom1_radius * ur
        p2 = p1 + 0.1 * d * ur

        pn = atom2_center - atom2_radius * ur
        pn_minus_1 = pn - 0.1 * d * ur

        points = [p1, p2]

        delta_points = np.linspace(0, distance_between_points(p2, pn_minus_1), points_count)
        for i in range(1, len(delta_points) - 1):
            y = amplitude if i % 2 else -amplitude
            points.append(p2 + delta_points[i] * ur + y * up)

        points.append(pn_minus_1)
        points.append(pn)

        for i in range(len(points) - 1):
            self.add(Line(points[i], points[i + 1]))

        for i in range(len(points)):
            self.add(Dot(points[i], radius=0.02))