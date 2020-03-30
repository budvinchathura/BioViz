from MSA.Algorithms.Algorithm import Algorithm


class Executer():
    def __init__(self, algorithm: Algorithm):
        self.algorithm = algorithm

    def get_results(self) -> dict:
        self.algorithm.initialize()
        self.algorithm.align()
        alignments = self.algorithm.get_alignments()
        return alignments
