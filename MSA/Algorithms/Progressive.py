from MSA.Algorithms.Algorithm import Algorithm
from MSA.Algorithms.NWProf import NWProf
from PairAlign.Executer import Executer


class Progressive(Algorithm):
    """
    Class which implements user defined progressive, multiple sequence alignment algorithm
    """

    def __init__(self, sequences, order, match_score=1, mismatch_penalty=-1, gap_penalty=-1):
        self.sequences = sequences
        self.order = order
        self.len_seq = len(sequences)
        self.match_score = match_score
        self.mismatch_penalty = mismatch_penalty
        self.gap_penalty = gap_penalty
        self.alignments = []
        self.profiles = {}
        self.graph = {}
        self.identity = 0
        super().__init__()

    def initialize(self):
        for seq_i in range(self.len_seq):
            self.profiles[seq_i+1] = self.sequences[seq_i][:1000]

    def align(self):
        temp_prof_data = {}
        offset = 1
        for pair in self.order:
            seq_id1 = pair[0]
            seq_id2 = pair[1]
            seq1 = self.profiles[seq_id1]
            seq2 = self.profiles[seq_id2]
            children = []
            if isinstance(seq1, str):
                seq1 = [seq1]
                children.append({"id": seq_id1})
            else:
                children.append(temp_prof_data[seq_id1])
            if isinstance(seq2, str):
                seq2 = [seq2]
                children.append({"id": seq_id2})
            else:
                children.append(temp_prof_data[seq_id2])

            nw_prof_algorithm = NWProf(
                seq1, seq2, self.match_score, self.mismatch_penalty, self.gap_penalty)
            executer = Executer(nw_prof_algorithm)
            result = executer.get_results()
            align_a = result['alignments'][0]['algn_a']
            align_b = result['alignments'][0]['algn_b']
            prof = align_a + align_b
            self.profiles[offset + self.len_seq] = prof
            graph = {"id": offset + self.len_seq, "children": children}
            temp_prof_data[offset + self.len_seq] = graph
            offset += 1
        self.graph = graph
        self.alignments = prof

    def get_alignments(self) -> list:
        return {'alignments': self.alignments, 'graph': self.graph,
                'profiles': self.profiles, 'identity': self.identity}
