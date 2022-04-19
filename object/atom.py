from ManimR import *


class Atom(VGroup):
    def __init__(self, radius: float, color: str = WHITE, position: np.ndarray = np.array([0, 0, 0])) -> None:
        super().__init__()
        self.radius = radius

        shadow_color = rgb_to_hex(hex_to_rgb(color) * hex_to_rgb(GRAY_B))
        molecule = Circle(radius=1, color=shadow_color, fill_color=shadow_color, fill_opacity=1)
        light_side = Circle(radius=1)
        light_side.shift(RIGHT * 0.2 + UP * 0.2)

        intersect = Intersection(molecule, light_side).set_fill(color=color, opacity=1).set_stroke(color)

        self.add(molecule, intersect)
        self.scale(radius)
        self.move_to(position)