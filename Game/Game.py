from flask import Blueprint,jsonify,request

from Game.Games.AlignmentGame import AlignmentGame


game_bp = Blueprint('game_bp', __name__)


@game_bp.route('/align',methods=['POST'])
def game_score():
    request_data = request.get_json()
    algn_a = str(request_data['algn_a'])
    algn_b = str(request_data['algn_b'])
    match = int(request_data['match'])
    mismatch = int(request_data['mismatch'])
    gap = int(request_data['gap'])
    alignment_game = AlignmentGame(algn_a,algn_b,match,mismatch,gap)
    alignment_game.calculate_score()
    resp = {'result':{}}
    
    resp['result']['game_score'] = alignment_game.get_score()
    resp['result']['alignment_result'] = alignment_game.get_align_result()


    return jsonify(resp)