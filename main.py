from ManimR import *
from object import *

# sine_func = lambda x: np.sin((x+10)**3 / 50)
# graph1 = FunctionGraph(sine_func, [-8, 8], color=WHITE)
#
# self.play(Create(graph1), run_time=3) self.play(graph1.animate.set_stroke(color_gradient([PURE_RED, ORANGE, YELLOW,
# GREEN, PURE_GREEN, TEAL, PURE_BLUE, "#FF00FF"], 100)[::-1]))


class Introduction(BetterScene):
    def construct(self):
        pass


class PotentielDeMorse(BetterScene):
    def construct(self):
        # ALWAYS REDRAW FUNCTION
        w = ValueTracker(10)
        sine = lambda x: 0.3 * np.sin(w.get_value() * x)
        color = color_gradient([RED_D, PURE_RED, ORANGE, YELLOW, GREEN, BLUE_D, PURE_BLUE, "#FF00FF"], 22)
        self.curve = FunctionGraph(sine, x_range=[-4, 4], color=RED)

        def draw_wave():
            index = int(w.get_value()) - 10
            c = color[index]
            return FunctionGraph(sine, x_range=[-8, 8], color=c)

        wave = always_redraw(draw_wave)

        self.add(wave)
        self.wait(1)
        self.play(w.animate.set_value(30), run_time=10)
        self.wait(2)
