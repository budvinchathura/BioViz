from flask import Blueprint,jsonify,request
from PairAlign.Algorithms.NW import NW
from PairAlign.Algorithms.SW import SW

pair_align_bp = Blueprint('pair_align_bp', __name__)

@pair_align_bp.route('/nw',methods=['POST'])
def pair_nw():
    request_data = request.get_json()
    match = int(request_data['match'])
    mismatch = int(request_data['mismatch'])
    gap = int(request_data['gap'])
    results = NW(request_data['seq_a'],request_data['seq_b'],match,mismatch,gap)
    
    return jsonify({'results':results})

@pair_align_bp.route('/sw',methods=['POST'])
def pair_sw():
    request_data = request.get_json()
    match = int(request_data['match'])
    mismatch = int(request_data['mismatch'])
    gap = int(request_data['gap'])
    results = SW(request_data['seq_a'],request_data['seq_b'],match,mismatch,gap)
    
    return jsonify({'results':results})
