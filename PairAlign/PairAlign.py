from flask import Blueprint, jsonify, request
from PairAlign.Algorithms.NW import NW
from PairAlign.Algorithms.SW import SW
from PairAlign.Algorithms.NW_extended import NWExtended

from PairAlign.Executer import Executer

pair_align_bp = Blueprint('pair_align_bp', __name__)


@pair_align_bp.route('/nw', methods=['POST'])
def pair_nw():
    request_data = request.get_json()
    match = int(request_data['match'])
    mismatch = int(request_data['mismatch'])
    gap = int(request_data['gap'])
    nw_algorithm = NW(request_data['seq_a'][:100],
                      request_data['seq_b'][:100], match, mismatch, gap)

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

    sw_algorithm = SW(request_data['seq_a'][:100],
                      request_data['seq_b'][:100], match, mismatch, gap)

    executer = Executer(sw_algorithm)
    result = executer.get_results()

    resp = {'result': result}


    return jsonify(resp)

@pair_align_bp.route('/nw-affine', methods=['POST'])
def pair_nw_affine():
    request_data = request.get_json()
    match = int(request_data['match'])
    mismatch = int(request_data['mismatch'])
    opening_gap = int(request_data['opening_gap'])
    extending_gap = int(request_data['extending_gap'])

    nw_affine_algorithm = NWExtended(request_data['seq_a'][:100],
                      request_data['seq_b'][:100], match, mismatch, opening_gap, extending_gap)

    executer = Executer(nw_affine_algorithm)
    result = executer.get_results()

    resp = {'result': result}


    return jsonify(resp)