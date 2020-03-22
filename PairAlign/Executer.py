from PairAlign.Algorithms.Algorithm import Algorithm


class Executer():
    def __init__(self, algorithm: Algorithm):
        self.algorithm = algorithm

    def get_results(self) -> dict:
        self.algorithm.initialize()
        self.algorithm.calculate_score()
        self.algorithm.traceback()
        alignments = self.algorithm.get_alignments()
        score = self.algorithm.get_score()
        score_mat = self.algorithm.get_score_matrix()
        direction_mat = self.algorithm.get_direction_matrix()
        return {'score': score, 'alignments': alignments,'score_matrix':score_mat,'direction_matrix':direction_mat}
