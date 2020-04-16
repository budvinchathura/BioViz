from flask import Flask
import unittest
import json

from Game.Games.AlignmentGame import AlignmentGame

app = Flask(__name__)

class GameTest(unittest.TestCase):

    # executed prior to each test
    def setUp(self):

        self.algo = AlignmentGame('AAAC', 'AAC-', 2, -1, -1)


    # executed after each test
    def tearDown(self):
        del self.algo

    ###############
    #### tests ####
    ###############

    #Ensure that user inputs sequence get correctly
    def test_input_sequence(self):
        input_seq = self.algo.get_input_alignments()
        self.assertEqual(input_seq[0], 'AAAC')
        self.assertEqual(input_seq[1], 'AAC-')


    # Ensure that user panalties get correcly
    def test_input_panalties(self):
        input_panalties = self.algo.get_input_panalty()
        self.assertEqual(input_panalties[0],2)
        self.assertEqual(input_panalties[1],-1)
        self.assertEqual(input_panalties[2],-1)


    # Ensure that game score get correctly
    def test_calculate_score(self):
        input_validation = self.algo.validate_input()
        self.assertEqual(input_validation, {'error': 'None'})
        self.algo.calculate_score()
        score = self.algo.get_score()
        self.assertEqual(score, 2)
        

    # Ensure that game alignment result get correctly
    def test_alignment_result(self):
        self.algo.calculate_score()
        alignment_result = self.algo.get_align_result()
        self.assertEqual(alignment_result, ['match','match','mismatch','gap'])



class GameTest_InputType1(unittest.TestCase):

    # executed prior to each test
    def setUp(self):

        self.algo = AlignmentGame('AACTU', 'AC', 4, -1, -1)


    # executed after each test
    def tearDown(self):
        del self.algo

    ###############
    #### tests ####
    ###############

    # Ensure that game score get correctly for diferent type of inputs 1
    def test_calculate_score(self):
        self.algo.calculate_score()
        score = self.algo.get_score()
        self.assertEqual(score, 0)
        
    # Ensure that game alignment result get correctly
    def test_alignment_result(self):
        self.algo.calculate_score()
        alignment_result = self.algo.get_align_result()
        self.assertEqual(alignment_result, ['match','mismatch','gap','gap','gap'])
    
    # Testing for validation
    def test_validation(self):
        input_validation = self.algo.validate_input()
        self.assertEqual(input_validation, {'error': 'None'})



class GameTest_InputType2(unittest.TestCase):

    # executed prior to each test
    def setUp(self):

        self.algo = AlignmentGame('C--TA', 'CACTU', 2, -1, -1)


    # executed after each test
    def tearDown(self):
        del self.algo

    ###############
    #### tests ####
    ###############

    # Ensure that game score get correctly for diferent type of inputs 1
    def test_get_score2(self):
        self.algo.calculate_score()
        score = self.algo.get_score()
        self.assertEqual(score, 1)
        
    # Ensure that game alignment result get correctly
    def test_alignment_result(self):
        self.algo.calculate_score()
        alignment_result = self.algo.get_align_result()
        self.assertEqual(alignment_result, ['match','gap','gap','match','mismatch'])
    
    # Testing for validation
    def test_validation(self):
        input_validation = self.algo.validate_input()
        self.assertEqual(input_validation, {'error': 'None'})



class GameTest_InputType3(unittest.TestCase):

    # executed prior to each test
    def setUp(self):

        self.algo = AlignmentGame('CUTTAC', '-', 2, -1, -1)


    # executed after each test
    def tearDown(self):
        del self.algo

    ###############
    #### tests ####
    ###############


    # Ensure that game score get correctly for diferent type of inputs 1
    def test_get_score3(self):
        self.algo.calculate_score()
        score = self.algo.get_score()
        self.assertEqual(score, -6)
        
    # Ensure that game alignment result get correctly
    def test_alignment_result(self):
        self.algo.calculate_score()
        alignment_result = self.algo.get_align_result()
        self.assertEqual(alignment_result, ['gap','gap','gap','gap','gap','gap'])
    
    # Testing for validation
    def test_validation(self):
        input_validation = self.algo.validate_input()
        self.assertEqual(input_validation, {'error': 'None'})



class GameTest_InputType_NullInput1(unittest.TestCase):

    # executed prior to each test
    def setUp(self):

        self.algo = AlignmentGame('', '', 2, -1, -1)


    # executed after each test
    def tearDown(self):
        del self.algo

    ###############
    #### tests ####
    ###############


    # Testing for for both null inputs
    def test_null_input1(self):
        input_validation = self.algo.validate_input()
        self.assertEqual(input_validation, {'error':'inputs are not entered'})



class GameTest_InputType_NullInput2(unittest.TestCase):

    # executed prior to each test
    def setUp(self):

        self.algo = AlignmentGame('AA-TU', '', 2, -1, -1)


    # executed after each test
    def tearDown(self):
        del self.algo

    ###############
    #### tests ####
    ###############


    # Testing for one null input 
    def test_null_input2(self):  
        input_validation = self.algo.validate_input()
        self.assertEqual(input_validation, {'error':'inputs are not entered'})  



class GameTest_InputType_InvalidInput1(unittest.TestCase):

    # executed prior to each test
    def setUp(self):

        self.algo = AlignmentGame('AB++', 'AB-C', 2, -1, -1)


    # executed after each test
    def tearDown(self):
        del self.algo

    ###############
    #### tests ####
    ###############


    # Testing for invalid input sequence
    def test_invalid_input_sequence(self):
        input_validation = self.algo.validate_input()
        self.assertEqual(input_validation, {'error': 'Invalid input sequence'})



class GameTest_InputType_InvalidInput1(unittest.TestCase):

    # executed prior to each test
    def setUp(self):

        self.algo = AlignmentGame('ACCC', 'AB-C', 2, -1, "a")


    # executed after each test
    def tearDown(self):
        del self.algo

    ###############
    #### tests ####
    ###############


    # Testing for invalid input panalty
    def test_invalid_input_panalty(self):
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




if __name__ == '__main__':
        unittest.main()
