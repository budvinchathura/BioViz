from flask import Blueprint, jsonify, request
from PairAlign.Algorithms.NW import NW
from PairAlign.Algorithms.SW import SW

from PairAlign.Executer import Executer

pair_align_bp = Blueprint('pair_align_bp', __name__)


@pair_align_bp.route('/nw', methods=['POST'])
def pair_nw():
    request_data = request.get_json()
    match = int(request_data['match'])
    mismatch = int(request_data['mismatch'])
    gap = int(request_data['gap'])
    nw_algorithm = NW(request_data['seq_a'],
                      request_data['seq_b'], match, mismatch, gap)

    executer = Executer(nw_algorithm)
    result = executer.get_results()

    resp = {'result': result}

    return jsonify(resp)


@pair_align_bp.route('/sw', methods=['POST'])
def pair_sw():
    request_data = request.get_json()
    match = int(request_data['match'])
    mismatch = int(request_data['mismatch'])
    gap = int(request_data['gap'])
    output_data = SW(request_data['seq_a'],
                     request_data['seq_b'], match, mismatch, gap)
    resp = {'result': {}}
    resp['result']['algn_a'] = output_data[2]
    resp['result']['algn_b'] = output_data[3]
    resp['result']['score_matrix'] = output_data[0]
    resp['result']['direction_matrix'] = output_data[1]

    return jsonify(resp)
