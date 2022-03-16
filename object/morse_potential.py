from ManimR import *
from math import factorial, ceil, sqrt, exp, nan


class MorsePotential(VGroup):
    def __init__(self):
        super(MorsePotential, self).__init__()

        self.axe = Axes(x_range=[0, 5], y_range=[0, 8])

        self.n = 1
        self.w0 = 50
        self.m1 = 1
        self.m2 = 1
        self.func =  self.axe.plot(self.__psi_density_squared_internal__, x_range=[-4, 4])

        self.De = 2
        self.Vre = 0
        self.re = 1
        self.a = 2
        self.morse = self.axe.plot(self.__morse_internal__, x_range=[0.8, 3])

        self.add(self.axe, self.morse)

    def __psi_internal__(self, x: float) -> float:
        return MorsePotential.psi(x, self.n, self.w0, self.m1, self.m2)

    def __psi_density_squared_internal__(self, x: float) -> float:
        return MorsePotential.psi_density_squared(x, self.n, self.w0, self.m1, self.m2)

    def __morse_internal__(self, x: float) -> float:
        return MorsePotential.morse_potential_function(x, self.De, self.Vre, self.re, self.a)

    @staticmethod
    def psi(x: float, n: int, w0: float, m1: float = 1, m2: float = 1) -> float:
        planck_constant = 40
        reduced_planck_constant = planck_constant / (2 * np.pi)
        mu = m1 * m2 / (m1 + m2) # Reduced mass
        alpha = mu * w0 / reduced_planck_constant

        f1 = (alpha / np.pi) ** (1/4)
        f2 = sqrt(1/(2**n * factorial(n)))
        f3 = exp(-alpha * x**2 / 2)
        f4 = MorsePotential.hermite_function(n, sqrt(alpha) * x)

        return f1 * f2 * f3 * f4

    @staticmethod
    def psi_density_squared(x: float, n: int, w0: float, m1: float = 1, m2: float = 1) -> float:
        return MorsePotential.psi(x, n, w0, m1, m2) ** 2

    @staticmethod
    def hermite_function(n: int, x: float):
        match n:
            case 0:
                return 1
            case 1:
                return 2 * x
            case 2:
                return 4 * x**2 - 2
            case 3:
                return 8 * x**3 - 12 * x
            case 4:
                return 16 * x**4 - 48 * x**2 + 12
            case 5:
                return 32 * x**5 - 160 * x**3 + 120 * x
            case 6:
                return 64 * x**6 - 480 * x**4 + 720 * x**2 - 120

    @staticmethod
    def morse_potential_function(x: float, De: float, Vre: float, re: float, a: float) -> float:
        value = De * (1 - exp(-a * (x - re)))**2 + Vre
        print(value)
        return value