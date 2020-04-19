from MSA.Algorithms.Algorithm import Algorithm
from MSA.Algorithms.NWProf import NWProf
from PairAlign.Executer import Executer


class Progressive(Algorithm):
    """
    Class which implements non optimal progressive, multiple sequence alignment algorithm
    """

    def __init__(self, sequences, match_score=1, mismatch_penalty=-1, gap_penalty=-1):
        self.sequences = sequences
        # self.len_seq = len(sequences)
        self.match_score = match_score
        self.mismatch_penalty = mismatch_penalty
        self.gap_penalty = gap_penalty
        self.alignments = []
        self.profiles = {}
        self.graph = {}
        self.identity = 0
        self.seq_i = 1
        self.prof_i = len(self.flatten(self.sequences)) + 1
        super().__init__()

    def initialize(self):
        self.sequences = self.lst2tuple(self.sequences)
        pass
        # for seq_i in range(self.len_seq):
        #     self.profiles[seq_i+1] = self.sequences[seq_i]

    # def align(self):
    #     seq1 = self.sequences[0]
    #     prof = [seq1]
    #     children = [{"id": 1}]
    #     for seqi in range(1, self.len_seq):
    #         seq = [self.sequences[seqi]]
    #         children.append({"id": seqi+1})
    #         nw_prof_algorithm = NWProf(
    #             prof, seq, self.match_score, self.mismatch_penalty, self.gap_penalty)
    #         executer = Executer(nw_prof_algorithm)
    #         result = executer.get_results()
    #         align_a = result['alignments'][0]['algn_a']
    #         align_b = result['alignments'][0]['algn_b']
    #         prof = align_a + align_b
    #         self.profiles[seqi + self.len_seq] = prof
    #         graph = {"id": seqi + self.len_seq, "children": children}
    #         children = [graph]
    #     self.graph = graph
    #     self.alignments = prof

    def align(self):
        # self.graph = graph
        self.alignments = self.flatten(self.alignmenthelper(self.sequences))

    def get_alignments(self) -> list:
        return {'alignments': self.alignments, 'graph': self.graph,
                'profiles': self.profiles, 'identity': self.identity}

    def flatten(self, lst):
        flattenedList = []
        for item in lst:
            if isinstance(item, list):
                flattenedList = flattenedList + self.flatten(item)
            else:
                flattenedList.append(item)
        return flattenedList

    def alignmenthelper(self, sequences):
        _0 = sequences[0]
        _1 = sequences[1]
        
        if isinstance(_0, tuple):
            _0 = self.alignmenthelper(_0)
        # elif isinstance(_0, list):
        #     print('flattened')
        #     _0 = flatten(_0)
        elif isinstance(_0, str):
            self.profiles[self.seq_i] = _0
            self.seq_i += 1
            _0 = [_0]
        if isinstance(_1, tuple):
            _1 = self.alignmenthelper(_1)
        # elif isinstance(_1, list):
        #     print('flattened')
        #     _1 = flatten(_1)
        elif isinstance(_1, str):
            self.profiles[self.seq_i] = _1
            self.seq_i += 1
            _1 = [_1]

        _0 = self.flatten(_0)
        _1 = self.flatten(_1)

        children = [{"id": self.seq_i - 1}, {"id": self.seq_i}]
        graph = {"id": self.prof_i, "children": children}

        nw_prof_algorithm = NWProf(
            _0, _1, 1, -1, -2)
        executer = Executer(nw_prof_algorithm)
        result = executer.get_results()
        align_a = result['alignments'][0]['algn_a']
        align_b = result['alignments'][0]['algn_b']

        prof = align_a + align_b
        self.profiles[self.prof_i] = prof
        self.prof_i += 1

        align_a = align_a[0] if len(align_a) == 1 else align_a
        align_b = align_b[0] if len(align_b) == 1 else align_b

        return([align_a, align_b])
    
    def lst2tuple(self, lst):
        return tuple(self.lst2tuple(i) if isinstance(i, list) else i for i in lst)