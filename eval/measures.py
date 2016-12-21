import numpy as np


def dot_product(album_vec, user_vec):
    print("shapes album {} user {}".format(album_vec.shape, user_vec.shape))
    nal = np.linalg.norm(album_vec)
    nuv = np.linalg.norm(user_vec)
    norm_album = album_vec / nal
    norm_user = user_vec / nuv
    return np.dot(norm_album, norm_user)
