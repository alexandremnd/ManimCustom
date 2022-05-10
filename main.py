import json
from itertools import zip_longest

from ManimR import *
from object import *

with open("data/lead_white.json") as f:
    jsonObject = json.load(f)

data = jsonObject["series"]["Submitter"]

wavenumber = []
absorbance = []
for key in data:
    wavenumber.append(round(float(key), 8))
    absorbance.append(max(round(data[key], 8), 0))
    
wavenumber = np.array(wavenumber)
absorbance = np.array(absorbance)
    
    
# fig, ax = plt.subplots()
# ax.plot(wavenumber, absorbance) # Transmitance = 10**(-absorbance)
# ax.invert_xaxis()
# # ax.set_ylim(0, 0.20)
# plt.show()


config.background_color = "#212121"


class Citation(BetterScene):
    def construct(self):
        citation1 = Text("\"Envisager l'art sous l'angle de ses matériaux", font="Karla", font_size=25)
        citation2 = Text("amène à privilégier les pratiques plus que la", font="Karla", font_size=25)
        citation3 = Text("considération des oeuvres closes et fermées\"", font="Karla", font_size=25)
        group = VGroup(citation1, citation2, citation3).arrange(DOWN, buff=DEFAULT_MOBJECT_TO_MOBJECT_BUFFER/2)

        author = Text("-Florence de Mèredieu", color="#18a5d4", font="Karla", font_size=20, weight=BOLD)
        author.next_to(group, ORIGIN, aligned_edge=RIGHT).shift(DOWN)

        self.play(Write(group), run_time=9)
        self.wait(1)
        self.play(Write(author))


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
        name = VGroup(alek, golem, nilo).arrange(DOWN, buff=0.1).next_to(title, DOWN, buff=0.3)

        self.add(logo_upsud)
        self.add(theme)
        self.add(name)
        self.wait(3)
        self.play(Write(title))
        self.wait(2)


class MomentDipolaire(BetterScene):
    def construct(self):
        lead = Atom(0.5, BLUE, 0.5 * DOWN)
        oxygen1 = Atom(0.4, RED, 0.5 * UP + LEFT)
        oxygen2 = Atom(0.4, RED, 0.5 * UP + RIGHT)
        h1 = Atom(0.2, WHITE, oxygen1.get_center() + 0.3 * UL)
        h2 = Atom(0.2, WHITE, oxygen2.get_center() + 0.3 * UR)

        alcool1 = VGroup(h1, oxygen1)
        alcool2 = VGroup(h2, oxygen2)

        bound_lead_ox1 = Bound(lead, oxygen1, 1)
        bound_lead_ox2 = Bound(lead, oxygen2, 1)

        def dipolar_redraw():
            lead_pos = lead.get_center()
            positive_center = lead_pos
            negative_center = (oxygen1.get_center() - lead_pos) + (oxygen2.get_center() - lead_pos)

            arrow = Arrow(start=negative_center, end=positive_center, stroke_width=1.5, buff=0.5, tip_length=0.2, max_tip_length_to_length_ratio=0.5)
            mu = MathTex("\\vec{\\mu}").next_to(arrow, UP).scale(0.8)

            return VGroup(arrow, mu)

        dipolar_moment = always_redraw(dipolar_redraw)

        self.add(bound_lead_ox1, bound_lead_ox2, alcool1, alcool2, lead)
        self.play(Create(dipolar_moment))

        self.wait()

        elongate_two(self, alcool1, alcool2, 0.25 * UL, 0.25 * UR, 5)
        self.wait()
        elongate_two(self, alcool1, alcool2, 0.25 * UL, -0.25 * UR, 5)


class VibrationMode(BetterScene):
    def construct(self):
        self.next_section(skip_animations=True)
        original_compounds = PbMolecule()

        x_list = [-4, -4, 0, 0, 4, 4]
        y_list = [2, -2] * 3

        compounds = []
        for x, y in zip(x_list, y_list):
            molecule = PbMolecule([x, y, 0])
            compounds.append(molecule)

        self.add(original_compounds)
        self.play(Transform(VGroup(original_compounds), VGroup(*compounds)))
        self.clear()
        self.add(*compounds)
        self.wait(0.25)

        self.next_section()

        anim0 = compounds[0].elongate(0.25, UL, UR, 10, 10)
        anim1 = compounds[1].elongate(0.25, UL, UR, 10, 10, False)
        anim2 = compounds[2].wagging(PI/8, 10, 10, True)
        anim3 = compounds[3].wagging(PI/8, 10, 10, False)
        for a0, a1, a2, a3 in zip_longest(anim0, anim1, anim2, anim3):
            self.animate_unpack(a0, a1, a2, a3)
        self.wait()

        self.next_section()

        # animations = []
        # for i, (x, y) in enumerate(zip(x_list, y_list)):
        #     animations.append(original_compounds[i].animate.move_to([x, y, 0]))
        #
        # self.add(*original_compounds)
        # self.wait()
        # self.play(*animations)
        # self.wait()


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

        self.play(Circumscribe(o1, Circle))

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

        self.wait(2)


class Ressort(BetterScene):
    def construct(self) -> None:
        lead = Atom(1, BLUE, 2 * LEFT)
        oxygen = Atom(0.3, RED, 2 * RIGHT)
        ressort = always_redraw(lambda: Spring(lead, oxygen, 11, 0.3))

        self.add(lead, oxygen)
        self.play(Create(ressort))
        self.wait(0.5)

        self.next_section()


class PotentielHarmonique(BetterScene):
    def construct(self) -> None:
        ax = Axes(
            x_range=[0, 5, 1],
            x_length=7,
            y_length=7,
            y_range=[-2, 6, 1],
            tips=True,
            axis_config={"include_numbers": False},
            y_axis_config={"scaling": LinearBase()},
        )

        a, re = 7, 2
        labels = ax.get_axis_labels(x_label='r', y_label='E').set_color(WHITE)
        graph = ax.plot(lambda x: a * (x - re) ** 2, x_range=[1.15, 2.85], use_smoothing=True)

        self.animate(CreateSimultaneous(ax, graph, labels))
        for E in range(1, 5):
            x2 = (2 * re + np.sqrt(4 * E / a)) / 2
            x1 = (2 * re - np.sqrt(4 * E / a)) / 2

            point1 = ax.coords_to_point(*[x1, E, 0])
            point2 = ax.coords_to_point(*[x2, E, 0])
            
            level_tex = Tex(f"$\\nu_{E}$").scale(0.8).next_to(point2, RIGHT)

            self.play(Create(Line(point1, point2)), run_time=0.2)
            self.play(Write(level_tex), run_time=0.1)

        self.wait(1)


class Sandbox(BetterScene):
    def construct(self):
        omega = MathTex("\\omega = \\sqrt{\\frac{k}{\\mu}}")
        self.add(omega)
        self.wait(0.5)
        pass