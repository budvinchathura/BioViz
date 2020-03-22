# bpy24.py

from __future__ import division, print_function
import numpy as np


# def mch(alpha, beta, match, mismatch, gap):
#     pt = {'match': match, 'mismatch': mismatch, 'gap': gap}
#     if alpha == beta:
#         return pt['match']
#     elif alpha == '-' or beta == '-':
#         return pt['gap']
#     else:
#         return pt['mismatch']


# def SW(s1, s2, match, mismatch, gap):
#     pt = {'match': match, 'mismatch': mismatch, 'gap': gap}

#     m, n = len(s1), len(s2)
#     H = np.zeros((m+1, n+1))
#     T = np.zeros((m+1, n+1))
#     max_score = 0

#     # Score, Pointer Matrix
#     for i in range(1, m + 1):
#         for j in range(1, n + 1):
#             sc_diag = H[i-1][j-1] + mch(s1[i-1], s2[j-1], match, mismatch, gap)
#             sc_up = H[i][j-1] + pt['gap']
#             sc_left = H[i-1][j] + pt['gap']
#             H[i][j] = max(0, sc_left, sc_up, sc_diag)
#             if H[i][j] == 0:
#                 T[i][j] = 0
#             if H[i][j] == sc_left:
#                 T[i][j] = 1
#             if H[i][j] == sc_up:
#                 T[i][j] = 2
#             if H[i][j] == sc_diag:
#                 T[i][j] = 3
#             if H[i][j] >= max_score:
#                 max_i = i
#                 max_j = j
#                 max_score = H[i][j]

#     align1, align2 = '', ''
#     i, j = max_i, max_j

#     # Traceback
#     while T[i][j] != 0:
#         if T[i][j] == 3:
#             a1 = s1[i-1]
#             a2 = s2[j-1]
#             i -= 1
#             j -= 1
#         elif T[i][j] == 2:
#             a1 = '-'
#             a2 = s2[j-1]
#             j -= 1
#         elif T[i][j] == 1:
#             a1 = s1[i-1]
#             a2 = '-'
#             i -= 1
#         align1 += a1
#         align2 += a2

#     align1 = align1[::-1]
#     align2 = align2[::-1]
#     sym = ''
#     iden = 0
#     for i in range(len(align1)):
#         a1 = align1[i]
#         a2 = align2[i]
#         if a1 == a2:
#             sym += a1
#             iden += 1
#         elif a1 != a2 and a1 != '-' and a2 != '-':
#             sym += ' '
#         elif a1 == '-' or a2 == '-':
#             sym += ' '

#     identity = iden / len(align1) * 100
#     # return [identity, max_score, align1, align2]
#     return (H.tolist(),T.tolist(), align1, align2)

# if __name__ == '__main__':
#     s1 = "TGTTACGG"
#     s2 = "GGTTGACTA"

#     max_score, align1, align2 = SW(s1, s2, 3, -3, 2)
#     print('Max Score = %d\n' % max_score)
#     print(align1)
#     print(align2)


# =================================================================================================



class SW(Algorithm):

    def __init__(self, seq_a, seq_b, match_score=1, mismatch_penalty=-1, gap_penalty=-1):
        self.seq_a = seq_a
        self.seq_b = seq_b

        self.len_a = len(seq_a)
        self.len_b = len(seq_b)
        
        self.match_score = match_score
        self.mismatch_penalty = mismatch_penalty
        self.gap_penalty = gap_penalty

        # final alignments
        self.algn_a = ''
        self.algn_b = ''

        # traceback matrix
        self.max_score = 0
        self.T=np.zeros((seq_a+1, seq_b+1))

        # ponter matrix of H
        self.H=np.zeros((seq_a+1, seq_b+1))
        self.max_i = 0
        self.max_j = 0

        self.sym = ''
        self.identity = 0



    def mch(alpha, beta):
        if alpha == beta:
            return self.match_score
        elif alpha == '-' or beta == '-':
            return self.gap_penalty
        else:
            return self.mismatch_penalty

# SW initialize score and ponter matrix
    def SW(self):
        # Score, Pointer Matrix
        for i in range(1, self.len_a + 1):
            for j in range(1, self.len_b + 1):
                sc_diag = H[i-1][j-1] + mch(self.seq_a[i-1], self.seq_b[j-1])
                sc_up = H[i][j-1] + self.gap_penalty
                sc_left = H[i-1][j] + self.gap_penalty
                H[i][j] = max(0, sc_left, sc_up, sc_diag)
                if H[i][j] == 0:
                    self.T[i][j] = 0
                if H[i][j] == sc_left:
                    self.T[i][j] = 1
                if H[i][j] == sc_up:
                    self.T[i][j] = 2
                if H[i][j] == sc_diag:
                    self.T[i][j] = 3
                if H[i][j] >= self.max_score:
                    max_i = i
                    max_j = j
                    self.max_score = H[i][j]


        self.max_i, self.max_j = max_i, max_j


    def traceback(self):
        i=self.max_i
        j=self.max_j
        
        while self.T[i][j] != 0:
            if self.T[i][j] == 3:
                a1 = self.seq_a[i-1]
                a2 = self.seq_b[j-1]
                i -= 1
                j -= 1
            elif self.T[i][j] == 2:
                a1 = '-'
                a2 = self.seq_b[j-1]
                j -= 1
            elif self.T[i][j] == 1:
                a1 = self.seq_a[i-1]
                a2 = '-'
                i -= 1
            self.algn_a += a1
            self.algn_b += a2

        self.algn_a = self.algn_a[::-1]
        self.algn_b = self.algn_b[::-1]
        
        
    def sym(self):   
        iden = 0 
        for i in range(len(self.algn_a)):
            a1 = self.algn_a[i]
            a2 = self.algn_b[i]
            if a1 == a2:
                self.sym += a1
                iden += 1
            elif a1 != a2 and a1 != '-' and a2 != '-':
                self.sym += ' '
            elif a1 == '-' or a2 == '-':
                self.sym += ' '

        self.identity = iden / len(self.algn_a) * 100

        # return [identity, max_score, align1, align2]
        # return (H.tolist(),self.T.tolist(), self.algn_a, self.algn_b)

    def get_alignments(self) -> list:
        return [{'path': self.T, 'algn_a': self.algn_a, 'algn_b': self.algn_b}]

    def get_max_score(self)-> int:
        return self.max_score

    def get_score_matrix(self) -> list:
        return self.T.tolist()

    def get_direction_matrix(self) -> list:
        return self.H.tolist()
