from Game.Games.Algorithm import Algorithm


class GameExecuter():
    def __init__(self, algorithm: Algorithm):
        self.algorithm = algorithm

    def get_results(self) -> dict:
        self.algorithm.calculate_score()
        score = self.algorithm.get_score()
        alignments = self.algorithm.get_align_result()
        return {'score': score, 'alignments': alignments}
