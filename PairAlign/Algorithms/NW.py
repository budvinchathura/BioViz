import numpy as np


def NW(seq_a, seq_b, match_score=1, mismatch_penalty=-1, gap_penalty=-1):

    def similarity(a, b):
        if seq_a[a] == seq_b[b]:
            return match_score
        else:
            return mismatch_penalty

    len_a = len(seq_a)
    len_b = len(seq_b)

    score_mat = np.zeros((len_a+1, len_b+1), dtype=np.int)

    for i in range(len_a+1):
        score_mat[i][0] = gap_penalty*i

    for j in range(len_b+1):
        score_mat[0][j] = gap_penalty*j

    for i in range(1, len_a + 1):
        for j in range(1, len_b + 1):
            match = score_mat[i-1][j-1] + similarity(i-1, j-1)
            delete = score_mat[i-1][j] + gap_penalty
            insert = score_mat[i][j-1] + gap_penalty
            score_mat[i][j] = max(match, delete, insert)

    def generate_algns(i, j, algn_a, algn_b):
        while(i > 0 or j > 0):
            if(i > 0 and j > 0 and score_mat[i][j] == score_mat[i-1][j-1] + similarity(i-1, j-1)):
                algn_a = seq_a[i-1]+algn_a
                algn_b = seq_b[j-1]+algn_b
                i -= 1
                j -= 1
            if(i > 0 and score_mat[i][j] == score_mat[i-1][j] + gap_penalty):
                algn_a = seq_a[i-1]+algn_a
                algn_b = '-'+algn_b
                i -= 1
            if(j > 0 and score_mat[i][j] == score_mat[i][j-1] + gap_penalty):
                algn_a = '-'+algn_a
                algn_b = seq_b[j-1]+algn_b
                j -= 1
        return (algn_a, algn_b)

    algn_a = ""
    algn_b = ""

    i = len_a
    j = len_b

    algn_results = generate_algns(i, j, algn_a, algn_b)
    return (score_mat.tolist(), algn_results[0], algn_results[1])
