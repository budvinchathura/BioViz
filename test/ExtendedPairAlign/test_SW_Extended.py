import unittest
import json
from Bio import pairwise2
from Bio.SubsMat import MatrixInfo as matlist

from PairAlign.Algorithms.SW_extended import SWExtended


# python -m coverage run Tests/test_pairalign.py
# python -m unittest discover -s test/ExtendedPairAlign

DATA_FILE_NAME = 'test/ExtendedPairAlign/data.json'


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
            algo = SWExtended(item['seq_type'], item['sub_mat'],
                              item['seq_a'], item['seq_b'],
                              item['match'], item['mismatch'],
                              item['opening_gap'], item['extending_gap'], item['priority'])
            algo.initialize()
            algo.calculate_score()
            algo.traceback()
            algo.calculate_identity()
            # alignments = algo.get_alignments()[0]
            score = algo.get_score()

            # aligner = Align.PairwiseAligner()
            # aligner.mode = 'local'
            # aligner.match_score = int(item['match'])
            # aligner.mismatch_score = int(item['mismatch'])
            # aligner.open_gap_score = int(item['opening_gap'])
            # aligner.extend_gap_score = int(item['extending_gap'])
            # if(item['sub_mat'] != 'DEFAULT'):
            #     aligner.substitution_matrix = substitution_matrices.load(item['sub_mat'])
            # ref_result = aligner.align(item['seq_a'], item['seq_b'])

            # ref_score = ref_result.score

            match = int(item['match'])
            mismatch = int(item['mismatch'])
            opening_gap = int(item['opening_gap'])
            extending_gap = int(item['extending_gap'])
            if item['sub_mat'] == 'DEFAULT':
                ref_score = pairwise2.align.localmd(item['seq_a'].upper(),
                                                    item['seq_b'].upper(),
                                                    match, mismatch,
                                                    opening_gap,
                                                    extending_gap,
                                                    opening_gap,
                                                    extending_gap,
                                                    score_only=True)
            else:
                # subs_mat = matlist.blosum90
                if item['sub_mat'] == 'BLOSUM90':
                    subs_mat = matlist.blosum90
                elif item['sub_mat'] == 'BLOSUM62':
                    subs_mat = matlist.blosum62
                elif item['sub_mat'] == 'BLOSUM60':
                    subs_mat = matlist.blosum60
                elif item['sub_mat'] == 'BLOSUM50':
                    subs_mat = matlist.blosum50
                elif item['sub_mat'] == 'BLOSUM45':
                    subs_mat = matlist.blosum45
                elif item['sub_mat'] == 'BLOSUM30':
                    subs_mat = matlist.blosum30

                ref_score = pairwise2.align.localdd(item['seq_a'].upper(),
                                                    item['seq_b'].upper(),
                                                    subs_mat, opening_gap,
                                                    extending_gap,
                                                    opening_gap,
                                                    extending_gap,
                                                    score_only=True)

            # self.assertEqual(score, ref_score)

            self.assertEqual(score, ref_score)
