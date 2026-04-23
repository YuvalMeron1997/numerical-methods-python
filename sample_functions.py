"""
Utility functions and shapes for testing numerical methods.

Includes function generators and geometric shapes used for
experimentation and validation.
"""

import numpy as np
from function_utils import AbstractShape


def exp(b):
    """
    :param b: the exponent base
    :return: a function f(x)=b^x
    """
    return lambda x: b ** x


def poly(*a):
    """
    :param a: a list of coefficients starting with the coefficient of the highest degree down to 0.
    :return: same as numpy.poly1d(a)
    """
    return np.poly1d(a)


def randomIntersectingPolynomials(deg):
    """
    Generates two polynomials of degree deg such that the first and last coefficients have negative signs. 
    [-,...,+]
    [+,...,-]
    Deg must be even. If deg is even then such polynomials intersect in at least two points.     
    """
    # Note: adding/subtracting 0.001 in the code below is a patch to avoid rare cases of zero coefficients

    assert (deg % 2 == 0)
    a1 = np.random.randn(deg + 1)
    a1[0] = abs(a1[0]) + 0.001
    a1[-1] = -1 * abs(a1[-1]) - 0.001
    f1 = np.poly1d(a1)
    assert (f1(0) < 0)

    a2 = np.random.randn(deg + 1)
    a2[0] = -1 * abs(a2[0]) - 0.001
    a2[-1] = abs(a2[-1]) + 0.001
    f2 = np.poly1d(a2)
    assert (f2(0) > 0)

    return f1, f2


def sinus():
    return np.sin


def strong_oscilations():
    def f(x):
        return 2.0 ** (1 / (x ** 2)) * np.sin(1 / x)

    return f


def bezier2(P1, P2, P3):
    M = np.array(
        [[1, -2, 1],
         [-2, 2, 0],
         [1, 0, 0]],
        dtype=np.float32
    )
    P = np.array([P1, P2, P3], dtype=np.float32)

    def f(t):
        T = np.array([t ** 2, t, 1], dtype=np.float32)
        return T.dot(M).dot(P)

    return f


def bezier3(P1, P2, P3, P4):
    M = np.array(
        [[-1, +3, -3, +1],
         [+3, -6, +3, 0],
         [-3, +3, 0, 0],
         [+1, 0, 0, 0]],
        dtype=np.float32
    )
    P = np.array([P1, P2, P3, P4], dtype=np.float32)

    def f(t):
        T = np.array([t ** 3, t ** 2, t, 1], dtype=np.float32)
        return T.dot(M).dot(P)

    return f


class Circle(AbstractShape):
    def __init__(self, cx: np.float32, cy: np.float32, radius: np.float32, noise: np.float32):
        self._radius = radius
        self._noise = noise
        self._cx = cx
        self._cy = cy

    def sample(self):
        w = np.random.random() * 2 * np.pi
        x = np.cos(w) * self._radius + self._cx
        x += np.random.randn() * self._noise
        y = np.sin(w) * self._radius + self._cy
        y += np.random.randn() * self._noise
        return x, y

    def contour(self, n: int):
        w = np.linspace(0, 2 * np.pi, num=n)
        x = np.cos(w) * self._radius + self._cx
        y = np.sin(w) * self._radius + self._cy
        xy = np.stack((x, y), axis=1)
        return xy

    def area(self):
        a = np.pi * self._radius ** 2
        return a


class BezierShape(AbstractShape):
    def __init__(self, knots, control, noise):
        self._knots = knots
        self._control = control
        self._noise = noise
        self._n = len(knots)

        self._fs = [
            bezier3(knots[i - 1], control[2 * i], control[2 * i + 1], knots[i])
            for i in range(self._n)
        ]

    def sample(self):
        i = np.random.randint(self._n)
        t = np.random.random()
        x, y = self._fs[i](t)
        x += np.random.randn() * self._noise
        y += np.random.randn() * self._noise
        return x, y


def noisy_circle(cx, cy, radius, noise) -> AbstractShape:
    return Circle(cx, cy, radius, noise).sample
