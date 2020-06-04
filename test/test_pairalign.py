# """
# Test classes for testing alignment game
# """
# import unittest
# from Bio import Align
# from Bio.Align import substitution_matrices

# from PairAlign.Algorithms.NW import NW
# from PairAlign.Algorithms.SW import SW
# from PairAlign.Algorithms.NW_extended import NWExtended
# from PairAlign.Algorithms.SW_extended import SWExtended

# # python -m coverage run Tests/test_pairalign.py
# # python -m unittest discover -s Tests


# class NWTest1(unittest.TestCase):
#     """
#     Class for testing NW algorithm
#     """

#     def setUp(self):
#         self.algo = NW('AAA', 'AAB', 1, -1, -1)
#         self.algo.initialize()
#         self.aligner = Align.PairwiseAligner()
#         self.aligner.mode = 'global'
#         self.aligner.match_score = 1
#         self.aligner.mismatch_score = -1
#         self.aligner.gap_score = -1
#         self.score = self.aligner.score('AAA', 'AAB')

#     def tearDown(self):
#         del self.algo

#     def test_score(self):
#         """
#         testing score
#         """
#         self.algo.calculate_score()
#         score = self.algo.get_score()
#         self.assertEqual(score, self.score)


# class NWTest2(unittest.TestCase):
#     """
#     Class for testing NW algorithm
#     """

#     def setUp(self):
#         s_1 = 'AAAAGAGGAGGAGGAGGGGTGTGATTGTTAGGTGAGGAGGTAGGTGATGATGGCTGATGCTTGATGCTGATG'
#         s_2 = 'AGTTTGGCTGGTGCGTAGTGCACAGTCATTACGTCAGCT'
#         match = 1
#         mismatch = -1
#         gap = -2

#         self.algo = NW(s_1, s_2, match, mismatch, gap)
#         self.algo.initialize()
#         self.aligner = Align.PairwiseAligner()
#         self.aligner.mode = 'global'
#         self.aligner.match_score = match
#         self.aligner.mismatch_score = mismatch
#         self.aligner.gap_score = gap
#         self.score = self.aligner.score(s_1, s_2)

#     # executed after each test
#     def tearDown(self):
#         del self.algo

#     def test_score(self):
#         """
#         testing score
#         """
#         self.algo.calculate_score()
#         score = self.algo.get_score()
#         self.assertEqual(score, self.score)


# class NWTest3(unittest.TestCase):
#     """
#     Class for testing NW algorithm
#     """

#     def setUp(self):
#         s_1 = 'AAAAGAGGAGTATTTTTTCTTCTTCTTCTTCTTCTCTAGGTGAGGAGTCTTATTCTTATTCTTATTTGATGCTGATG'
#         s_2 = 'AGTTTGGCTTTCTTATTTTTCTTATTTCTTATTCCCTACTCTACTCACTCTACTCTTTTACCTCATCATCTCTCGGATTACGTCAGCT'
#         match = 1
#         mismatch = -1
#         gap = -2

#         self.algo = NW(s_1, s_2, match, mismatch, gap)
#         self.algo.initialize()
#         self.aligner = Align.PairwiseAligner()
#         self.aligner.mode = 'global'
#         self.aligner.match_score = match
#         self.aligner.mismatch_score = mismatch
#         self.aligner.gap_score = gap
#         self.score = self.aligner.score(s_1, s_2)

#     def tearDown(self):
#         del self.algo
#     def test_score(self):
#         """
#         testing score
#         """
#         self.algo.calculate_score()
#         score = self.algo.get_score()
#         self.assertEqual(score, self.score)


# class NWTest4(unittest.TestCase):
#     """
#     Class for testing NW algorithm
#     """

#     def setUp(self):
#         s_1 = 'AAAAAAAAAATTTTTTTT'
#         s_2 = 'GGGGGGGGGCGGCGCGGCGG'
#         match = 1
#         mismatch = -1
#         gap = -2

#         self.algo = NW(s_1, s_2, match, mismatch, gap)
#         self.algo.initialize()
#         self.aligner = Align.PairwiseAligner()
#         self.aligner.mode = 'global'
#         self.aligner.match_score = match
#         self.aligner.mismatch_score = mismatch
#         self.aligner.gap_score = gap
#         self.score = self.aligner.score(s_1, s_2)

#     def tearDown(self):
#         del self.algo

#     def test_score(self):
#         """
#         testing score
#         """
#         self.algo.calculate_score()
#         score = self.algo.get_score()
#         self.assertEqual(score, self.score)


# class NWTest5(unittest.TestCase):
#     """
#     Class for testing NW algorithm
#     """

