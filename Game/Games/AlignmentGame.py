class AlignmentGame():
    def __init__(self,algn_a, algn_b, match_score=1, mismatch_penalty=-1, gap_penalty=-1):
        self.algn_a = algn_a
        self.algn_b = algn_b
        self.min_length = min(len(algn_a),len(algn_b))
        self.max_length = max(len(algn_a),len(algn_b))
        self.match_score = match_score
        self.mismatch_penalty = mismatch_penalty
        self.gap_penalty = gap_penalty
        self.align_result = []
        self.score = 0

    def calculate_score(self):
        for i in range(self.min_length):
            if self.algn_a[i]=='-' or self.algn_b[i]=='-':
                self.score+=self.gap_penalty
                self.align_result.append('gap')
            elif self.algn_a[i] == self.algn_b[i]:
                self.score+=self.match_score
                self.align_result.append('mismatch')

            else:
                self.score+=self.mismatch_penalty
                self.align_result.append('match')

    def get_score(self):
        return self.score
    
    def get_align_result(self):
        return self.align_result



