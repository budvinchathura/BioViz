from MSA.Algorithms.Algorithm import Algorithm


class Executer():
    """
    This Class calls the methods of relevant algorithm in specified order.
    """

    def __init__(self, algorithm: Algorithm):
        self.algorithm = algorithm

    def get_results(self) -> dict:
        """
        Returns results from relevant MSA algorithm.
        """
        self.algorithm.initialize()
        self.algorithm.align()
        self.algorithm.calculate_identity()
        alignments = self.algorithm.get_alignments()
        return alignments
