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
        self.graph = {}
        self.profiles = {}

    def initialize(self):
        for seqi in range(self.len_seq):
            self.profiles[seqi+1] = self.sequences[seqi]

    def align(self):
        seq1 = self.sequences[0]
        prof = [seq1]
        children = [{"id" : 1}]
        for seqi in range(1, self.len_seq):
            seq = [self.sequences[seqi]]
            children.append({"id" : seqi+1})
            nw_prof_algorithm = NWProf(prof, seq, self.match_score, self.mismatch_penalty, self.gap_penalty)
            executer = Executer(nw_prof_algorithm)
            result = executer.get_results()
            align_a = result['alignments'][0]['algn_a']
            align_b = result['alignments'][0]['algn_b']
            prof = align_a + align_b
            self.profiles[seqi + self.len_seq -1] = prof
            graph = {"id": seqi + self.len_seq , "children" : children}
            children = [graph]
        self.graph = graph
        self.alignments = prof
        self.identity = result['alignments'][0]['identity']

    def get_alignments(self) -> list:
        return {'alignments': self.alignments,'graph': self.graph, 'profiles': self.profiles , 'identity': self.identity}
