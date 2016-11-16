class FuzzyVariable():
    """docstring for FuzzyVariable"""
    def __init__(self, terms, functions):
        self.fdict = {}
        for term, func in zip(terms, functions):
            self.fdict[term] = func
