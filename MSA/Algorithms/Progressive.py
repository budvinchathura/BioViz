from MSA.Algorithms.Algorithm import Algorithm
from MSA.Algorithms.NWProf import NWProf
from PairAlign.Executer import Executer


class Progressive(Algorithm):
    """
    Class which implements non optimal progressive, multiple sequence alignment algorithm
    """

    def __init__(self, sequences, match_score=1, mismatch_penalty=-1, gap_penalty=-1):
        self.sequences = sequences
        self.len_seq = len(self.flatten(self.sequences))
        self.match_score = match_score
        self.mismatch_penalty = mismatch_penalty
        self.gap_penalty = gap_penalty
        self.alignments = []
        self.profiles = {}
        self.graph = {}
        self.identity = 0
        self.seq_i = 1
        self.prof_i = self.len_seq + 1
        self.temp_prof_data = {}
        self.order = []
        self.ordered_alignments = [''] * self.len_seq
        super().__init__()

    def initialize(self):
        self.sequences = self.lst2tuple(self.sequences)

    def align(self):
        self.alignments = self.flatten(self.alignmenthelper(self.sequences))

    def get_alignments(self) -> list:
        self.get_order(self.graph)
        self.rearrange()
        return {'alignments': self.alignments, 'graph': self.graph,
                'profiles': self.profiles, 'identity': self.identity}

    def flatten(self, lst):
        ''' To flatten the nested lists'''
        flattenedList = []
        for item in lst:
            if isinstance(item, list):
                flattenedList = flattenedList + self.flatten(item)
            else:
                flattenedList.append(item)
        return flattenedList

    def alignmenthelper(self, sequences):
        ''' Helper function to slign sequences in user selected order'''
        seq1 = sequences[0]
        seq2 = sequences[1]
        
        if isinstance(seq1, tuple):
            seq1 = self.alignmenthelper(seq1)
        if isinstance(seq2, tuple):
            seq2 = self.alignmenthelper(seq2)
        if isinstance(seq1, str):
            seq1_i = self.seq_i
            self.profiles[self.seq_i] = seq1
            self.seq_i += 1
            seq1 = [seq1]
        if isinstance(seq2, str):
            seq2_i = self.seq_i
            self.profiles[self.seq_i] = seq2
            self.seq_i += 1
            seq2 = [seq2]

        seq1 = self.flatten(seq1)
        seq2 = self.flatten(seq2)

        if(len(seq1) == 1 and len(seq2) == 1):
            children = [{"id": seq1_i}, {"id": seq2_i}]
        elif(len(seq1) == 1 and len(seq2) != 1):
            children = [{"id": seq1_i}, self.temp_prof_data[self.prof_i -1]]
        elif(len(seq1) != 1 and len(seq2) == 1):
            children = [self.temp_prof_data[self.prof_i - 1], {"id": seq2_i}]
        else:
            children = [self.temp_prof_data[self.prof_i - 1], self.temp_prof_data[self.prof_i - 2]]

        #get the alignment of selected sequences
        nw_prof_algorithm = NWProf(
            seq1, seq2, 1, -1, -2)
        executer = Executer(nw_prof_algorithm)
        result = executer.get_results()
        align_a = result['alignments'][0]['algn_a']
        align_b = result['alignments'][0]['algn_b']

        graph = {"id": self.prof_i, "children": children}
        self.temp_prof_data[self.prof_i] = graph
        prof = align_a + align_b
        self.profiles[self.prof_i] = prof
        self.prof_i += 1

        align_a = align_a[0] if len(align_a) == 1 else align_a
        align_b = align_b[0] if len(align_b) == 1 else align_b

        self.graph = graph
        return([align_a, align_b])
    
    def lst2tuple(self, lst):
        ''' Convert nested lists into nested tuples'''
        return tuple(self.lst2tuple(i) if isinstance(i, list) else i for i in lst)

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