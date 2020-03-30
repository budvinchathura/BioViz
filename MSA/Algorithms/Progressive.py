from MSA.Algorithms.Algorithm import Algorithm
from PairAlign.Algorithms.NW import NW
from PairAlign.Executer import Executer
from MSA.Algorithms.NWProf import NWProf


class Progressive(Algorithm):

    def __init__(self, sequences, match_score=1, mismatch_penalty=-1, gap_penalty=-1):
        self.sequences = sequences
        self.len_seq = len(sequences)
        self.match_score = match_score
        self.mismatch_penalty = mismatch_penalty
        self.gap_penalty = gap_penalty
        self.alignments = []
        self.identity = 0
        self.profiles = []
        self.intermediate_profs = {}

    def initialize(self):
        for seqi in range(self.len_seq):
            self.intermediate_profs[seqi] = self.sequences[seqi]

    def align(self):
        seq1 = self.sequences[0]
        prof = [seq1]
        children = [{"id" : 0}]
        for seqi in range(1, self.len_seq):
            seq = [self.sequences[seqi]]
            children.append({"id" : seqi})
            nw_prof_algorithm = NWProf(prof, seq, self.match_score, self.mismatch_penalty, self.gap_penalty)
            executer = Executer(nw_prof_algorithm)
            result = executer.get_results()
            align_a = result['alignments'][0]['algn_a']
            align_b = result['alignments'][0]['algn_b']
            prof = align_a + align_b
            self.intermediate_profs[seqi + self.len_seq -1] = prof
            prof_data = {"id": seqi + self.len_seq -1 , "Children" : children}
            children = [prof_data]
        self.profiles.append({'graph': prof_data, 'profiles': self.intermediate_profs})
        self.alignments = prof
        self.identity = result['alignments'][0]['identity']

    def get_alignments(self) -> list:
        return {'alignments': self.alignments, 'intermediate' :self.profiles, 'identity': self.identity}
