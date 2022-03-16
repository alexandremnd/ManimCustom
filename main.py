from ManimR import *
from object import *

config.background_color = "#1d1d1d"

class Introduction(BetterScene):
    def construct(self):
        logo_upsud = SVGMobject("img/Logo.svg").set_fill("#63003C", opacity=1)

        # move logo_upsud to top left corner
        logo_upsud.scale(0.5)
        logo_upsud.to_edge(UL)
        logo_upsud.shift(0.2*UP)

        theme = Text("Thème 2022: La science dans l'art", font_size=35, font="Karla").shift(UP)
        title = Text("SPECTROSCOPIE INFRAROUGE", font_size=35, font="Karla").next_to(theme, DOWN, buff=0.3)

        alek = Text("Alexandre MENARD", font_size=20, font="Karla")
        golem = Text("Florent VIEILLEDENT", font_size=20, font="Karla")
        nilo = Text("Nilo RANCHY", font_size=20, font="Karla")
        edouard = Text("Edouard SADEK", font_size=20, font="Karla")
        name = VGroup(alek, golem, nilo, edouard).arrange(DOWN, buff=0.1).next_to(title, DOWN, buff=0.3)

        self.add(logo_upsud)
        self.add(theme)
        self.add(name)
        self.wait(3)
        self.play(Write(title))
        self.wait(2)


class WavelengthIllustration(Scene):
    def construct(self):
        animation_duration = 5
        fps = self.camera.frame_rate
        w = ValueTracker(1.5)
        sine = lambda x: 0.3 * np.sin(w.get_value() * x)
        color = color_gradient([RED_D, PURE_RED, ORANGE, YELLOW, GREEN, BLUE_D, PURE_BLUE, "#FF00FF"],
                               fps * animation_duration + 1)
        self.curve = FunctionGraph(sine, x_range=[-4, 4], color=RED)

        def draw_wave():
            frame = (w.get_value() - 1.5) / 3.8 * fps * animation_duration
            frame = int(frame)
            c = color[frame]
            return FunctionGraph(sine, x_range=[-4, 4], color=c)

        wave = always_redraw(draw_wave)

        self.add(wave)
        self.wait(1)
        self.play(w.animate.set_value(5.2), run_time=animation_duration)
        self.wait(2)
        pass