#     def setUp(self):
#         s_1 = 'AAAAAAAAAATTTTTTTT'
#         s_2 = 'GGGGGGGGGCGGCGCGGCGG'
#         match = 1
#         mismatch = -1
#         gap = 0

#         self.algo = NW(s_1, s_2, match, mismatch, gap)
#         self.algo.initialize()
#         self.aligner = Align.PairwiseAligner()
#         self.aligner.mode = 'global'
#         self.aligner.match_score = match
#         self.aligner.mismatch_score = mismatch
#         self.aligner.gap_score = gap
#         self.score = self.aligner.score(s_1, s_2)

#     def tearDown(self):
#         del self.algo

#     def test_score(self):
#         """
#         testing score
#         """
#         self.algo.calculate_score()
#         score = self.algo.get_score()
#         self.assertEqual(score, self.score)


# class SWTest1(unittest.TestCase):
#     """
#     Class for testing SW algorithm
#     """

#     def setUp(self):
#         self.algo = SW('AAA', 'AAB', 1, -1, -1)
#         self.algo.initialize()
#         self.aligner = Align.PairwiseAligner()
#         self.aligner.mode = 'local'
#         self.aligner.match_score = 1
#         self.aligner.mismatch_score = -1
#         self.aligner.gap_score = -1
#         self.score = self.aligner.score('AAA', 'AAB')
#     def tearDown(self):
#         del self.algo

#     def test_score(self):
#         """
#         testing score
#         """
#         self.algo.calculate_score()
#         score = self.algo.get_score()
#         self.assertEqual(score, self.score)


# class SWTest2(unittest.TestCase):
#     """
#     Class for testing SW algorithm
#     """

#     def setUp(self):
#         s_1 = 'AAAAGAGGAGTATTTTTTCTTCTTCTTCTTCTTCTCTAGGTGAGGAGTCTTATTCTTATTCTTATTTGATGCTGATG'
#         s_2 = 'AGTTTGGCTTTCTTATTTTTCTTATTTCTTATTCCCTACTCTACTCACTCTACTCTTTTACCTCATCATCTCTCGGATTACGTCAGCT'
#         match = 1
#         mismatch = -1
#         gap = -2

#         self.algo = SW(s_1, s_2, match, mismatch, gap)
#         self.algo.initialize()
#         self.aligner = Align.PairwiseAligner()
#         self.aligner.mode = 'local'
#         self.aligner.match_score = match
#         self.aligner.mismatch_score = mismatch
#         self.aligner.gap_score = gap
#         self.score = self.aligner.score(s_1, s_2)
#     def tearDown(self):
#         del self.algo

#     def test_score(self):
#         """
#         testing score
#         """
#         self.algo.calculate_score()
#         score = self.algo.get_score()
#         self.assertEqual(score, self.score)


# class SWTest3(unittest.TestCase):
#     """
#     Class for testing SW algorithm
#     """

#     def setUp(self):
#         s_1 = 'AAAAGAGGGGGGCGGCGGCGGCGCGGGCGGCGGGGCGTTTCGGCTGCTGTGCTCTTATTTGATGCTGATG'
#         s_2 = 'AGTTTGGCTTTCTTATTTTTCTTGGCTGGTTGAGATGTCTCACTCTACTCTTTTACCTCATCATCTCTCGGATTACGTCAGCT'
#         match = 1
#         mismatch = -1
#         gap = -2

#         self.algo = SW(s_1, s_2, match, mismatch, gap)
#         self.algo.initialize()
#         self.aligner = Align.PairwiseAligner()
#         self.aligner.mode = 'local'
#         self.aligner.match_score = match
#         self.aligner.mismatch_score = mismatch
#         self.aligner.gap_score = gap
#         self.score = self.aligner.score(s_1, s_2)
#     def tearDown(self):
#         del self.algo

#     def test_score(self):
#         """
#         testing score
#         """
#         self.algo.calculate_score()
#         score = self.algo.get_score()
#         self.assertEqual(score, self.score)


# class SWTest4(unittest.TestCase):
#     """
#     Class for testing SW algorithm
#     """

#     def setUp(self):
#         s_1 = 'AAAAAAAAAATTTTTTTT'
#         s_2 = 'GGGGGGGGGCGGCGCGGCGG'
#         match = 1
#         mismatch = -1
#         gap = -2

#         self.algo = SW(s_1, s_2, match, mismatch, gap)
#         self.algo.initialize()
#         self.aligner = Align.PairwiseAligner()
#         self.aligner.mode = 'local'
#         self.aligner.match_score = match
#         self.aligner.mismatch_score = mismatch
#         self.aligner.gap_score = gap
#         self.score = self.aligner.score(s_1, s_2)
#     def tearDown(self):
#         del self.algo

