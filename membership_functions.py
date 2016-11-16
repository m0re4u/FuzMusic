import numpy as np


class Identity():
    """calculates the Identity function"""
    def calculate(self, x):
        return x


class Gaussian():
    """
    calculates the Gaussian function after setting mu and sigma
    TODO Check if this is function shows correct behaviour
    """
    def __init__(self, mu, sigma):
        self.mu = mu
        self.sigma = sigma

    def calculate(self, x):
        t = -np.power(x - self.mu, 2.) / (2 * np.power(self.sigma, 2.))
        return np.exp(t)


class Trapezoidial():
    """calculates the Trapezoidial function after setting a,b,c,d"""
    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def calculate(self, x):
        p = (x - self.a) / (self.b - self.a)
        q = (self.d - x) / (self.d - self.c)
        return max(min(p, 1, q), 0)


class LeftShoulder():
    """docstring for LeftShoulder"""
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def calculate(self, x):
        if (x <= self.a):
            return 1
        elif (self.a <= x <= self.b):
            return (self.b - x) / (self.b - self.a)
        elif (x > self.b):
            return 0


class RightShoulder():
    """docstring for RightShoulder"""
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def calculate(self, x):
        if (x <= self.a):
            return 0
        elif (self.a <= x <= self.b):
            return (x - self.a) / (b - self.a)
        elif (x > self.b):
            return 1
