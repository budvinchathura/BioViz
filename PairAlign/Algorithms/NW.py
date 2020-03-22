import numpy as np

def NW(seq_a, seq_b, match_score=1, mismatch_penalty=-1, gap_penalty=-1):
    LEFT = 1
    DIAGONAL = 2
    UP = 3

    def similarity(a, b):
        if seq_a[a] == seq_b[b]:
            return match_score
        else:
            return mismatch_penalty

    len_a = len(seq_a)
    len_b = len(seq_b)

    score_mat = np.zeros((len_a+1, len_b+1), dtype=np.int)
    direction_mat = np.empty((len_a+1, len_b+1), dtype=object)
    direction_mat[0][0] = [0]

    for i in range(1,len_a+1):
        score_mat[i][0] = gap_penalty*i
        direction_mat[i][0] = [UP]

    for j in range(1,len_b+1):
        score_mat[0][j] = gap_penalty*j
        direction_mat[0][j] = [LEFT]

    for i in range(1, len_a + 1):
        for j in range(1, len_b + 1):
            match = score_mat[i-1][j-1] + similarity(i-1, j-1)
            delete = score_mat[i-1][j] + gap_penalty
            insert = score_mat[i][j-1] + gap_penalty

            max_value = max(match, delete, insert)

            score_mat[i][j] = max_value
            direction_mat[i][j] = []
            if max_value == match:
                direction_mat[i][j].append(DIAGONAL)
            if max_value == delete:
                direction_mat[i][j].append(UP)
            if max_value == insert:
                direction_mat[i][j].append(LEFT)

    def generate_algns(i, j, algn_a, algn_b):
        while(i > 0 or j > 0):
            if(i > 0 and j > 0 and DIAGONAL in direction_mat[i][j]):
                algn_a = seq_a[i-1]+algn_a
                algn_b = seq_b[j-1]+algn_b
                i -= 1
                j -= 1
            elif(i > 0 and UP in direction_mat[i][j]):
                algn_a = seq_a[i-1]+algn_a
                algn_b = '-'+algn_b
                i -= 1
            elif(j > 0 and LEFT in direction_mat[i][j]):
                algn_a = '-'+algn_a
                algn_b = seq_b[j-1]+algn_b
                j -= 1
        return (algn_a, algn_b)

    algn_a = ""
    algn_b = ""

    i = len_a
    j = len_b

    algn_results = generate_algns(i, j, algn_a, algn_b)
    return (score_mat.tolist(),direction_mat.tolist(), algn_results[0], algn_results[1])
