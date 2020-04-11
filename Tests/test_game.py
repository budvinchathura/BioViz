# from app import app 
from flask import Flask
import unittest

from Game.Games.AlignmentGame import AlignmentGame

app = Flask(__name__)

class GameTest(unittest.TestCase):

    # executed prior to each test
    def setUp(self):

        self.algo = AlignmentGame('AAAB', 'AAB-', 2, -1, -1)


    # executed after each test
    def tearDown(self):
        del self.algo

    ###############
    #### tests ####
    ###############

    #Ensure that user inputs get correctly
    def test_inputs(self):
        input_seq = self.algo.get_input_alignments()
        input_panalties = self.algo.get_input_panalty()
        self.assertEqual(input_seq[0], 'AAAB')
        self.assertEqual(input_seq[1], 'AAB-')
        self.assertEqual(input_panalties[0],2)
        self.assertEqual(input_panalties[1],-1)
        self.assertEqual(input_panalties[2],-1)

    # Ensure that game results get correctly
    def test_main_page(self):
        self.algo.calculate_score()
        score = self.algo.get_score()
        alignment_result = self.algo.get_align_result()
        self.assertEqual(score, 2)
        self.assertEqual(alignment_result, ['match','match','mismatch','gap'])

    # Ensure that flask was setup correctly
    def test_index(self):
        tester = app.test_client(self)
        response = tester.get('/game', content_type='html/text') # ------- get req is not seted yet
        self.assertEqual(response.status_code, 200)

    # Ensure that the game page load correctly
    def test_game_page_loads(self):
        tester = app.test_client(self)
        response = tester.get('/game', content_type='html/text')
        # ----------need to write 'Game' inside the game page frontend --------
        self.assertTrue(b'Game' in response.data)

    # Ensure that game behave correctly given the correct credentials
    def test_correct_input_behave(self):
        tester = app.test_client(self)
        response = tester.post(
            '/game', 
            data=dict(algn_a="AAAB", algn_b="AAB-", match="1", mismatch="-1", gap="-1"), 
            follow_redirects=True
            )
        # --------need to write 'Score is' in frontend page when submit the values ---------
        self.assertIn(b'Score is', response.data)

    # Ensure that game behave correctly given the incorrect credentials
    def test_incorrect_input_behave(self):
        tester = app.test_client(self)
        response = tester.post(
            '/game', 
            data=dict(algn_a="AA+B", algn_b="AAB-", match="1", mismatch="a", gap="-1"), 
            follow_redirects=True
            )
        # -------need to write 'Input is invalid' in frontend page when submit the values --------
        self.assertIn(b'Input is invalid', response.data)







    if __name__ == '__main__':
        unittest.main()
