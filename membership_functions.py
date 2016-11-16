import numpy as np


class IdentityFunction():
    """calculates the IdentityFunction"""
    def calculate(self, x):
        return x


class GaussianFunction():
    """calculates the GaussianFunction after setting mu and sigma"""
    def __init__(self, mu, sigma):
        self.mu = mu
        self.sigma = sigma

    def calculate(self, x):
        t = -np.power(x - self.mu, 2.) / (2 * np.power(self.sigma, 2.))
        return np.exp(t)
