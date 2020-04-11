import unittest

from PairAlign.Algorithms.NW import NW
from PairAlign.Algorithms.SW import SW

# python -m coverage run Tests/test_pairalign.py
# python -m unittest discover -s Tests


class NWTest(unittest.TestCase):

    # executed prior to each test
    def setUp(self):

        self.algo = NW('AAA', 'AAB', 1, -1, -1)
        self.algo.initialize()

    # executed after each test
    def tearDown(self):
        del self.algo

    ###############
    #### tests ####
    ###############

    def test_alignments(self):
        self.algo.calculate_score()
        self.algo.traceback()
        self.algo.calculate_identity()
        alignments = self.algo.get_alignments()
        self.assertEqual(alignments[0]['algn_a'], 'AAA')
        self.assertEqual(alignments[0]['algn_b'], 'AAB')

    def test_score(self):
        self.algo.calculate_score()
        score = self.algo.get_score()
        self.assertEqual(score, 1)

    def test_identity(self):
        self.algo.calculate_score()
        self.algo.traceback()
        self.algo.calculate_identity()
        alignments = self.algo.get_alignments()
        self.assertEqual(alignments[0]['identity'], 2/3)

class SWTest(unittest.TestCase):

    # executed prior to each test
    def setUp(self):

        self.algo = SW('AAA', 'AAB', 1, -1, -1)
        self.algo.initialize()

    # executed after each test
    def tearDown(self):
        del self.algo

    ###############
    #### tests ####
    ###############

    def test_alignments(self):
        self.algo.calculate_score()
        self.algo.traceback()
        self.algo.calculate_identity()
        alignments = self.algo.get_alignments()
        score = self.algo.get_score()
        self.assertEqual(score, 2)
        self.assertEqual(alignments[0]['algn_a'], 'AA')
        self.assertEqual(alignments[0]['algn_b'], 'AA')
    
    def test_score(self):
        self.algo.calculate_score()
        score = self.algo.get_score()
        self.assertEqual(score, 2)

    def test_identity(self):
        self.algo.calculate_score()
        self.algo.traceback()
        self.algo.calculate_identity()
        alignments = self.algo.get_alignments()
        self.assertEqual(alignments[0]['identity'], 1)
