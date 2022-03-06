import numpy as np

from ManimR import *


class EnergyDiagram(VGroup):
    def __init__(self, position: np.ndarray):
        super().__init__()

        self.energy_arrow = Arrow(start=position, end=position + 4 * UP, buff=0)

        l1 = Line(start=position, end=position + 2 * RIGHT).shift(UP * 0.1)
        l2 = Line(start=position, end=position + 2 * RIGHT).shift(UP * 1.6)
        l3 = Line(start=position, end=position + 2 * RIGHT).shift(UP * 2.6)
        l4 = Line(start=position, end=position + 2 * RIGHT).shift(UP * 3.1)
        self.energy_levels: tuple[Line, Line, Line, Line] = (l1, l2, l3, l4)

        tex: list[Tex] = [Tex(f"$E_{i}$").next_to(self.energy_levels[i - 1], LEFT).scale(0.8) for i in range(1, len(self.energy_levels) + 1)]
        self.energy_labels: tuple[Tex] = tuple(tex)

        self.add(self.energy_arrow, *self.energy_labels, *self.energy_levels)

    @override_animation(Create)
    def __create_override(self):
        energy_arrow_creation = Create(self.energy_arrow)
        energy_level_creation = CreateSimultaneous(*self.energy_labels, *self.energy_levels)

        return AnimationPacker(energy_arrow_creation, energy_level_creation)

    def shift(self, shift_value: np.ndarray) -> None:
        for obj in self.submobjects:
            obj.shift(shift_value)

    @override_animate(shift)
    def __shift_override(self):
        pass