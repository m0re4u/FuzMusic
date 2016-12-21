import numpy as np


def combine_fclusters(memberships, clusters):
    """
    Combine the fuzzy clusters into one vector that will act as a centroid
    """
    M = clusters * memberships
    return np.sum(M, axis=0)
