from ManimR import *
from object import *

config.background_color = "#212121"

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


class Elongation(Scene):
    def construct(self):
        carbone = Atom(0.4, GRAY, LEFT + UP)
        o1 = Atom(0.4, RED, RIGHT + UP)
        o2 = Atom(0.4, RED, LEFT + DOWN)
        o3 = Atom(0.4, RED, 2 * LEFT + 2 * UP)
        pb = Atom(0.6, BLUE, RIGHT + DOWN)

        liaison_c_o1 = Line(carbone.get_center(), o1.get_center())
        liaison_c_o2 = Line(carbone.get_center(), o2.get_center())
        liaison_o1_pb = Line(o1.get_center(), pb.get_center())
        liaison_o2_pb = Line(o2.get_center(), pb.get_center())
        liaison_c_o3_1 = Line(carbone.get_center() + UR * 0.05, o3.get_center() + UR * 0.05)
        liaison_c_o3_2 = Line(carbone.get_center() + DL * 0.05, o3.get_center() + DL * 0.05)

        self.add(liaison_c_o3_1, liaison_c_o3_2, liaison_o2_pb, liaison_o1_pb, liaison_c_o2, liaison_c_o1)
        self.add(carbone, o1, o2, o3, pb)
        self.wait(1)
        self.play(Uncreate(liaison_c_o3_1), Uncreate(liaison_c_o3_2), Uncreate(liaison_c_o2), Uncreate(liaison_c_o1), FadeOut(carbone, o3))
        self.wait(1)




class WavelengthIllustration(Scene):
    def construct(self):
        animation_duration = 5
        fps = self.camera.frame_rate
        w = ValueTracker(1.5)
        sine = lambda x: 0.3 * np.sin(w.get_value() * x)
        color = color_gradient([RED_D, PURE_RED, ORANGE, YELLOW, GREEN, BLUE_D, PURE_BLUE, "#FF00FF"],
                               fps * animation_duration + 1)
        self.curve = FunctionGraph(sine, x_range=[-4, 4], color=RED)


