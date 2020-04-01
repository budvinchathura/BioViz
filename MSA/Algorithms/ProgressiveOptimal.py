import numpy as np
from MSA.Algorithms.Algorithm import Algorithm
from MSA.Algorithms.NWProf import NWProf
from PairAlign.Executer import Executer


class ProgressiveOptimal(Algorithm):

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
        l = self.len_seq
        x = 1
        temp_prof_data = {}
        while l > 1:
            current_max_score = float('-inf')
            current_best_result = []
            current_best_pair = []
            for i in range(l):
                for j in range(i, l):
                    if i == j:
                        continue
                    nw_prof_algorithm = NWProf(
                        self.sequences[i][1], self.sequences[j][1], self.match_score, self.mismatch_penalty, self.gap_penalty)
                    executer = Executer(nw_prof_algorithm)
                    result = executer.get_results()
                    score = result['score']

                    if(score > current_max_score):
                        current_max_score = score
                        current_best_result = result
                        current_best_pair = [i, j]

            seq1i, seq2i = current_best_pair
            if seq1i > seq2i:
                a = self.sequences.pop(seq1i)
                b = self.sequences.pop(seq2i)
                seq1 = a[1]
                seq2 = b[1]
                seq_id1 = a[0]
                seq_id2 = b[0]
            else:
                b = self.sequences.pop(seq2i)
                a = self.sequences.pop(seq1i)
                seq2 = b[1]
                seq1 = a[1]
                seq_id1 = a[0]
                seq_id2 = b[0]
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
            self.profiles[x + self.len_seq] = prof
            graph = {"id": x + self.len_seq, "children": children}
            temp_prof_data[x + self.len_seq - 1] = graph
            self.sequences.append([x + self.len_seq - 1, prof])
            l = len(self.sequences)
            x += 1
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
            for g in graph['children']:
                self.get_order(g)
        else:
            self.order.append(graph['id'])
            return

    def rearrange(self):
        ''' Rearange output alignments in the order of input'''
        for i in range(self.len_seq):
            index = self.order[i]
            self.ordered_alignments[index-1] = self.alignments[i]
