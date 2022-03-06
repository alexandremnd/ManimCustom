from ManimR import *
from math import factorial, ceil, sqrt, exp


class MorsePotential(VGroup):
    def __init__(self):
        super(MorsePotential, self).__init__()

        self.n = 1
        self.w0 = 100
        self.m1 = 1
        self.m2 = 1
        self.func = FunctionGraph(self.__psi_density_squared_internal__, x_range=[-8, 8])

        self.add(func)

    def __psi_internal__(self, x: float) -> float:
        return MorsePotential.psi(x, self.n, self.w0, self.m1, self.m2)

    def __psi_density_squared_internal__(self, x: float) -> float:
        return MorsePotential.psi_density_squared(x, self.n, self.w0, self.m1, self.m2)

    @staticmethod
    def psi(x: float, n: int, w0: float, m1: float = 1, m2: float = 1) -> float:
        planck_constant = 2
        reduced_planck_constant = planck_constant / (2 * np.pi)
        mu = m1 * m2 / (m1 + m2) # Reduced mass
        alpha = mu * w0 / 10

        f1 = (alpha / np.pi) ** (1/4)
        f2 = sqrt(1/(2**n * factorial(n)))
        f3 = exp(-alpha * x**2 / 2)
        f4 = MorsePotential.hermite_function(n, sqrt(alpha) * x)

        print(f1, f2, f3, f4)
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
