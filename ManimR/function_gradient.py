from manim import Mobject, override_animation, Create, Dot, RED, UP, RIGHT, color_gradient, BLUE, GREEN, PURPLE, YELLOW
from ManimR.animation import CreateOneByOne, Add


class Function(Mobject):
    def __init__(self, function, x_range: tuple[float, float]):
        self.function = function
        self.x_range = x_range
        self.precision = 0.05

        self.start = min(self.x_range[0], self.x_range[1])
        self.end = max(self.x_range[0], self.x_range[1])

    @override_animation(Create)
    def __override_create(self):
        length = self.end - self.start
        nb_points = int(length / self.precision)
        colors = color_gradient([RED, YELLOW, GREEN, BLUE, PURPLE], nb_points)

        point = []
        for i in range(0, nb_points):
            point.append(Dot(self.function(self.precision * i) * UP + RIGHT * (self.start + self.precision * i), self.precision, color=colors[i]))

        return Add(*point)
