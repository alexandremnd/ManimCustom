import json
from itertools import zip_longest

import matplotlib.pyplot as plt
import numpy as np

from ManimR import *
from object import *

# with open("data/painting.json") as f:
#     jsonObject = json.load(f)
#
# data = jsonObject["series"]["Submitter"]
#
# wavenumber = []
# absorbance = []
# for key in data:
#     wavenumber.append(round(float(key), 8))
#     absorbance.append(max(round(data[key], 8), 0))
#
# wavenumber = np.array(wavenumber)
# absorbance = np.array(absorbance)
#
#
# fig, ax = plt.subplots()
# ax.plot(wavenumber, 10**(-absorbance)) # Transmitance = 10**(-absorbance)
# ax.invert_xaxis()
# # ax.set_ylim(0, 0.20)
# plt.show()


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
        name = VGroup(alek, golem, nilo).arrange(DOWN, buff=0.1).next_to(title, DOWN, buff=0.3)

        self.add(logo_upsud)
        self.add(theme)
        self.add(name)
        self.wait(3)
        self.play(Write(title))
        self.wait(2)


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

class GlobalView(BetterScene):
    def construct(self):
        self.next_section(skip_animations=True)
        waiting_logo = WaitingLogo()

        for anim in waiting_logo.wait(3):
            self.play(anim)

        spectrometer = Rectangle(BLUE_D, height=1, width=2)
        work = Line(3 * RIGHT + 2 * UP, 3 * RIGHT + 2 * DOWN, stroke_width=5)

        def draw_spectro_title():
            return Text("Spectromètre", font_size=18, font="Karla").move_to(spectrometer)

        spectrometer_title = always_redraw(draw_spectro_title)
        self.play(Transform(waiting_logo, VGroup(spectrometer, spectrometer_title, work)))

        self.next_section()
        self.add(line)

class Graph(BetterScene):
    def construct(self):
        wavenumber = np.loadtxt("data/wavenumber.txt")
        absorbance = np.loadtxt("data/absorbance.txt")

        ax = Axes(
            x_range=[wavenumber[-1], wavenumber[0], 1000],
            x_length=7,
            y_length=5,
            y_range=[0, 0.45, 0.2],
            tips=True,
            axis_config={"include_numbers": True},
            y_axis_config={"scaling": LinearBase()},
        )
        #ax.flip(UP)

        nu = MathTex(r"\nu")
        A = MathTex(r"A")
        labels = ax.get_axis_labels(x_label=nu, y_label=A).set_color(WHITE)
        graph = ax.plot_line_graph(wavenumber[::-1], absorbance[::-1], add_vertex_dots=False, stroke_width=2).set_color(WHITE).flip(UP)
        for sub in ax.submobjects:
            print(sub)

        self.animate(CreateSimultaneous(ax, labels))
        self.play(Create(graph))
        self.wait()





class VibrationMode(BetterScene):
    def construct(self):
        self.next_section(skip_animations=True)
        original_compounds = PbMolecule()

        x_list = [-4, -4, 0, 0]
        y_list = [2, -2] * 2

        compounds = []
        for x, y in zip(x_list, y_list):
            molecule = PbMolecule([x, y, 0])
            compounds.append(molecule)

        compounds.append(PbMoleculeSide([4, 2, 0]))
        compounds.append(PbMoleculeSide([4, -2, 0]))

        self.add(original_compounds)
        self.play(Transform(VGroup(original_compounds), VGroup(*compounds)))
        self.clear()

        self.next_section(skip_animations=True)

        self.add(*compounds)
        self.wait(0.25)

        self.next_section(skip_animations=True)

        anim0 = compounds[0].stretching(0.25, UL, UR, 10, 10)
        anim1 = compounds[1].stretching(0.25, UL, UR, 10, 10, False)
        anim2 = compounds[2].scissoring(PI / 12, 10, 10)
        anim3 = compounds[3].scissoring(PI / 12, 10, 10, False)
        anim4 = compounds[4].wagging(0.25 * LEFT, 10, 10)
        anim5 = compounds[5].wagging(0.25 * LEFT, 10, 10, False)

        for a0, a1, a2, a3, a4, a5 in zip_longest(anim0, anim1, anim2, anim3, anim4, anim5):
            self.animate_unpack(a0, a1, a2, a3, a4, a5)
        self.wait()

        self.next_section(skip_animations=False)


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


class Poubelle(BetterScene):
    def construct(self):
        amplitude = 0.1
        frequency = ValueTracker(10)

        def photon_redraw():
            coeff = -34
            b = 1120
            lam = coeff * frequency.get_value() + b
            return Photon(spectrometer.get_corner(RIGHT), work.get_corner(LEFT), amplitude=amplitude,
                          frequency=frequency.get_value())

        def lambda_redraw():
            coeff = -34
            b = 1120
            lam = coeff * frequency.get_value() + b
            value = Text(f"{lam:.0f}nm").scale(0.5)
            group = VGroup(lam_tex.copy(), value).arrange(RIGHT, buff=0.2).next_to(photon, DOWN).scale(0.5)
            return group

        lam_tex = MathTex(rf"\lambda = ")
        photon = always_redraw(photon_redraw)
        wavelength = always_redraw(lambda_redraw)

        self.play(Create(photon), Create(wavelength))
        self.play(frequency.animate.set_value(20))
        self.wait()