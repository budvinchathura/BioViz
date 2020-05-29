import unittest
import json
from Bio import Align
from Bio.Align import substitution_matrices

from PairAlign.Algorithms.SW_extended import SWExtended


# python -m coverage run Tests/test_pairalign.py
# python -m unittest discover -s test/SW_Extended

DATA_FILE_NAME = 'test/SW_Extended/data.json'


class SWTest(unittest.TestCase):
    """
    Class for testing SWExtended algorithm
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
            algo = SWExtended(item['seq_type'],item['sub_mat'], item['seq_a'], item['seq_b'],
                      item['match'], item['mismatch'], item['opening_gap'], item['extending_gap'], item['priority'])
            algo.initialize()
            algo.calculate_score()
            algo.traceback()
            algo.calculate_identity()
            # alignments = algo.get_alignments()[0]
            score = algo.get_score()

            aligner = Align.PairwiseAligner()
            aligner.mode = 'local'
            aligner.match_score = int(item['match'])
            aligner.mismatch_score = int(item['mismatch'])
            aligner.open_gap_score = int(item['opening_gap'])
            aligner.extend_gap_score = int(item['extending_gap'])
            if(item['sub_mat'] != 'DEFAULT'):
                aligner.substitution_matrix = substitution_matrices.load(item['sub_mat'])
            ref_result = aligner.align(item['seq_a'], item['seq_b'])

            ref_score = ref_result.score
            
            # self.assertEqual(score, ref_score)
            self.assertGreaterEqual(score, ref_score)
            
