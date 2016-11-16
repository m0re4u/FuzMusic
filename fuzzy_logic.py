import argparse
import numpy as np
import fuzzy_variable as fv
import membership_functions as mf


def fuzzify(inputs):
    for fname, fuzv, value in inputs:
        for key in fuzv.fdict.keys():
            res = fuzv.fdict[key].calculate(value)
            print("Value for {} term {} is {}".format(fname, key, res))


def main():
    # TODO: Domain specify and processing everything outside the domain
    exam = fv.FuzzyVariable(['fail', 'pass', 'excellent'], [
            mf.LeftShoulder(0, 0.55),
            mf.Trapezoidial(0.4, 0.5, 0.6, 0.7),
            mf.RightShoulder(0.6, 1)
        ])
    perf = fv.FuzzyVariable(['low', 'medium', 'high'], [
            mf.LeftShoulder(0, 0.45),
            mf.Trapezoidial(0.3, 0.5, 0.7, 0.9),
            mf.RightShoulder(0.75, 1)
        ])
    fuz = fuzzify([('exam', exam, 0.1), ('perf', perf, 0.2)])

if __name__ == '__main__':
    main()
