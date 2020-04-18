"""
Test classes for testing alignment game
"""
import unittest
from Game.Games.AlignmentGame import AlignmentGame

class GameTest(unittest.TestCase):
    """
    class for testing alignment game
    """

    def setUp(self):
        self.algo = AlignmentGame('AAAC', 'AAC-', 2, -1, -1)

    def tearDown(self):
        del self.algo

    def test_input_sequence(self):
        """
        Ensure that user inputs sequence get correctly
        """
        input_seq = self.algo.get_input_alignments()
        self.assertEqual(input_seq[0], 'AAAC')
        self.assertEqual(input_seq[1], 'AAC-')

    def test_input_panalties(self):
        """
        Ensure that user panalties get correcly
        """
        input_panalties = self.algo.get_input_panalty()
        self.assertEqual(input_panalties[0], 2)
        self.assertEqual(input_panalties[1], -1)
        self.assertEqual(input_panalties[2], -1)

    def test_calculate_score(self):
        """
        Ensure that game score get correctly
        """
        input_validation = self.algo.validate_input()
        self.assertEqual(input_validation, {'error': 'None'})
        self.algo.calculate_score()
        score = self.algo.get_score()
        self.assertEqual(score, 2)

    def test_alignment_result(self):
        """
        Ensure that game alignment result get correctly
        """
        self.algo.calculate_score()
        alignment_result = self.algo.get_align_result()
        self.assertEqual(alignment_result, ['match', 'match', 'mismatch', 'gap'])


class GameTestInputType1(unittest.TestCase):
    """
    class for testing alignment game
    """

    def setUp(self):
        self.algo = AlignmentGame('AACTU', 'AC', 4, -1, -1)

    def tearDown(self):
        del self.algo

    def test_calculate_score(self):
        """
        Ensure that game score get correctly for diferent type of inputs 1
        """
        self.algo.calculate_score()
        score = self.algo.get_score()
        self.assertEqual(score, 0)

    def test_alignment_result(self):
        """
        Ensure that game alignment result get correctly
        """
        self.algo.calculate_score()
        alignment_result = self.algo.get_align_result()
        self.assertEqual(alignment_result, ['match', 'mismatch', 'gap', 'gap', 'gap'])

    def test_validation(self):
        """
        Testing for validation
        """
        input_validation = self.algo.validate_input()
        self.assertEqual(input_validation, {'error': 'None'})


class GameTestInputType2(unittest.TestCase):
    """
    class for testing alignment game
    """

    def setUp(self):

        self.algo = AlignmentGame('C--TA', 'CACTU', 2, -1, -1)

    def tearDown(self):
        del self.algo

    def test_get_score2(self):
        """
        Ensure that game score get correctly for diferent type of inputs 1
        """
        self.algo.calculate_score()
        score = self.algo.get_score()
        self.assertEqual(score, 1)

    def test_alignment_result(self):
        """
        Ensure that game alignment result get correctly
        """
        self.algo.calculate_score()
        alignment_result = self.algo.get_align_result()
        self.assertEqual(alignment_result, ['match', 'gap', 'gap', 'match', 'mismatch'])

    def test_validation(self):
        """
        Testing for validation
        """
        input_validation = self.algo.validate_input()
        self.assertEqual(input_validation, {'error': 'None'})


class GameTestInputType3(unittest.TestCase):
    """
    class for testing alignment game
    """

    def setUp(self):
        self.algo = AlignmentGame('CUTTAC', '-', 2, -1, -1)

    def tearDown(self):
        del self.algo

    def test_get_score3(self):
        """
        Ensure that game score get correctly for diferent type of inputs 1
        """
        self.algo.calculate_score()
        score = self.algo.get_score()
        self.assertEqual(score, -6)

    def test_alignment_result(self):
        """
        Ensure that game alignment result get correctly
        """
        self.algo.calculate_score()
        alignment_result = self.algo.get_align_result()
        self.assertEqual(alignment_result, ['gap', 'gap', 'gap', 'gap', 'gap', 'gap'])

    def test_validation(self):
        """
        Testing for validation
        """
        input_validation = self.algo.validate_input()
        self.assertEqual(input_validation, {'error': 'None'})


class GameTestInputTypeNullInput1(unittest.TestCase):
    """
    class for testing alignment game
    """

    def setUp(self):
        self.algo = AlignmentGame('', '', 2, -1, -1)

    def tearDown(self):
        del self.algo
    def test_null_input1(self):
        """
        Testing for for both null inputs
        """
        input_validation = self.algo.validate_input()
        self.assertEqual(input_validation, {'error': 'inputs are not entered'})


class GameTestInputTypeNullInput2(unittest.TestCase):
    """
    class for testing alignment game
    """

    def setUp(self):
        self.algo = AlignmentGame('AA-TU', '', 2, -1, -1)

    def tearDown(self):
        del self.algo

    def test_null_input2(self):
        """
        Testing for one null input
        """
        input_validation = self.algo.validate_input()
        self.assertEqual(input_validation, {'error': 'inputs are not entered'})


class GameTestInputTypeInvalidInput1(unittest.TestCase):
    """
    class for testing alignment game
    """

    def setUp(self):
        self.algo = AlignmentGame('AB++', 'AB-C', 2, -1, -1)

    def tearDown(self):
        del self.algo

    def test_invalid_input_sequence(self):
        """
        Testing for invalid input sequence
        """
        input_validation = self.algo.validate_input()
        self.assertEqual(input_validation, {'error': 'Invalid input sequence'})


class GameTestInputTypeInvalidInput2(unittest.TestCase):
    """
    class for testing alignment game
    """

    def setUp(self):
        self.algo = AlignmentGame('ACCC', 'AB-C', 2, -1, "a")

    def tearDown(self):
        del self.algo

    def test_invalid_input_panalty(self):
        """
        Testing for invalid input panalty
        """
        input_validation = self.algo.validate_input()
        self.assertEqual(input_validation, {'error': 'Invalid input sequence'})


# class GameTest_BackendBehave(unittest.TestCase):

#     # executed prior to each test
#     def setUp(self):

#         self.testing_data = {
#                     "seq_a":"AABBC",
#                     "seq_b": "AABAB",
#                     "match": 2,
#                     "mismatch": -1,
#                     "gap": -1
#                 }

#     ###############
#     #### tests ####
#     ###############


#     # Ensure that game behave correctly given the correct credentials
#     def test_correct_input_behave(self):
#         tester = app.test_client(self)
#         response = tester.post(
#             path='/game/align',
#             # data=json.dumps(self.testing_data),
#             data=dict(seq_a="AA-BC", seq_b="AAB-C", match="1", mismatch="-1", gap="-1"),
#             content_type='application/json'
#             )

#         self.assertEqual(response.status_code,200)
#         # self.assertEqual(int(response.json()['result']['score']), 1)
