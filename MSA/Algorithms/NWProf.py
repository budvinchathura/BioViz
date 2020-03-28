import numpy as np

class NWProf:

    LEFT = 1
    DIAGONAL = 2
    UP = 3

    def __init__(self, prof_a, prof_b, match_score=1, mismatch_penalty=-1, gap_penalty=-1):
        self.prof_a = prof_a
        self.prof_b = prof_b

        self.len_a = len(prof_a[0])
        self.len_b = len(prof_b[0])
        self.len_prof_a = len(prof_a)
        self.len_prof_b = len(prof_b)
        self.match_score = match_score
        self.mismatch_penalty = mismatch_penalty
        self.gap_penalty = gap_penalty
        self.algn_a = ''
        self.algn_b = ''
        self.score = 0
        self.identity = []
        self.traceback_path = []

        self.score_mat = np.zeros((self.len_a+1, self.len_b+1), dtype=np.int)
        self.direction_mat = np.empty(
            (self.len_a+1, self.len_b+1), dtype=object)

    def initialize(self):
        self.direction_mat[0][0] = [0]

        for i in range(1, self.len_a+1):
            self.score_mat[i][0] = self.gap_penalty*i
            self.direction_mat[i][0] = [self.UP]

        for j in range(1, self.len_b+1):
            self.score_mat[0][j] = self.gap_penalty*j
            self.direction_mat[0][j] = [self.LEFT]

    def __similarity(self, a_i, b_i):
        score = 0
        for i in range(self.len_prof_a):
            for j in range(self.len_prof_b):
                if self.prof_a[i][a_i] == self.prof_b[j][b_i]:
                    score += self.match_score
                else:
                    score += self.mismatch_penalty
        return score

    def calculate_score(self):
        for i in range(1, self.len_a + 1):
            for j in range(1, self.len_b + 1):
                match = self.score_mat[i-1][j-1] + self.__similarity(i-1, j-1)
                delete = self.score_mat[i-1][j] + self.gap_penalty
                insert = self.score_mat[i][j-1] + self.gap_penalty

                max_value = max(match, delete, insert)

                self.score_mat[i][j] = max_value
                self.direction_mat[i][j] = []
                if max_value == match:
                    self.direction_mat[i][j].append(self.DIAGONAL)
                if max_value == delete:
                    self.direction_mat[i][j].append(self.UP)
                if max_value == insert:
                    self.direction_mat[i][j].append(self.LEFT)

        self.score = int(self.score_mat[self.len_a][self.len_b])

    def traceback(self):
        i = self.len_a
        j = self.len_b
        while(i > 0 or j > 0):
            self.traceback_path.append([i, j])

            if(i > 0 and j > 0 and self.DIAGONAL in self.direction_mat[i][j]):
                self.algn_a = self.prof_a[0][i-1]+self.algn_a
                self.algn_b = self.prof_b[0][j-1]+self.algn_b
                i -= 1
                j -= 1
            elif(i > 0 and self.UP in self.direction_mat[i][j]):
                self.algn_a = self.prof_a[0][i-1]+self.algn_a
                self.algn_b = '-'+self.algn_b
                i -= 1
            elif(j > 0 and self.LEFT in self.direction_mat[i][j]):
                self.algn_a = '-'+self.algn_a
                self.algn_b = self.prof_b[0][j-1]+self.algn_b
                j -= 1

    def calculate_identity(self):
        sym = ''
        iden = 0
        l = len(self.algn_a)
        for i in range(l):
            a1 = self.algn_a[i]
            a2 = self.algn_b[i]
            if a1 == a2:
                sym += a1
                iden += 1
            elif a1 != a2 and a1 != '-' and a2 != '-':
                sym += ' '
            elif a1 == '-' or a2 == '-':
                sym += ' '

        self.identity = iden / l

    def get_alignments(self) -> list:
        return [{'path': self.traceback_path, 'algn_a': self.algn_a, 'algn_b': self.algn_b, 'identity': self.identity}]

    def get_score(self) -> int:
        return self.score

    def get_score_matrix(self) -> list:
        return self.score_mat.tolist()

    def get_direction_matrix(self) -> list:
        return self.direction_mat.tolist()
