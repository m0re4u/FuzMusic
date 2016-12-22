import random
from preprocess.make_user_vectors import open_all_tags


def highest_tag(center_vec, user_vec, tag_file):
    A = center_vec - user_vec
    # Indices of highest values in A
    max_indices = A.argsort()[::-1][:5]
    # Pick one of top 5
    random.seed()
    ri = random.randint(0, 4)
    # Return the right tag and its count
    maxi = max_indices[ri]
    tag = open_all_tags(tag_file)
    return (tag[maxi], A[maxi])
