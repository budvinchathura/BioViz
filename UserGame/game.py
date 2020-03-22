from flask import Blueprint,jsonify,request

from UserGame.Algorithm.GameScore import GS


game_bp = Blueprint('game_bp', __name__)


@game_bp.route('/GS',methods=['POST'])
def game_score():
    request_data = request.get_json()
    match = int(request_data['match'])
    mismatch = int(request_data['mismatch'])
    gap = int(request_data['gap'])
    output_data = GS(request_data['seq_a'],request_data['seq_b'],match,mismatch,gap)
    resp = {'result':{}}
    
    resp['result']['game_score'] = output_data


    return jsonify(resp)