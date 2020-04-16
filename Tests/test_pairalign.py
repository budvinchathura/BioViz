import unittest
from Bio import Align

from PairAlign.Algorithms.NW import NW
from PairAlign.Algorithms.SW import SW

# python -m coverage run Tests/test_pairalign.py
# python -m unittest discover -s Tests


class NWTest1(unittest.TestCase):

    # executed prior to each test
    def setUp(self):

        self.algo = NW('AAA', 'AAB', 1, -1, -1)
        self.algo.initialize()
        self.aligner = Align.PairwiseAligner()
        self.aligner.mode = 'global'
        self.aligner.match_score = 1
        self.aligner.mismatch_score = -1
        self.aligner.gap_score = -1
        self.score = self.aligner.score('AAA', 'AAB')

    # executed after each test
    def tearDown(self):
        del self.algo

    ###############
    #### tests ####
    ###############

    # def test_alignments(self):
    #     self.algo.calculate_score()
    #     self.algo.traceback()
    #     self.algo.calculate_identity()
    #     alignments = self.algo.get_alignments()
    #     self.assertEqual(alignments[0]['algn_a'], 'AAA')
    #     self.assertEqual(alignments[0]['algn_b'], 'AAB')

    def test_score(self):
        self.algo.calculate_score()
        score = self.algo.get_score()
        self.assertEqual(score, self.score)

    # def test_identity(self):
    #     self.algo.calculate_score()
    #     self.algo.traceback()
    #     self.algo.calculate_identity()
    #     alignments = self.algo.get_alignments()
    #     self.assertEqual(alignments[0]['identity'], 2/3)


class NWTest2(unittest.TestCase):
    
    # executed prior to each test
    def setUp(self):

        s1 = 'AAAAGAGGAGGAGGAGGGGTGTGATTGTTAGGTGAGGAGGTAGGTGATGATGGCTGATGCTTGATGCTGATG'
        s2 = 'AGTTTGGCTGGTGCGTAGTGCACAGTCATTACGTCAGCT'
        match = 1
        mismatch = -1
        gap = -2

        self.algo = NW(s1, s2, match, mismatch, gap)
        self.algo.initialize()
        self.aligner = Align.PairwiseAligner()
        self.aligner.mode = 'global'
        self.aligner.match_score = match
        self.aligner.mismatch_score = mismatch
        self.aligner.gap_score = gap
        self.score = self.aligner.score(s1, s2)

    # executed after each test
    def tearDown(self):
        del self.algo

    ###############
    #### tests ####
    ###############

    def test_score(self):
        self.algo.calculate_score()
        score = self.algo.get_score()
        self.assertEqual(score, self.score)


class NWTest3(unittest.TestCase):
    
    # executed prior to each test
    def setUp(self):

        s1 = 'AAAAGAGGAGTATTTTTTCTTCTTCTTCTTCTTCTCTAGGTGAGGAGTCTTATTCTTATTCTTATTTGATGCTGATG'
        s2 = 'AGTTTGGCTTTCTTATTTTTCTTATTTCTTATTCCCTACTCTACTCACTCTACTCTTTTACCTCATCATCTCTCGGATTACGTCAGCT'
        match = 1
        mismatch = -1
        gap = -2

        self.algo = NW(s1, s2, match, mismatch, gap)
        self.algo.initialize()
        self.aligner = Align.PairwiseAligner()
        self.aligner.mode = 'global'
        self.aligner.match_score = match
        self.aligner.mismatch_score = mismatch
        self.aligner.gap_score = gap
        self.score = self.aligner.score(s1, s2)

    # executed after each test
    def tearDown(self):
        del self.algo

    ###############
    #### tests ####
    ###############

    def test_score(self):
        self.algo.calculate_score()
        score = self.algo.get_score()
        self.assertEqual(score, self.score)



class NWTest4(unittest.TestCase):
    
    # executed prior to each test
    def setUp(self):

        s1 = 'AAAAAAAAAATTTTTTTT'
        s2 = 'GGGGGGGGGCGGCGCGGCGG'
        match = 1
        mismatch = -1
        gap = -2

        self.algo = NW(s1, s2, match, mismatch, gap)
        self.algo.initialize()
        self.aligner = Align.PairwiseAligner()
        self.aligner.mode = 'global'
        self.aligner.match_score = match
        self.aligner.mismatch_score = mismatch
        self.aligner.gap_score = gap
        self.score = self.aligner.score(s1, s2)

    # executed after each test
    def tearDown(self):
        del self.algo

    ###############
    #### tests ####
    ###############

    def test_score(self):
        self.algo.calculate_score()
        score = self.algo.get_score()
        self.assertEqual(score, self.score)

class NWTest5(unittest.TestCase):
    
    # executed prior to each test
    def setUp(self):

        s1 = 'AAAAAAAAAATTTTTTTT'
        s2 = 'GGGGGGGGGCGGCGCGGCGG'
        match = 1
        mismatch = -1
        gap = 0

        self.algo = NW(s1, s2, match, mismatch, gap)
        self.algo.initialize()
        self.aligner = Align.PairwiseAligner()
        self.aligner.mode = 'global'
        self.aligner.match_score = match
        self.aligner.mismatch_score = mismatch
        self.aligner.gap_score = gap
        self.score = self.aligner.score(s1, s2)

    # executed after each test
    def tearDown(self):
        del self.algo

    ###############
    #### tests ####
    ###############

    def test_score(self):
        self.algo.calculate_score()
        score = self.algo.get_score()
        self.assertEqual(score, self.score)

