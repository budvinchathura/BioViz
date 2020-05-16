import numpy as np

from PairAlign.Algorithms.Algorithm import Algorithm
from PairAlign.Algorithms.SubstitutionMatrix.subsMat import BLOSUM


class SWExtended(Algorithm):
    """
    Class for implementing SW algorithm with affine gap penalties
    and custom substitution matrix
    """
    LEFT = 1
    DIAGONAL = 2
    UP = 3

    def __init__(self, seq_type, sub_mat, seq_a, seq_b,
                 match_score=1, mismatch_penalty=-1, opening_gap_penalty=-1,
                 extending_gap_penalty=-1, priority='HIGHROAD'):
        self.seq_a = seq_a
        self.seq_b = seq_b

        self.len_a = len(seq_a)
        self.len_b = len(seq_b)

        self.seq_type = seq_type
        self.sub_mat = BLOSUM[sub_mat] if(self.seq_type == 'PROTEIN'
                                          and sub_mat != 'DEFAULT') else sub_mat

        self.priority = priority
        self.match_score = match_score
        self.mismatch_penalty = mismatch_penalty
        self.opening_gap_penalty = opening_gap_penalty
        self.extending_gap_penalty = extending_gap_penalty
        self.algn_a = []
        self.algn_b = []
        self.score = 0
        self.max_score = 0
        self.max_i = []
        self.max_j = []
        self.identity = []
        self.traceback_path = []

        self.score_mat = np.full(
            (self.len_a+1, self.len_b+1, 3), ['-inf', '-inf', '-inf'], dtype=object)
        self.direction_mat = np.empty(
            (self.len_a + 1, self.len_b + 1), dtype=object)

    def initialize(self):
        self.score_mat[0][0] = [0, 0, 0]

        for i in range(1, self.len_a + 1):
            self.score_mat[i][0][0] = 0
            self.direction_mat[i][0] = [[0], [0], [0]]

        for j in range(1, self.len_b + 1):
            self.score_mat[0][j][0] = 0
            self.direction_mat[0][j] = [[0], [0], [0]]

        self.direction_mat[0][0] = [[0], [0], [0]]

    def __similarity(self, a_i, b_i):
        if self.sub_mat == 'DEFAULT':
            if self.seq_a[a_i].upper() == self.seq_b[b_i].upper():
                return self.match_score
            return self.mismatch_penalty

        if self.seq_type == 'DNA':
            char1, char2 = (self.seq_a[a_i].upper(), self.seq_b[b_i].upper()) \
                if (self.seq_a[a_i] > self.seq_b[b_i]) else (self.seq_b[b_i].upper(), self.seq_a[a_i].upper())
            return int(self.sub_mat[char1+char2])
        if self.seq_type == 'PROTEIN':
            char1, char2 = (self.seq_a[a_i].upper(), self.seq_b[b_i].upper()) \
                if (self.seq_a[a_i], self.seq_b[b_i]) in self.sub_mat \
                else (self.seq_b[b_i].upper(), self.seq_a[a_i].upper())
            return self.sub_mat[(char1, char2)]

        raise ValueError('Invalid sub_mat type')

    def calculate_score(self):
        for i in range(1, self.len_a + 1):
            for j in range(1, self.len_b + 1):
                match = -np.inf if self.score_mat[i-1][j-1][0] == '-inf' \
                    else self.score_mat[i-1][j-1][0] + self.__similarity(i-1, j-1)
                insertion_1 = -np.inf if self.score_mat[i-1][j-1][1] == '-inf' \
                    else self.score_mat[i-1][j-1][1] + self.__similarity(i-1, j-1)
                insertion_2 = -np.inf if self.score_mat[i-1][j-1][2] == '-inf' \
                    else self.score_mat[i-1][j-1][2] + self.__similarity(i-1, j-1)

                open_gap_1 = -np.inf if self.score_mat[i-1][j][0] == '-inf' \
                    else self.score_mat[i-1][j][0] + self.opening_gap_penalty
                extend_gap_1 = -np.inf if self.score_mat[i-1][j][1] == '-inf' \
                    else self.score_mat[i-1][j][1] + self.extending_gap_penalty

                open_gap_2 = -np.inf if self.score_mat[i][j-1][0] == '-inf' \
                    else self.score_mat[i][j-1][0] + self.opening_gap_penalty
                extend_gap_2 = -np.inf if self.score_mat[i][j-1][2] == '-inf' \
                    else self.score_mat[i][j-1][2] + self.extending_gap_penalty

                max_1 = max(match, insertion_1, insertion_2, 0)
                max_2 = max(open_gap_1, extend_gap_1)
                max_3 = max(open_gap_2, extend_gap_2)

                max_value = ['-inf' if max_1 == -np.inf else max_1,
                             '-inf' if max_2 == -np.inf else max_2,
                             '-inf' if max_3 == -np.inf else max_3]

                self.score_mat[i][j] = max_value
                self.direction_mat[i][j] = [[], [], []]
                if max_value[0] == match:
                    self.direction_mat[i][j][0].append((0, self.DIAGONAL))
                if max_value[0] == insertion_1 and max_value[0] != -np.inf:
                    self.direction_mat[i][j][0].append((1, self.DIAGONAL))
                if max_value[0] == insertion_2 and max_value[0] != -np.inf:
                    self.direction_mat[i][j][0].append((2, self.DIAGONAL))
                if max_value[1] == open_gap_1 and max_value[1] != -np.inf:
                    self.direction_mat[i][j][1].append((0, self.UP))
                if max_value[1] == extend_gap_1 and max_value[1] != -np.inf:
                    self.direction_mat[i][j][1].append((1, self.UP))
                if max_value[2] == open_gap_2 and max_value[2] != -np.inf:
                    self.direction_mat[i][j][2].append((0, self.LEFT))
                if max_value[2] == extend_gap_2 and max_value[2] != -np.inf:
                    self.direction_mat[i][j][2].append((2, self.LEFT))
                if max_value[0] == 0:
                    self.direction_mat[i][j][0].append(0)
                if max_value[0] > self.max_score:
                    self.max_i = [i]
                    self.max_j = [j]
                    self.max_score = max_value[0]
                elif max_value[0] == self.max_score and self.match_score != 0:
                    self.max_i.append(i)
                    self.max_j.append(j)

        self.score = int(self.score_mat[self.len_a][self.len_b][0])

    def traceback(self):
        for k in range(len(self.max_i)):
            i = self.max_i[k]
            j = self.max_j[k]
            matrix_id = 0
            self.algn_a.append('')
            self.algn_b.append('')
            self.traceback_path.append([])
            end = False
            if self.priority == 'HIGHROAD':
                while True:
                    self.traceback_path[k].append([i, j, matrix_id])

                    if (0, self.UP) in self.direction_mat[i][j][matrix_id]:
                        self.algn_a[k] = self.seq_a[i - 1] + self.algn_a[k]
                        self.algn_b[k] = '-' + self.algn_b[k]
                        i -= 1
                        matrix_id = 0
                    elif (1, self.UP) in self.direction_mat[i][j][matrix_id]:
                        self.algn_a[k] = self.seq_a[i - 1] + self.algn_a[k]
                        self.algn_b[k] = '-' + self.algn_b[k]
                        i -= 1
                        matrix_id = 1
                    elif (1, self.DIAGONAL) in self.direction_mat[i][j][matrix_id]:
                        self.algn_a[k] = self.seq_a[i - 1] + self.algn_a[k]
                        self.algn_b[k] = self.seq_b[j - 1] + self.algn_b[k]
                        i -= 1
                        j -= 1
                        matrix_id = 1
                    elif (0, self.DIAGONAL) in self.direction_mat[i][j][matrix_id]:
                        self.algn_a[k] = self.seq_a[i - 1] + self.algn_a[k]
                        self.algn_b[k] = self.seq_b[j - 1] + self.algn_b[k]
                        i -= 1
                        j -= 1
                        matrix_id = 0
                    elif (2, self.DIAGONAL) in self.direction_mat[i][j][matrix_id]:
                        self.algn_a[k] = self.seq_a[i - 1] + self.algn_a[k]
                        self.algn_b[k] = self.seq_b[j - 1] + self.algn_b[k]
                        i -= 1
                        j -= 1
                        matrix_id = 2
                    elif (0, self.LEFT) in self.direction_mat[i][j][matrix_id]:
                        self.algn_b[k] = self.seq_b[j - 1] + self.algn_b[k]
                        self.algn_a[k] = '-' + self.algn_a[k]
                        j -= 1
                        matrix_id = 0
                    elif (2, self.LEFT) in self.direction_mat[i][j][matrix_id]:
                        self.algn_b[k] = self.seq_b[j - 1] + self.algn_b[k]
                        self.algn_a[k] = '-' + self.algn_a[k]
                        j -= 1
                        matrix_id = 2
                    if end:
                        break
                    if 0 in self.direction_mat[i][j][0]:
                        end = True
            elif self.priority == 'LOWROAD':
                while True:
                    self.traceback_path[k].append([i, j, matrix_id])

                    if (0, self.LEFT) in self.direction_mat[i][j][matrix_id]:
                        self.algn_b[k] = self.seq_b[j - 1] + self.algn_b[k]
                        self.algn_a[k] = '-' + self.algn_a[k]
                        j -= 1
                        matrix_id = 0
                    elif (2, self.LEFT) in self.direction_mat[i][j][matrix_id]:
                        self.algn_b[k] = self.seq_b[j - 1] + self.algn_b[k]
                        self.algn_a[k] = '-' + self.algn_a[k]
                        j -= 1
                        matrix_id = 2
                    elif (2, self.DIAGONAL) in self.direction_mat[i][j][matrix_id]:
                        self.algn_a[k] = self.seq_a[i - 1] + self.algn_a[k]
                        self.algn_b[k] = self.seq_b[j - 1] + self.algn_b[k]
                        i -= 1
                        j -= 1
                        matrix_id = 2
                    elif (0, self.DIAGONAL) in self.direction_mat[i][j][matrix_id]:
                        self.algn_a[k] = self.seq_a[i - 1] + self.algn_a[k]
                        self.algn_b[k] = self.seq_b[j - 1] + self.algn_b[k]
                        i -= 1
                        j -= 1
                        matrix_id = 0
                    elif (1, self.DIAGONAL) in self.direction_mat[i][j][matrix_id]:
                        self.algn_a[k] = self.seq_a[i - 1] + self.algn_a[k]
                        self.algn_b[k] = self.seq_b[j - 1] + self.algn_b[k]
                        i -= 1
                        j -= 1
                        matrix_id = 1
                    elif (0, self.UP) in self.direction_mat[i][j][matrix_id]:
                        self.algn_a[k] = self.seq_a[i - 1] + self.algn_a[k]
                        self.algn_b[k] = '-' + self.algn_b[k]
                        i -= 1
                        matrix_id = 0
                    elif (1, self.UP) in self.direction_mat[i][j][matrix_id]:
                        self.algn_a[k] = self.seq_a[i - 1] + self.algn_a[k]
                        self.algn_b[k] = '-' + self.algn_b[k]
                        i -= 1
                        matrix_id = 1
                    if end:
                        break
                    if 0 in self.direction_mat[i][j][0]:
                        end = True

    def calculate_identity(self):
        for k in range(len(self.max_i)):
            sym = ''
            iden = 0
            length = len(self.algn_a[k])
            for i in range(length):
                ch_1 = self.algn_a[k][i].upper() if self.algn_a[k][i] != '-' else '-'
                ch_2 = self.algn_b[k][i].upper() if self.algn_b[k][i] != '-' else '-'
                if ch_1 == ch_2:
                    sym += ch_1
                    iden += 1
                elif ch_1 != ch_2 and ch_1 != '-' and ch_2 != '-':
                    sym += ' '
                elif ch_1 == '-' or ch_2 == '-':
                    sym += ' '

            self.identity.append(iden / length)

    def get_alignments(self) -> list:
        res = []
        for k in range(len(self.max_i)):
            res.append({'path': self.traceback_path[k], 'algn_a': self.algn_a[k],
                        'algn_b': self.algn_b[k], 'identity': self.identity[k]})
        return res

    def get_score(self) -> int:
        return self.max_score

    def get_score_matrix(self) -> list:
        return self.score_mat.tolist()

    def get_direction_matrix(self) -> list:
        return self.direction_mat.tolist()
