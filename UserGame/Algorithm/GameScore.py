# for both NW & SW 

def GameScore(seq_a, seq_b, match_score=1, mismatch_penalty=-1, gap_penalty=-1):
    l1 = len(seq_a)
    l2 = len(seq_b)

    min_eliment= min(l1,l2)
    max_eliment= max(l1,l2)

    score = 0
    for i in range(min_eliment):
        if(seq_a[i] == seq_b[i]):
           score+=match_score
        else:
            score+=mismatch_penalty
    score+= (max_eliment-min_eliment)*gap_penalty
    return score
        
if __name__ == '__main__':
    score =GameScore('GCATG-CU', 'G-ATTACA', 1, -1, -1)
    print (score)    