#     def test_score(self):
#         """
#         testing score
#         """
#         self.algo.calculate_score()
#         score = self.algo.get_score()
#         self.assertEqual(score, self.score)


# class SWTest5(unittest.TestCase):
#     """
#     Class for testing SW algorithm
#     """

#     def setUp(self):
#         s_1 = 'AAATGGTAGGTGTTTCTTCGCTTTTTTT'
#         s_2 = 'GGGGGTGTGATGTTAGTGGCGG'
#         match = 1
#         mismatch = -1
#         gap = 0

#         self.algo = SW(s_1, s_2, match, mismatch, gap)
#         self.algo.initialize()
#         self.aligner = Align.PairwiseAligner()
#         self.aligner.mode = 'local'
#         self.aligner.match_score = match
#         self.aligner.mismatch_score = mismatch
#         self.aligner.gap_score = gap
#         self.score = self.aligner.score(s_1, s_2)

#     def tearDown(self):
#         del self.algo

#     def test_score(self):
#         """
#         testing score
#         """
#         self.algo.calculate_score()
#         score = self.algo.get_score()
#         self.assertEqual(score, self.score)

# class NWExtendedTest1(unittest.TestCase):
#     """
#     Class for testing NWExtended algorithm
#     """

#     def setUp(self):
#         seq_type = 'DNA'
#         sub_mat = 'DEFAULT'
#         s_1 = 'AAATGGTAGGTGTTTCTTCGCTTTTTTT'
#         s_2 = 'GGGGGTGTGATGTTAGTGGCGG'
#         match = 1
#         mismatch = -1
#         opening_gap_penalty = -3
#         extending_gap_penalty = -1
#         priority = 'HIGHROAD'

#         self.algo = NWExtended(seq_type, sub_mat, s_1, s_2, match, mismatch, opening_gap_penalty, extending_gap_penalty, priority)
#         self.algo.initialize()
#         self.aligner = Align.PairwiseAligner()
#         self.aligner.mode = 'global'
#         self.aligner.match_score = match
#         self.aligner.mismatch_score = mismatch
#         self.aligner.open_gap_score = opening_gap_penalty
#         self.aligner.extend_gap_score = extending_gap_penalty
#         self.score = self.aligner.score(s_1, s_2)

#     def tearDown(self):
#         del self.algo

#     def test_score(self):
#         """
#         testing score
#         """
#         self.algo.calculate_score()
#         score = self.algo.get_score()
#         self.assertEqual(score, self.score)

# class NWExtendedTest2(unittest.TestCase):
#     """
#     Class for testing NWExtended algorithm
#     """

#     def setUp(self):
#         seq_type = 'PROTEIN'
#         sub_mat = 'BLOSUM50'
#         s_1 = 'AAATGGTAGGTGTTTCTTCGCTXTTTTTT'
#         s_2 = 'GGGGGTGTGATGTTAGTGGCGG'
#         match = 0
#         mismatch = 0
#         opening_gap_penalty = -3
#         extending_gap_penalty = -1
#         priority = 'HIGHROAD'

#         self.algo = NWExtended(seq_type, sub_mat, s_1, s_2, match, mismatch, opening_gap_penalty, extending_gap_penalty, priority)
#         self.algo.initialize()
#         self.aligner = Align.PairwiseAligner()
#         self.aligner.mode = 'global'
#         # self.aligner.match_score = match
#         # self.aligner.mismatch_score = mismatch
#         self.aligner.substitution_matrix = substitution_matrices.load("BLOSUM50")
#         self.aligner.open_gap_score = opening_gap_penalty
#         self.aligner.extend_gap_score = extending_gap_penalty
#         self.score = self.aligner.score(s_1, s_2)

#     def tearDown(self):
#         del self.algo

#     def test_score(self):
#         """
#         testing score
#         """
#         self.algo.calculate_score()
#         score = self.algo.get_score()
#         self.assertEqual(score, self.score)

# class NWExtendedTest3(unittest.TestCase):
#     """
#     Class for testing NWExtended algorithm
#     """

#     def setUp(self):
#         seq_type = 'PROTEIN'
#         sub_mat = 'DEFAULT'
#         s_1 = 'AAATGGTAGGTGTTTCTTCGCTTTTTTT'
#         s_2 = 'GGGGGTGTGATGTTAGTGGCGG'
#         match = 1
#         mismatch = -1
#         opening_gap_penalty = -3
#         extending_gap_penalty = -1
#         priority = 'HIGHROAD'

