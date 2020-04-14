class AlignmentGame():
    def __init__(self,algn_a, algn_b, match_score=1, mismatch_penalty=-1, gap_penalty=-1):
        self.algn_a = algn_a
        self.algn_b = algn_b
        self.min_length = min(len(algn_a),len(algn_b))
        self.max_length = max(len(algn_a),len(algn_b))
        self.diference= self.max_length-self.min_length
        self.match_score = match_score
        self.mismatch_penalty = mismatch_penalty
        self.gap_penalty = gap_penalty
        self.align_result = []
        self.score = 0
        self.valid_input = ['A','C','G','T','U','-']
        self.error = False

    
    def calculate_score(self):
        for i in range(self.min_length):
            if self.algn_a[i]=='-' or self.algn_b[i]=='-':
                self.score+=self.gap_penalty
                self.align_result.append('gap')
            elif self.algn_a[i] == self.algn_b[i]:
                self.score+=self.match_score
                self.align_result.append('match')
            else:
                self.score+=self.mismatch_penalty
                self.align_result.append('mismatch')

        if(self.diference >0):
            self.score+=self.gap_penalty*self.diference
            for i in range(self.diference):
                self.align_result.append('gap')

    def get_score(self):
        return self.score
    
    def get_align_result(self):
        return self.align_result
    
    def get_input_alignments(self):
        return [self.algn_a,self.algn_b]

    def get_input_panalty(self):
        return [self.match_score,self.mismatch_penalty,self.gap_penalty]
    


    def validate_input(self):
        for element in self.algn_a:
            if element not in self.valid_input:
                self.error = True
        
        for element in self.algn_b:
            if element not in self.valid_input:
                self.error = True

        if(self.error):
            return {'error':'Invalid input sequence'}
        elif(len(self.algn_a)==0 or len(self.algn_b)==0):
            return {'error':'inputs are not entered'}
        elif(type(self.match_score) is not int or type(self.mismatch_penalty) is not int or type(self.gap_penalty) is not int):
            return {'error':'input panalty are not valid'}
        else:
            return {'error': 'None'}



