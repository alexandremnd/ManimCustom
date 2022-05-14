from math import atan2
from ManimR import *


class Photon(VGroup):
    def __init__(self, start: np.ndarray = ORIGIN, end: np.ndarray = RIGHT, amplitude: float = 0.2, frequency: float = 10,
                 color: str = YELLOW_C, width=5) -> None:
        super().__init__()

        def sinusoidal_func(x: float) -> float:
            return amplitude * np.sin(x * frequency)

        distance_start_to_end = distance_between_points(start, end)
        x_diff = end[0] - start[0]
        y_diff = end[1] - start[1]
        angle = atan2(y_diff, x_diff)

        self.wave_photon = FunctionGraph(sinusoidal_func, x_range=[0, distance_start_to_end], color=color, stroke_width=width)
        self.wave_head = Circle(radius=0.1, color=color, fill_color=color, fill_opacity=1)

        # Lambda is useful in this case because it allows access to self.wave_photon
        # Classical functions loose scope on self object.
        self.wave_head.add_updater(lambda obj: obj.move_to(self.wave_photon.points[-1]))

        self.wave_photon.rotate(angle)
        self.wave_photon.shift(end - self.wave_photon.points[-1])
        #self.wave_photon.shift(start)

        self.add(self.wave_photon)
        #self.add(self.wave_head)

    @override_animation(Create)
    def __create_override(self):
        wave_creation = Create(self.wave_photon)
        # wave_head_add = Add(self.wave_head)
        return wave_creation

