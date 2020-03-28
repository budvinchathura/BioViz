import numpy as np
from MSA.Algorithms.Algorithm import Algorithm
from PairAlign.Algorithms.NW import NW
from PairAlign.Executer import Executer
from MSA.Algorithms.NWProf import NWProf


class ProgressiveOptimal(Algorithm):

    def __init__(self, sequences, match_score=1, mismatch_penalty=-1, gap_penalty=-1):
        self.sequences = sequences
        self.match_score = match_score
        self.mismatch_penalty = mismatch_penalty
        self.gap_penalty = gap_penalty
        self.alignments = []
        self.intermediate_profs = []
        self.identity = 0

    def align(self):
        l = len(self.sequences)
        while l > 1:
            similarity_matrix = np.zeros((l, l))
            for i in range(l):
                for j in range(i, l):
                    if i == j:
                        continue
                    nw_prof_algorithm = NWProf(self.sequences[i], self.sequences[j], self.match_score, self.mismatch_penalty, self.gap_penalty)
                    executer = Executer(nw_prof_algorithm)
                    result = executer.get_results()
                    similarity = result['alignments'][0]['identity']
                    similarity_matrix[i][j] = similarity
            seq1i, seq2i = np.where(
                similarity_matrix == np.amax(similarity_matrix))
            seq1i, seq2i = seq1i[0], seq2i[0]
            if seq1i > seq2i:
                a = self.sequences.pop(seq1i)
                b = self.sequences.pop(seq2i)
                seq1 = a if isinstance(a, list) else [a]
                seq2 = b if isinstance(b, list) else [b]
            else:
                b = self.sequences.pop(seq2i)
                a = self.sequences.pop(seq1i)
                seq2 = b if isinstance(b, list) else [b]
                seq1 = a if isinstance(a, list) else [a]
            nw_prof_algorithm = NWProf(seq1, seq2, self.match_score, self.mismatch_penalty, self.gap_penalty)
            executer = Executer(nw_prof_algorithm)
            result = executer.get_results()
            align_a = result['alignments'][0]['algn_a']
            align_b = result['alignments'][0]['algn_b']
            prof = align_a + align_b
            print(prof)
            self.intermediate_profs.append(prof)
            self.sequences.append(prof)
            l = len(self.sequences)
        self.alignments = prof
        self.identity = result['alignments'][0]['identity']

    def get_alignments(self) -> list:
        return {'alignments': self.alignments, 'intermediate' :self.intermediate_profs, 'identity': self.identity}
