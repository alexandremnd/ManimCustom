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


class ElongationTest(BetterScene):
    def construct(self):
        carbone = Atom(0.4, GRAY, LEFT + UP)
        o1 = Atom(0.4, RED, RIGHT + UP)
        o2 = Atom(0.4, RED, LEFT + DOWN)
        o3 = Atom(0.4, RED, 2 * LEFT + 2 * UP)
        pb = Atom(0.4, BLUE, RIGHT + DOWN)

        liaison_c_o1 = Bound(carbone, o1, 1)
        liaison_c_o2 = Bound(carbone, o2, 1)
        liaison_c_o3 = Bound(carbone, o3, 2)
        liaison_o2_pb = Bound(o2, pb, 1)
        liaison_o1_pb = Bound(o1, pb, 1)

        self.add(liaison_c_o1, liaison_c_o2, liaison_c_o3, liaison_o1_pb, liaison_o2_pb)
        self.add(carbone, o1, o2, o3, pb)
        self.wait(1)
        self.animate(UncreateMultiple(liaison_c_o3, liaison_c_o2, liaison_c_o1, run_time=0.3), FadeOut(carbone, o3))

        def draw_spring_1():
            return Spring(o1, pb, 7, 0.2)

        def draw_spring_2():
            return Spring(o2, pb, 7, 0.2)

        spring_o1_pb = always_redraw(draw_spring_1)
        spring_o2_pb = always_redraw(draw_spring_2)


        self.animate(UncreateMultiple(liaison_o2_pb, liaison_o1_pb), CreateSimultaneous(spring_o1_pb, spring_o2_pb))

        self.play(pb.animate.move_to(ORIGIN), o2.animate.shift(2 * UP))

        symetric = Text("Symétrique").next_to(pb, UP).shift(2.5 * UP)
        antisymetric = Text("Antisymétrique").next_to(pb, UP).shift(2.5 * UP)

        self.play(Write(symetric))
        self.play(Rotate(o1, angle=PI/8, about_point=ORIGIN), Rotate(o2, angle=-PI/8, about_point=ORIGIN))
        for i in range(2):
            self.play(Rotate(o1, angle=(-1)**(i + 1) * PI / 4, about_point=ORIGIN), Rotate(o2, angle=(-1)**i * PI / 4, about_point=ORIGIN))
        self.play(Rotate(o1, angle=-PI/8, about_point=ORIGIN), Rotate(o2, angle=PI/8, about_point=ORIGIN))

        self.play(Transform(symetric, antisymetric))
        self.play(Rotate(o1, angle=PI / 8, about_point=ORIGIN),
                  Rotate(o2, angle=PI / 8, about_point=ORIGIN))
        for i in range(1, 3):
            self.play(Rotate(o1, angle=(-1) ** i * PI / 4, about_point=ORIGIN),
                      Rotate(o2, angle=(-1) ** i * PI / 4, about_point=ORIGIN))
        self.play(Rotate(o1, angle=-PI / 8, about_point=ORIGIN),
                  Rotate(o2, angle=-PI / 8, about_point=ORIGIN))

        # TODO: Animation de cisaillement ("bras/ange"), et d'avant/arrière
        # TODO: Animation ressort -> potentiel harmonique de la mécanique classique avec w = sqrt(k/mu), mu = masse réduite
        # TODO: Potentiel harmonique -> niveau d'énergie pour absorption des photons
        # TODO: Enonciation de la probabilité de passage d'un état à un autre -> différents niveaux d'absorptions
        # TODO: Mise en scène d'une spectroscopie en temps réel -> on trace l'absorbance en même temps
        # TODO: On analyse le tableau puis conclusion / ouverture sur la réflectographie qui ouvre sur de nouvelles façons de voir les oeuvres

        # self.wait(2)

class Ressort(BetterScene):
    def construct(self):


