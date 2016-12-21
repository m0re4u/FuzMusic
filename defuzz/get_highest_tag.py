from preprocess.make_user_vectors import open_all_tags


def highest_tag(center_vec, user_vec, tag_file):
    A = center_vec - user_vec
    # Index of highest value in A
    maxi = A.argmax()
    tag = open_all_tags(tag_file)
    print("Highest tag was: {} with score {}".format(tag[maxi], A[maxi]))
    return (tag[maxi], A[maxi])
