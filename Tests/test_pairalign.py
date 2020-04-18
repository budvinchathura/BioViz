"""
Test classes for testing alignment game
"""
import unittest
from Bio import Align

from PairAlign.Algorithms.NW import NW
from PairAlign.Algorithms.SW import SW

# python -m coverage run Tests/test_pairalign.py
# python -m unittest discover -s Tests


class NWTest1(unittest.TestCase):
    """
    Class for testing NW algorithm
    """

    def setUp(self):
        self.algo = NW('AAA', 'AAB', 1, -1, -1)
        self.algo.initialize()
        self.aligner = Align.PairwiseAligner()
        self.aligner.mode = 'global'
        self.aligner.match_score = 1
        self.aligner.mismatch_score = -1
        self.aligner.gap_score = -1
        self.score = self.aligner.score('AAA', 'AAB')

    def tearDown(self):
        del self.algo

    def test_score(self):
        """
        testing score
        """
        self.algo.calculate_score()
        score = self.algo.get_score()
        self.assertEqual(score, self.score)


class NWTest2(unittest.TestCase):
    """
    Class for testing NW algorithm
    """

    def setUp(self):
        s_1 = 'AAAAGAGGAGGAGGAGGGGTGTGATTGTTAGGTGAGGAGGTAGGTGATGATGGCTGATGCTTGATGCTGATG'
        s_2 = 'AGTTTGGCTGGTGCGTAGTGCACAGTCATTACGTCAGCT'
        match = 1
        mismatch = -1
        gap = -2

        self.algo = NW(s_1, s_2, match, mismatch, gap)
        self.algo.initialize()
        self.aligner = Align.PairwiseAligner()
        self.aligner.mode = 'global'
        self.aligner.match_score = match
        self.aligner.mismatch_score = mismatch
        self.aligner.gap_score = gap
        self.score = self.aligner.score(s_1, s_2)

    # executed after each test
    def tearDown(self):
        del self.algo

    def test_score(self):
        """
        testing score
        """
        self.algo.calculate_score()
        score = self.algo.get_score()
        self.assertEqual(score, self.score)


class NWTest3(unittest.TestCase):
    """
    Class for testing NW algorithm
    """

    def setUp(self):
        s_1 = 'AAAAGAGGAGTATTTTTTCTTCTTCTTCTTCTTCTCTAGGTGAGGAGTCTTATTCTTATTCTTATTTGATGCTGATG'
        s_2 = 'AGTTTGGCTTTCTTATTTTTCTTATTTCTTATTCCCTACTCTACTCACTCTACTCTTTTACCTCATCATCTCTCGGATTACGTCAGCT'
        match = 1
        mismatch = -1
        gap = -2

        self.algo = NW(s_1, s_2, match, mismatch, gap)
        self.algo.initialize()
        self.aligner = Align.PairwiseAligner()
        self.aligner.mode = 'global'
        self.aligner.match_score = match
        self.aligner.mismatch_score = mismatch
        self.aligner.gap_score = gap
        self.score = self.aligner.score(s_1, s_2)

    def tearDown(self):
        del self.algo
    def test_score(self):
        """
        testing score
        """
        self.algo.calculate_score()
        score = self.algo.get_score()
        self.assertEqual(score, self.score)


class NWTest4(unittest.TestCase):
    """
    Class for testing NW algorithm
    """

    def setUp(self):
        s_1 = 'AAAAAAAAAATTTTTTTT'
        s_2 = 'GGGGGGGGGCGGCGCGGCGG'
        match = 1
        mismatch = -1
        gap = -2

        self.algo = NW(s_1, s_2, match, mismatch, gap)
        self.algo.initialize()
        self.aligner = Align.PairwiseAligner()
        self.aligner.mode = 'global'
        self.aligner.match_score = match
        self.aligner.mismatch_score = mismatch
        self.aligner.gap_score = gap
        self.score = self.aligner.score(s_1, s_2)

    def tearDown(self):
        del self.algo

    def test_score(self):
        """
        testing score
        """
        self.algo.calculate_score()
        score = self.algo.get_score()
        self.assertEqual(score, self.score)


class NWTest5(unittest.TestCase):
    """
    Class for testing NW algorithm
    """

    def setUp(self):
        s_1 = 'AAAAAAAAAATTTTTTTT'
        s_2 = 'GGGGGGGGGCGGCGCGGCGG'
        match = 1
        mismatch = -1
        gap = 0

        self.algo = NW(s_1, s_2, match, mismatch, gap)
        self.algo.initialize()
        self.aligner = Align.PairwiseAligner()
        self.aligner.mode = 'global'
        self.aligner.match_score = match
        self.aligner.mismatch_score = mismatch
        self.aligner.gap_score = gap
        self.score = self.aligner.score(s_1, s_2)

    def tearDown(self):
        del self.algo

    def test_score(self):
        """
        testing score
        """
        self.algo.calculate_score()
        score = self.algo.get_score()
        self.assertEqual(score, self.score)


