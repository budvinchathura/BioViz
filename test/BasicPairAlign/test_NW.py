"""
Test classes for testing alignment game
"""
import unittest
import json
from Bio import Align

from PairAlign.Algorithms.NW import NW


# python -m coverage run Tests/test_pairalign.py
# python -m unittest discover -s Tests

DATA_FILE_NAME = 'test/BasicPairAlign/data.json'


class NWTest(unittest.TestCase):
    """
    Class for testing NW algorithm
    """

    def setUp(self):
        with open(DATA_FILE_NAME, 'r') as file:
            self.data = json.load(file)

    def tearDown(self):
        pass

    def test_results(self):
        """
        testing results
        """

        for item in self.data:
            algo = NW(item['seq_a'], item['seq_b'],
                      item['match'], item['mismatch'], item['gap'])
            algo.initialize()
            algo.calculate_score()
            algo.traceback()
            algo.calculate_identity()
            # alignments = algo.get_alignments()[0]
            score = algo.get_score()

            aligner = Align.PairwiseAligner()
            aligner.mode = 'global'
            aligner.match_score = item['match']
            aligner.mismatch_score = item['mismatch']
            aligner.gap_score = item['gap']
            ref_result = aligner.align(item['seq_a'], item['seq_b'])
            ref_score = ref_result.score
            # ref_alignments = []

            # for align in ref_result:
            #     temp = str(align.format()).split('\n')
            #     ref_alignments.append([temp[0], temp[2]])

            # self.assertIn([alignments['algn_a'], alignments['algn_b']], ref_alignments)

            self.assertEqual(score, ref_score, item)
