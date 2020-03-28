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
        self.identity = 0
        self.traceback_path = []
        self.intermediate_profs = []

    def align(self):
        seq1 = self.sequences.pop(0)
        seq2 = self.sequences.pop(0)
        nw_algorithm = NW(seq1[:100],
                          seq2[:100], self.match_score, self.mismatch_penalty, self.gap_penalty)
        executer = Executer(nw_algorithm)
        result = executer.get_results()
        align_a = result['alignments'][0]['algn_a']
        align_b = result['alignments'][0]['algn_b']
        prof = [align_a, align_b]
        self.intermediate_profs.append(prof)
        for seq in self.sequences:
            nw_prof_algorithm = NWProf(prof,[seq],self.match_score, self.mismatch_penalty, self.gap_penalty)
            executer = Executer(nw_prof_algorithm)
            result = executer.get_results()
            align_a = result['alignments'][0]['algn_a']
            align_b = result['alignments'][0]['algn_b']
            prof = align_a + align_b
            self.intermediate_profs.append(prof)
        self.alignments = prof
        # self.traceback_path = result['alignments'][0]['path']
        self.identity = result['alignments'][0]['identity']

    def get_alignments(self) -> list:
        return {'alignments': self.alignments, 'intermediate' :self.intermediate_profs, 'identity': self.identity}
