# bpy24.py

import numpy as np
from PairAlign.Algorithms.Algorithm import Algorithm

class SW(Algorithm):
    LEFT = 1
    DIAGONAL = 2
    UP = 3

    def __init__(self, seq_a, seq_b, match_score=1, mismatch_penalty=-1, gap_penalty=-1):
        self.seq_a = seq_a
        self.seq_b = seq_b

        self.len_a = len(seq_a)
        self.len_b = len(seq_b)

        self.match_score = match_score
        self.mismatch_penalty = mismatch_penalty
        self.gap_penalty = gap_penalty
        self.algn_a = []
        self.algn_b = []
        self.score = 0
        self.max_score = 0
        self.max_i = []
        self.max_j = []
        self.identity = []
        self.traceback_path = []

        self.score_mat = np.zeros((self.len_a + 1, self.len_b + 1))
        self.direction_mat = np.empty((self.len_a + 1, self.len_b + 1), dtype=object)

    def initialize(self):
        self.direction_mat[0][0] = [0]

        for i in range(1, self.len_a + 1):
            self.direction_mat[i][0] = [0]

        for j in range(1, self.len_b + 1):
            self.direction_mat[0][j] = [0]

    def __similarity(self, a_i, b_i):
        if self.seq_a[a_i].upper() == self.seq_b[b_i].upper():
            return self.match_score
        else:
            return self.mismatch_penalty

    def calculate_score(self):
        for i in range(1, self.len_a + 1):
            for j in range(1, self.len_b + 1):
                match = self.score_mat[i - 1][j - 1] + self.__similarity(i - 1, j - 1)
                delete = self.score_mat[i - 1][j] + self.gap_penalty
                insert = self.score_mat[i][j - 1] + self.gap_penalty

                max_value = max(0, match, delete, insert)

                self.score_mat[i][j] = max_value
                self.direction_mat[i][j] = []
                if max_value == match:
                    self.direction_mat[i][j].append(self.DIAGONAL)
                if max_value == delete:
                    self.direction_mat[i][j].append(self.UP)
                if max_value == insert:
                    self.direction_mat[i][j].append(self.LEFT)
                if max_value == 0:
                    self.direction_mat[i][j].append(0)
                if max_value > self.max_score:
                    self.max_i = [i]
                    self.max_j = [j]
                    self.max_score = max_value
                elif max_value == self.max_score  and self.match_score != 0:
                    self.max_i.append(i)
                    self.max_j.append(j)

        self.score = int(self.score_mat[self.len_a][self.len_b])

    def traceback(self):
        for k in range(len(self.max_i)):
            i = self.max_i[k]
            j = self.max_j[k]
            self.algn_a.append('')
            self.algn_b.append('')
            self.traceback_path.append([])
            while (0 not in self.direction_mat[i][j]):
                self.traceback_path[k].append([i, j])

                if (self.DIAGONAL in self.direction_mat[i][j]):
                    self.algn_a[k] = self.seq_a[i - 1] + self.algn_a[k]
                    self.algn_b[k] = self.seq_b[j - 1] + self.algn_b[k]
                    i -= 1
                    j -= 1
                elif (self.UP in self.direction_mat[i][j]):
                    self.algn_a[k] = self.seq_a[i - 1] + self.algn_a[k]
                    self.algn_b[k] = '-' + self.algn_b[k]
                    i -= 1
                elif (self.LEFT in self.direction_mat[i][j]):
                    self.algn_b[k] = self.seq_b[j - 1] + self.algn_b[k]
                    self.algn_a[k] = '-' + self.algn_a[k]
                    j -= 1
    
    def calculate_identity(self):
        for k in range(len(self.max_i)):
            sym = ''
            iden = 0
            l = len(self.algn_a[k])
            for i in range(l):
                a1 = self.algn_a[k][i].upper() if self.algn_a[k][i] != '-' else '-'
                a2 = self.algn_b[k][i].upper() if self.algn_b[k][i] != '-' else '-'
                if a1 == a2:
                    sym += a1
                    iden += 1
                elif a1 != a2 and a1 != '-' and a2 != '-':
                    sym += ' '
                elif a1 == '-' or a2 == '-':
                    sym += ' '

            self.identity.append(iden / l)

    def get_alignments(self) -> list:
        res = []
        for k in range(len(self.max_i)):
            res.append({'path': self.traceback_path[k], 'algn_a': self.algn_a[k], 'algn_b': self.algn_b[k], 'identity': self.identity[k]})
        return res

    def get_score(self)-> int:
        return self.max_score

    def get_score_matrix(self) -> list:
        return self.score_mat.tolist()

    def get_direction_matrix(self) -> list:
        return self.direction_mat.tolist()
