import numpy as np

from ManimR import *
from object import *


class WaitingLogo(VGroup):
    def __init__(self):
        super(WaitingLogo, self).__init__()
        
        dot = Dot(ORIGIN, radius=0.2)
        items = []
        colors = [BLUE_C, BLUE_D, BLUE_E, BLUE_B, ]
        for i in range(4):
            item = Ellipse(1.8, 0.6).set_color(colors[i])
            item.rotate_about_origin(i * PI / 4)
            items.append(item)

        self.add(dot, *items)

    def wait(self, count, run_time = -1):
        if run_time == -1:
            run_time = (count + 5) / (count + 2)
        else:
            run_time = run_time / (count + 2)

        s1_to_s2 = 0.8 / 1.2
        s2_to_s1 = 1.2 / 0.8

        yield self.animate(run_time=run_time).scale(1.2)
        for i in range(count):
            yield self.animate(run_time=run_time).scale(s1_to_s2 if i % 2 == 0 else s2_to_s1)

        if count % 2 == 1:
            yield self.animate(run_time=run_time).scale(1 / 0.8)
        else:
            yield self.animate(run_time=run_time).scale(1 / 1.2)