class SWTest1(unittest.TestCase):

    # executed prior to each test
    def setUp(self):

        self.algo = SW('AAA', 'AAB', 1, -1, -1)
        self.algo.initialize()
        self.aligner = Align.PairwiseAligner()
        self.aligner.mode = 'local'
        self.aligner.match_score = 1
        self.aligner.mismatch_score = -1
        self.aligner.gap_score = -1
        self.score = self.aligner.score('AAA', 'AAB')


    # executed after each test
    def tearDown(self):
        del self.algo

    ###############
    #### tests ####
    ###############

    # def test_alignments(self):
    #     self.algo.calculate_score()
    #     self.algo.traceback()
    #     self.algo.calculate_identity()
    #     alignments = self.algo.get_alignments()
    #     score = self.algo.get_score()
    #     self.assertEqual(score, 2)
    #     self.assertEqual(alignments[0]['algn_a'], 'AA')
    #     self.assertEqual(alignments[0]['algn_b'], 'AA')
    
    def test_score(self):
        self.algo.calculate_score()
        score = self.algo.get_score()
        self.assertEqual(score, self.score)

    # def test_identity(self):
    #     self.algo.calculate_score()
    #     self.algo.traceback()
    #     self.algo.calculate_identity()
    #     alignments = self.algo.get_alignments()
    #     self.assertEqual(alignments[0]['identity'], 1)

class SWTest2(unittest.TestCase):
    
    # executed prior to each test
    def setUp(self):

        s1 = 'AAAAGAGGAGTATTTTTTCTTCTTCTTCTTCTTCTCTAGGTGAGGAGTCTTATTCTTATTCTTATTTGATGCTGATG'
        s2 = 'AGTTTGGCTTTCTTATTTTTCTTATTTCTTATTCCCTACTCTACTCACTCTACTCTTTTACCTCATCATCTCTCGGATTACGTCAGCT'
        match = 1
        mismatch = -1
        gap = -2


        self.algo = SW(s1, s2, match, mismatch, gap)
        self.algo.initialize()
        self.aligner = Align.PairwiseAligner()
        self.aligner.mode = 'local'
        self.aligner.match_score = match
        self.aligner.mismatch_score = mismatch
        self.aligner.gap_score = gap
        self.score = self.aligner.score(s1, s2)


    # executed after each test
    def tearDown(self):
        del self.algo

    ###############
    #### tests ####
    ###############
    
    def test_score(self):
        self.algo.calculate_score()
        score = self.algo.get_score()
        self.assertEqual(score, self.score)

class SWTest3(unittest.TestCase):
    
    # executed prior to each test
    def setUp(self):

        s1 = 'AAAAGAGGGGGGCGGCGGCGGCGCGGGCGGCGGGGCGTTTCGGCTGCTGTGCTCTTATTTGATGCTGATG'
        s2 = 'AGTTTGGCTTTCTTATTTTTCTTGGCTGGTTGAGATGTCTCACTCTACTCTTTTACCTCATCATCTCTCGGATTACGTCAGCT'
        match = 1
        mismatch = -1
        gap = -2


        self.algo = SW(s1, s2, match, mismatch, gap)
        self.algo.initialize()
        self.aligner = Align.PairwiseAligner()
        self.aligner.mode = 'local'
        self.aligner.match_score = match
        self.aligner.mismatch_score = mismatch
        self.aligner.gap_score = gap
        self.score = self.aligner.score(s1, s2)


    # executed after each test
    def tearDown(self):
        del self.algo

    ###############
    #### tests ####
    ###############
    
    def test_score(self):
        self.algo.calculate_score()
        score = self.algo.get_score()
        self.assertEqual(score, self.score)

class SWTest4(unittest.TestCase):
    
    # executed prior to each test
    def setUp(self):

        s1 = 'AAAAAAAAAATTTTTTTT'
        s2 = 'GGGGGGGGGCGGCGCGGCGG'
        match = 1
        mismatch = -1
        gap = -2


        self.algo = SW(s1, s2, match, mismatch, gap)
        self.algo.initialize()
        self.aligner = Align.PairwiseAligner()
        self.aligner.mode = 'local'
        self.aligner.match_score = match
        self.aligner.mismatch_score = mismatch
        self.aligner.gap_score = gap
        self.score = self.aligner.score(s1, s2)


    # executed after each test
    def tearDown(self):
        del self.algo

    ###############
    #### tests ####
    ###############
    
    def test_score(self):
        self.algo.calculate_score()
        score = self.algo.get_score()
        self.assertEqual(score, self.score)

class SWTest5(unittest.TestCase):
    
    # executed prior to each test
    def setUp(self):

        s1 = 'AAATGGTAGGTGTTTCTTCGCTTTTTTT'
        s2 = 'GGGGGTGTGATGTTAGTGGCGG'
        match = 1
        mismatch = -1
        gap = 0


        self.algo = SW(s1, s2, match, mismatch, gap)
        self.algo.initialize()
        self.aligner = Align.PairwiseAligner()
        self.aligner.mode = 'local'
        self.aligner.match_score = match
        self.aligner.mismatch_score = mismatch
        self.aligner.gap_score = gap
        self.score = self.aligner.score(s1, s2)


    # executed after each test
    def tearDown(self):
        del self.algo

    ###############
    #### tests ####
    ###############
    
    def test_score(self):
        self.algo.calculate_score()
        score = self.algo.get_score()
        self.assertEqual(score, self.score)