class SWTest1(unittest.TestCase):
    """
    Class for testing SW algorithm
    """

    def setUp(self):
        self.algo = SW('AAA', 'AAB', 1, -1, -1)
        self.algo.initialize()
        self.aligner = Align.PairwiseAligner()
        self.aligner.mode = 'local'
        self.aligner.match_score = 1
        self.aligner.mismatch_score = -1
        self.aligner.gap_score = -1
        self.score = self.aligner.score('AAA', 'AAB')
    def tearDown(self):
        del self.algo

    def test_score(self):
        """
        testing score
        """
        self.algo.calculate_score()
        score = self.algo.get_score()
        self.assertEqual(score, self.score)


class SWTest2(unittest.TestCase):
    """
    Class for testing SW algorithm
    """

    def setUp(self):
        s_1 = 'AAAAGAGGAGTATTTTTTCTTCTTCTTCTTCTTCTCTAGGTGAGGAGTCTTATTCTTATTCTTATTTGATGCTGATG'
        s_2 = 'AGTTTGGCTTTCTTATTTTTCTTATTTCTTATTCCCTACTCTACTCACTCTACTCTTTTACCTCATCATCTCTCGGATTACGTCAGCT'
        match = 1
        mismatch = -1
        gap = -2

        self.algo = SW(s_1, s_2, match, mismatch, gap)
        self.algo.initialize()
        self.aligner = Align.PairwiseAligner()
        self.aligner.mode = 'local'
        self.aligner.match_score = match
        self.aligner.mismatch_score = mismatch
        self.aligner.gap_score = gap
        self.score = self.aligner.score(s_1, s_2)
    def tearDown(self):
        del self.algo

    def test_score(self):
        """
        testing score
        """
        self.algo.calculate_score()
        score = self.algo.get_score()
        self.assertEqual(score, self.score)


class SWTest3(unittest.TestCase):
    """
    Class for testing SW algorithm
    """

    def setUp(self):
        s_1 = 'AAAAGAGGGGGGCGGCGGCGGCGCGGGCGGCGGGGCGTTTCGGCTGCTGTGCTCTTATTTGATGCTGATG'
        s_2 = 'AGTTTGGCTTTCTTATTTTTCTTGGCTGGTTGAGATGTCTCACTCTACTCTTTTACCTCATCATCTCTCGGATTACGTCAGCT'
        match = 1
        mismatch = -1
        gap = -2

        self.algo = SW(s_1, s_2, match, mismatch, gap)
        self.algo.initialize()
        self.aligner = Align.PairwiseAligner()
        self.aligner.mode = 'local'
        self.aligner.match_score = match
        self.aligner.mismatch_score = mismatch
        self.aligner.gap_score = gap
        self.score = self.aligner.score(s_1, s_2)
    def tearDown(self):
        del self.algo

    def test_score(self):
        """
        testing score
        """
        self.algo.calculate_score()
        score = self.algo.get_score()
        self.assertEqual(score, self.score)


class SWTest4(unittest.TestCase):
    """
    Class for testing SW algorithm
    """

    def setUp(self):
        s_1 = 'AAAAAAAAAATTTTTTTT'
        s_2 = 'GGGGGGGGGCGGCGCGGCGG'
        match = 1
        mismatch = -1
        gap = -2

        self.algo = SW(s_1, s_2, match, mismatch, gap)
        self.algo.initialize()
        self.aligner = Align.PairwiseAligner()
        self.aligner.mode = 'local'
        self.aligner.match_score = match
        self.aligner.mismatch_score = mismatch
        self.aligner.gap_score = gap
        self.score = self.aligner.score(s_1, s_2)
    def tearDown(self):
        del self.algo

    def test_score(self):
        """
        testing score
        """
        self.algo.calculate_score()
        score = self.algo.get_score()
        self.assertEqual(score, self.score)


class SWTest5(unittest.TestCase):
    """
    Class for testing SW algorithm
    """

    def setUp(self):
        s_1 = 'AAATGGTAGGTGTTTCTTCGCTTTTTTT'
        s_2 = 'GGGGGTGTGATGTTAGTGGCGG'
        match = 1
        mismatch = -1
        gap = 0

        self.algo = SW(s_1, s_2, match, mismatch, gap)
        self.algo.initialize()
        self.aligner = Align.PairwiseAligner()
        self.aligner.mode = 'local'
        self.aligner.match_score = match
        self.aligner.mismatch_score = mismatch
        self.aligner.gap_score = gap
        self.score = self.aligner.score(s_1, s_2)

    def tearDown(self):
        del self.algo

    def test_score(self):
        """
        testing score
        """
        self.algo.calculate_score()
        score = self.algo.get_score()
        self.assertEqual(score, self.score)
