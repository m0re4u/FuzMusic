import numpy as np


def dot_product(album_vec, user_vec):
    """
    Cosine similarity between two vectors
    """
    nal = np.linalg.norm(album_vec)
    nuv = np.linalg.norm(user_vec)
    if nal == 0:
        norm_album = album_vec
    else:
        norm_album = album_vec / nal
    if nuv == 0:
        norm_user = user_vec
    else:
        norm_user = user_vec / nuv

    return np.dot(norm_album, norm_user)


def euclidean_dist(album_vec, user_vec):
    """
    Euclidean distance between two vectors
    """
    return np.linalg.norm(album_vec-user_vec)
