from MSA.Algorithms.Algorithm import Algorithm
from PairAlign.Algorithms.NW import NW
from PairAlign.Executer import Executer


class Progressive(Algorithm):

    def __init__(self, sequences, match_score=1, mismatch_penalty=-1, gap_penalty=-1):
        self.sequences = sequences
        self.match_score = match_score
        self.mismatch_penalty = mismatch_penalty
        self.gap_penalty = gap_penalty
        self.alignments = []

    def initialize(self):
        self.sequences.sort(key=lambda x: -len(x))

    def align(self):
        seq1 = self.sequences.pop(0)
        seq2 = self.sequences.pop(0)
        nw_algorithm = NW(seq1[:100],
                          seq2[:100], self.match_score, self.mismatch_penalty, self.gap_penalty)
        executer = Executer(nw_algorithm)
        result = executer.get_results()
        align_a = result['alignments'][0]['algn_a']
        align_b = result['alignments'][0]['algn_b']
        self.alignments.append(align_a)
        self.alignments.append(align_b)
        for seq in self.sequences:
            nw_algorithm = NW(align_a[:100],
                              seq, self.match_score, self.mismatch_penalty, self.gap_penalty)
            executer = Executer(nw_algorithm)
            result = executer.get_results()
            align_b = result['alignments'][0]['algn_b']
            self.alignments.append(align_b)

    def get_alignments(self) -> list:
        return self.alignments
