from MSA.Algorithms.Algorithm import Algorithm
from PairAlign.Algorithms.NW import NW
from PairAlign.Executer import Executer
from MSA.Algorithms.NWProf import NWProf


class Progressive(Algorithm):

    def __init__(self, sequences, match_score=1, mismatch_penalty=-1, gap_penalty=-1):
        self.sequences = sequences
        self.match_score = match_score
        self.mismatch_penalty = mismatch_penalty
        self.gap_penalty = gap_penalty
        self.alignments = []

    def initialize(self):
        for i in range(len(self.sequences)):
           self.sequences[i] = [self.sequences[i], str(i)]
        self.sequences.sort(key=lambda x: -len(x[0]))

    def align(self):
        seq1 = self.sequences.pop(0)
        seq2 = self.sequences.pop(0)
        seq1i = seq1[1]
        seq2i = seq2[1]
        seq1 = seq1[0]
        seq2 = seq2[0]
        nw_algorithm = NW(seq1[:100],
                          seq2[:100], self.match_score, self.mismatch_penalty, self.gap_penalty)
        executer = Executer(nw_algorithm)
        result = executer.get_results()
        align_a = result['alignments'][0]['algn_a']
        align_b = result['alignments'][0]['algn_b']
        self.alignments.append([align_a, seq1i])
        self.alignments.append([align_b, seq2i])
        for seq in self.sequences:
            seqi = seq[1]
            seq = seq[0]
            nw_prof_algorithm = NWProf([align_a, align_b],[seq],self.match_score, self.mismatch_penalty, self.gap_penalty)
            executer = Executer(nw_prof_algorithm)
            result = executer.get_results()
            align_a = result['alignments'][0]['algn_a']
            align_b = result['alignments'][0]['algn_b']
            # self.alignments.append(align_a)
            self.alignments.append([align_b, seqi])

    def get_alignments(self) -> list:
        self.alignments.sort(key=lambda x: x[1])
        for i in range(len(self.alignments)):
            self.alignments[i] = self.alignments[i][0]
        return self.alignments
