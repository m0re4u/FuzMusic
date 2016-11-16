import argparse
import numpy as np
import fuzzy_variable as fv
import membership_functions as mf


def fuzzify(inputs):
    for fuzv, value in inputs:
        for key in fuzv.fdict.keys():
            res = fuzv.fdict[key].calculate(value)
            print("Value for term {} is {}".format(key, res))


def main():
    input_vector = np.array([0.1])
    exam = fv.FuzzyVariable(['fail', 'pass', 'excellent'], [
            mf.IdentityFunction(),
            mf.GaussianFunction(1, 1),
            mf.IdentityFunction()
        ])
    perf = fv.FuzzyVariable(['low', 'medium', 'high'], [
            mf.IdentityFunction(),
            mf.IdentityFunction(),
            mf.IdentityFunction()
        ])
    fuz = fuzzify([(exam, 0.1), (perf, 0.2)])

if __name__ == '__main__':
    main()