#         self.algo = NWExtended(seq_type, sub_mat, s_1, s_2, match, mismatch, opening_gap_penalty, extending_gap_penalty, priority)
#         self.algo.initialize()
#         self.aligner = Align.PairwiseAligner()
#         self.aligner.mode = 'global'
#         self.aligner.match_score = match
#         self.aligner.mismatch_score = mismatch
#         self.aligner.open_gap_score = opening_gap_penalty
#         self.aligner.extend_gap_score = extending_gap_penalty
#         self.score = self.aligner.score(s_1, s_2)

#     def tearDown(self):
#         del self.algo

#     def test_score(self):
#         """
#         testing score
#         """
#         self.algo.calculate_score()
#         score = self.algo.get_score()
#         self.assertEqual(score, self.score)

# class SWExtendedTest1(unittest.TestCase):
#     """
#     Class for testing SWExtended algorithm
#     """

#     def setUp(self):
#         seq_type = 'DNA'
#         sub_mat = 'DEFAULT'
#         s_1 = 'AAATGGTAGGTGTTTCTTCGCTTTTTTT'
#         s_2 = 'GGGGGTGTGATGTTAGTGGCGG'
#         match = 1
#         mismatch = -1
#         opening_gap_penalty = -3
#         extending_gap_penalty = -1
#         priority = 'HIGHROAD'

#         self.algo = SWExtended(seq_type, sub_mat, s_1, s_2, match, mismatch, opening_gap_penalty, extending_gap_penalty, priority)
#         self.algo.initialize()
#         self.aligner = Align.PairwiseAligner()
#         self.aligner.mode = 'local'
#         self.aligner.match_score = match
#         self.aligner.mismatch_score = mismatch
#         self.aligner.open_gap_score = opening_gap_penalty
#         self.aligner.extend_gap_score = extending_gap_penalty
#         self.score = self.aligner.score(s_1, s_2)

#     def tearDown(self):
#         del self.algo

#     def test_score(self):
#         """
#         testing score
#         """
#         self.algo.calculate_score()
#         score = self.algo.get_score()
#         self.assertEqual(score, self.score)

# class SWExtendedTest2(unittest.TestCase):
#     """
#     Class for testing SWExtended algorithm
#     """

#     def setUp(self):
#         seq_type = 'PROTEIN'
#         sub_mat = 'BLOSUM50'
#         s_1 = 'AAATGGTAGGTGTTTCTTCGCTXTTTTTT'
#         s_2 = 'GGGGGTGTGATGTTAGTGGCGG'
#         match = 0
#         mismatch = 0
#         opening_gap_penalty = -3
#         extending_gap_penalty = -1
#         priority = 'HIGHROAD'

#         self.algo = SWExtended(seq_type, sub_mat, s_1, s_2, match, mismatch, opening_gap_penalty, extending_gap_penalty, priority)
#         self.algo.initialize()
#         self.aligner = Align.PairwiseAligner()
#         self.aligner.mode = 'local'
#         # self.aligner.match_score = match
#         # self.aligner.mismatch_score = mismatch
#         self.aligner.substitution_matrix = substitution_matrices.load("BLOSUM50")
#         self.aligner.open_gap_score = opening_gap_penalty
#         self.aligner.extend_gap_score = extending_gap_penalty
#         self.score = self.aligner.score(s_1, s_2)

#     def tearDown(self):
#         del self.algo

#     def test_score(self):
#         """
#         testing score
#         """
#         self.algo.calculate_score()
#         score = self.algo.get_score()
#         self.assertEqual(score, self.score)

# class SWExtendedTest3(unittest.TestCase):
#     """
#     Class for testing SWExtended algorithm
#     """

#     def setUp(self):
#         seq_type = 'PROTEIN'
#         sub_mat = 'DEFAULT'
#         s_1 = 'AAATGGTAGGTGTTTCTTCGCTTTTTTT'
#         s_2 = 'GGGGGTGTGATGTTAGTGGCGG'
#         match = 1
#         mismatch = -1
#         opening_gap_penalty = -3
#         extending_gap_penalty = -1
#         priority = 'HIGHROAD'

#         self.algo = SWExtended(seq_type, sub_mat, s_1, s_2, match, mismatch, opening_gap_penalty, extending_gap_penalty, priority)
#         self.algo.initialize()
#         self.aligner = Align.PairwiseAligner()
#         self.aligner.mode = 'local'
#         self.aligner.match_score = match
#         self.aligner.mismatch_score = mismatch
#         self.aligner.open_gap_score = opening_gap_penalty
#         self.aligner.extend_gap_score = extending_gap_penalty
#         self.score = self.aligner.score(s_1, s_2)

#     def tearDown(self):
#         del self.algo

#     def test_score(self):
#         """
#         testing score
#         """
#         self.algo.calculate_score()
#         score = self.algo.get_score()
#         self.assertEqual(score, self.score)
