import numpy as np

from PairAlign.Algorithms.SubstitutionMatrix.substitution_matrices import BLOSUM


class NWProf:
    """
    Helper Class for alignining two profiles with NW algorithm
    """

    LEFT = 1
    DIAGONAL = 2
    UP = 3

    def __init__(self, seq_type, sub_mat, prof_a, prof_b,
                 match_score=1, mismatch_penalty=-1, gap_penalty=-1):
        self.prof_a = prof_a
        self.prof_b = prof_b

        self.len_a = len(prof_a[0])
        self.len_b = len(prof_b[0])
        self.len_prof_a = len(prof_a)
        self.len_prof_b = len(prof_b)

        self.seq_type = seq_type
        self.sub_mat = BLOSUM[sub_mat] if(self.seq_type == 'PROTEIN'
                                          and sub_mat != 'DEFAULT') else sub_mat

        self.match_score = match_score
        self.mismatch_penalty = mismatch_penalty
        self.gap_penalty = gap_penalty
        self.algn_a = [''] * self.len_prof_a
        self.algn_b = [''] * self.len_prof_b
        self.score = 0
        self.traceback_path = []

        self.score_mat = np.zeros((self.len_a+1, self.len_b+1), dtype=np.int)
        self.direction_mat = np.empty(
            (self.len_a+1, self.len_b+1), dtype=object)

    def initialize(self):
        """
        Initializes matrices
        """
        self.direction_mat[0][0] = [0]

        for i in range(1, self.len_a+1):
            self.score_mat[i][0] = self.score_mat[i-1][0] + \
                self.__gap_similarity('a', i-1)
            self.direction_mat[i][0] = [self.UP]

        for j in range(1, self.len_b+1):
            self.score_mat[0][j] = self.score_mat[0][j-1] + \
                self.__gap_similarity('b', j-1)
            self.direction_mat[0][j] = [self.LEFT]

    def __gap_similarity(self, prof_selector, idx):
        score = 0
        prof = []
        if prof_selector == 'a':
            prof = self.prof_a
        else:
            prof = self.prof_b
        for seq in prof:
            character = seq[idx]
            if character == '-':
                score += self.match_score * len(prof)
            else:
                score += self.gap_penalty * len(prof)

        return score

    def __similarity(self, a_i, b_i):
        score = 0
        if self.sub_mat == 'DEFAULT':
            for i in range(self.len_prof_a):
                for j in range(self.len_prof_b):
                    if self.prof_a[i][a_i] == '-' or self.prof_b[j][b_i] == '-':
                        score += self.gap_penalty
                    elif self.prof_a[i][a_i].upper() == self.prof_b[j][b_i].upper():
                        score += self.match_score
                    else:
                        score += self.mismatch_penalty

        elif self.seq_type == 'DNA':
            for i in range(self.len_prof_a):
                for j in range(self.len_prof_b):
                    if self.prof_a[i][a_i] == '-' or self.prof_b[j][b_i] == '-':
                        score += self.gap_penalty
                    else:
                        char1, char2 = (self.prof_a[i][a_i].upper(), self.prof_b[j][b_i].upper()) \
                            if (self.prof_a[i][a_i].upper() > self.prof_b[j][b_i].upper()) \
                            else (self.prof_b[j][b_i].upper(), self.prof_a[i][a_i].upper())
                        score += self.sub_mat[char1+char2]

        elif self.seq_type == 'PROTEIN':
            for i in range(self.len_prof_a):
                for j in range(self.len_prof_b):
                    if self.prof_a[i][a_i] == '-' or self.prof_b[j][b_i] == '-':
                        score += self.gap_penalty
                    else:
                        char1, char2 = (self.prof_a[i][a_i].upper(), self.prof_b[j][b_i].upper()) \
                            if (self.prof_a[i][a_i].upper(), self.prof_b[j][b_i].upper()) \
                            in self.sub_mat \
                            else (self.prof_b[j][b_i].upper(), self.prof_a[i][a_i].upper())
                        score += self.sub_mat[(char1, char2)]

        return score

    def calculate_score(self):
        """
        Fills DP score matrix
        """
        for i in range(1, self.len_a + 1):
            for j in range(1, self.len_b + 1):
                match = self.score_mat[i-1][j-1] + self.__similarity(i-1, j-1)
                delete = self.score_mat[i-1][j] + \
                    self.__gap_similarity('a', i-1)
                insert = self.score_mat[i][j-1] + \
                    self.__gap_similarity('b', j-1)

                max_value = max(match, delete, insert)

                self.score_mat[i][j] = max_value
                self.direction_mat[i][j] = []
                if max_value == match:
                    self.direction_mat[i][j].append(self.DIAGONAL)
                if max_value == delete:
                    self.direction_mat[i][j].append(self.UP)
                if max_value == insert:
                    self.direction_mat[i][j].append(self.LEFT)

        self.score = int(
            self.score_mat[self.len_a][self.len_b])/(self.len_prof_a*self.len_prof_b)

    def traceback(self):
        """
        Finds traceback path using score matrix and direction matrix
        """
        i = self.len_a
        j = self.len_b
        while(i > 0 or j > 0):
            self.traceback_path.append([i, j])

            if(i > 0 and j > 0 and self.DIAGONAL in self.direction_mat[i][j]):
                for k in range(self.len_prof_a):
                    self.algn_a[k] = self.prof_a[k][i-1]+self.algn_a[k]
                for k in range(self.len_prof_b):
                    self.algn_b[k] = self.prof_b[k][j-1]+self.algn_b[k]
                i -= 1
                j -= 1
            elif(i > 0 and self.UP in self.direction_mat[i][j]):
                for k in range(self.len_prof_a):
                    self.algn_a[k] = self.prof_a[k][i-1]+self.algn_a[k]
                for k in range(self.len_prof_b):
                    self.algn_b[k] = '-'+self.algn_b[k]
                i -= 1
            elif(j > 0 and self.LEFT in self.direction_mat[i][j]):
                for k in range(self.len_prof_a):
                    self.algn_a[k] = '-'+self.algn_a[k]
                for k in range(self.len_prof_b):
                    self.algn_b[k] = self.prof_b[k][j-1]+self.algn_b[k]
                j -= 1

    def calculate_identity(self):
        """
        Calculates identity(similarity) in the final alignment
        """

    def get_alignments(self) -> list:
        """
        Returns final alignment results
        """
        return [{'path': self.traceback_path, 'algn_a': self.algn_a,
                 'algn_b': self.algn_b}]

    def get_score(self) -> int:
        """
        Returns final score
        """
        return self.score

    def get_score_matrix(self) -> list:
        """
        Returns DP score matrix
        """
        return self.score_mat.tolist()

    def get_direction_matrix(self) -> list:
        """
        Returns the direction matrix which has the way each value was calculated
        """
        return self.direction_mat.tolist()
