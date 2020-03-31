import numpy as np
from MSA.Algorithms.Algorithm import Algorithm
from PairAlign.Algorithms.NW import NW
from PairAlign.Executer import Executer
from MSA.Algorithms.NWProf import NWProf


class ProgressiveOptimal(Algorithm):

    def __init__(self, sequences, match_score=1, mismatch_penalty=-1, gap_penalty=-1):
        self.sequences = sequences
        self.len_seq = len(sequences)
        self.match_score = match_score
        self.mismatch_penalty = mismatch_penalty
        self.gap_penalty = gap_penalty
        self.alignments = []
        self.identity = 0
        self.profiles = {}
        self.graph = {}
        self.profiles = {}

    def initialize(self):
        for seqi in range(self.len_seq):
            self.profiles[seqi] = self.sequences[seqi]
            self.sequences[seqi] = [seqi, self.sequences[seqi]]            

    def align(self):
        l = self.len_seq
        x = 1
        temp_prof_data = {}
        while l > 1:
            similarity_matrix = np.zeros((l, l))
            for i in range(l):
                for j in range(i, l):
                    if i == j:
                        continue
                    nw_prof_algorithm = NWProf(self.sequences[i][1], self.sequences[j][1], self.match_score, self.mismatch_penalty, self.gap_penalty)
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
                seq1 = a[1] if isinstance(a[1], list) else [a[1]]
                seq2 = b[1] if isinstance(b[1], list) else [b[1]]
                seq_id1 = a[0]
                seq_id2 = b[0]
            else:
                b = self.sequences.pop(seq2i)
                a = self.sequences.pop(seq1i)
                seq2 = b[1] if isinstance(b[1], list) else [b[1]]
                seq1 = a[1] if isinstance(a[1], list) else [a[1]]
                seq_id1 = a[0]
                seq_id2 = b[0]
            if(len(seq1) == 1 and len(seq2) == 1):
                children = [{"id" : seq_id1}, {"id" : seq_id2}]
            elif(len(seq1) == 1 and len(seq2) != 1):
                children = [{"id" : seq_id1}, temp_prof_data[seq_id2]]
            elif(len(seq1) == 1 and len(seq2) != 1):
                children = [temp_prof_data[seq_id1], {"id" : seq_id2}]
            else:
                children = [temp_prof_data[seq_id1], temp_prof_data[seq_id2]]
            nw_prof_algorithm = NWProf(seq1, seq2, self.match_score, self.mismatch_penalty, self.gap_penalty)
            executer = Executer(nw_prof_algorithm)
            result = executer.get_results()
            align_a = result['alignments'][0]['algn_a']
            align_b = result['alignments'][0]['algn_b']
            prof = align_a + align_b
            self.profiles[x + self.len_seq -1] = prof
            graph = {"id": x + self.len_seq -1 , "children" : children}
            temp_prof_data[x + self.len_seq -1 ] = graph
            self.sequences.append([x + self.len_seq -1, prof])
            l = len(self.sequences)
            x += 1
        self.graph = graph
        self.alignments = prof
        self.identity = result['alignments'][0]['identity']

    def get_alignments(self) -> list:
        # self.get_order()
        return {'alignments': self.alignments,'graph': self.graph, 'profiles': self.profiles , 'identity': self.identity}

    def get_order(self):
        order = []
        for profile in self.xxxx:
            print(profile['graph'])