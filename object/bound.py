import numpy as np

from ManimR import *
from object import *

class Bound(VGroup):
    def __init__(self, atom1: Atom, atom2: Atom, bound_count: int):
        if bound_count == 0 or bound_count >= 4:
            raise ValueError("bound_count can only be between 1 and 3 (or go fuck yourself :))")
        super().__init__()

        self.bound_count: int= bound_count
        self.atom1: Atom = atom1
        self.atom2: Atom = atom2

        funs = [self.get_first_line, self.get_second_line, self.get_third_line]
        for i in range(self.bound_count):
            line = always_redraw(funs[i])
            self.add(line)

    def get_displacement(self):
        a = self.atom2.get_x() - self.atom1.get_x()
        b = self.atom2.get_y() - self.atom1.get_y()
        delta = -np.sin(np.arctan2(b,a)) * RIGHT + np.cos(np.arctan2(b,a)) * UP

        return delta

    def get_first_line(self):
        return self.get_line(0)

    def get_second_line(self):
        return self.get_line(1)

    def get_third_line(self):
        return self.get_line(2)

    def get_line(self, line_index):
        if line_index > self.bound_count:
            raise ValueError("bound_count can only be between 1 and 3 (or go fuck yourself :))")

        c1 = self.atom1.get_center()
        c2 = self.atom2.get_center()
        delta = self.get_displacement()

        if self.bound_count == 1:
            return Line(c1, c2)
        elif self.bound_count == 2:
            point1 = c1 + delta * (2 * line_index - 1) * self.atom1.radius / 3
            point2 = c2 + delta * (2 * line_index - 1) * self.atom2.radius / 3
            return Line(point1, point2)
        else:
            point1 = c1 + delta * (line_index - 1) * self.atom1.radius / 3
            point2 = c2 + delta * (line_index - 1) * self.atom2.radius / 3
            return Line(point1, point2)
