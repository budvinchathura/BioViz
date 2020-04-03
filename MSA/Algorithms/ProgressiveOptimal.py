from MSA.Algorithms.Algorithm import Algorithm
from MSA.Algorithms.NWProf import NWProf
from PairAlign.Executer import Executer


class ProgressiveOptimal(Algorithm):
    """
    Algorithm class for executing optimal progressive MSA algorithm
    """

    def __init__(self, sequences, match_score=1, mismatch_penalty=-1, gap_penalty=-1):
        self.sequences = sequences
        self.len_seq = len(sequences)
        self.match_score = match_score
        self.mismatch_penalty = mismatch_penalty
        self.gap_penalty = gap_penalty
        self.alignments = []
        self.profiles = {}
        self.graph = {}
        self.identity = 0
        self.order = []
        self.ordered_alignments = [''] * self.len_seq
        super().__init__()

    def initialize(self):
        for seqi in range(self.len_seq):
            self.profiles[seqi+1] = self.sequences[seqi]
            self.sequences[seqi] = [seqi, [self.sequences[seqi]]]

    def align(self):
        remaining = self.len_seq
        offset = 1
        temp_prof_data = {}
        while remaining > 1:
            current_max_score = float('-inf')
            current_best_result = []
            current_best_pair = []
            for i in range(remaining):
                for j in range(i, remaining):
                    if i == j:
                        continue
                    nw_prof_algorithm = NWProf(
                        self.sequences[i][1], self.sequences[j][1],
                        self.match_score, self.mismatch_penalty, self.gap_penalty)
                    executer = Executer(nw_prof_algorithm)
                    result = executer.get_results()
                    score = result['score']

                    if score > current_max_score:
                        current_max_score = score
                        current_best_result = result
                        current_best_pair = [i, j]

            seq1i, seq2i = current_best_pair
            if seq1i > seq2i:
                temp_a = self.sequences.pop(seq1i)
                temp_b = self.sequences.pop(seq2i)
                seq1 = temp_a[1]
                seq2 = temp_b[1]
                seq_id1 = temp_a[0]
                seq_id2 = temp_b[0]
            else:
                temp_b = self.sequences.pop(seq2i)
                temp_a = self.sequences.pop(seq1i)
                seq2 = temp_b[1]
                seq1 = temp_a[1]
                seq_id1 = temp_a[0]
                seq_id2 = temp_b[0]
            if(len(seq1) == 1 and len(seq2) == 1):
                children = [{"id": seq_id1+1}, {"id": seq_id2+1}]
            elif(len(seq1) == 1 and len(seq2) != 1):
                children = [{"id": seq_id1+1}, temp_prof_data[seq_id2]]
            elif(len(seq1) != 1 and len(seq2) == 1):
                children = [temp_prof_data[seq_id1], {"id": seq_id2+1}]
            else:
                children = [temp_prof_data[seq_id1], temp_prof_data[seq_id2]]
            # nw_prof_algorithm = NWProf(
            #     seq1, seq2, self.match_score, self.mismatch_penalty, self.gap_penalty)
            # executer = Executer(nw_prof_algorithm)
            # result = executer.get_results()
            align_a = current_best_result['alignments'][0]['algn_a']
            align_b = current_best_result['alignments'][0]['algn_b']
            prof = align_a + align_b
            self.profiles[offset + self.len_seq] = prof
            graph = {"id": offset + self.len_seq, "children": children}
            temp_prof_data[offset + self.len_seq - 1] = graph
            self.sequences.append([offset + self.len_seq - 1, prof])
            remaining = len(self.sequences)
            offset += 1
        self.graph = graph
        self.alignments = prof

    def get_alignments(self) -> list:
        self.get_order(self.graph)
        self.rearrange()
        return {'alignments': self.ordered_alignments, 'graph': self.graph,
                'profiles': self.profiles, 'identity': self.identity}

    def get_order(self, graph):
        '''Get order of calculated aligngments vs input'''
        if 'children' in graph:
            for i in graph['children']:
                self.get_order(i)
        else:
            self.order.append(graph['id'])
            return

    def rearrange(self):
        ''' Rearange output alignments in the order of input'''
        for i in range(self.len_seq):
            index = self.order[i]
            self.ordered_alignments[index-1] = self.alignments[i]
