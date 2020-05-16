from flask import Blueprint, jsonify, request
from PairAlign.Algorithms.NW import NW
from PairAlign.Algorithms.SW import SW
from PairAlign.Algorithms.NW_extended import NWExtended
from PairAlign.Algorithms.SW_extended import SWExtended

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
    
    opening_gap = int(request_data['opening_gap'])
    extending_gap = int(request_data['extending_gap'])
    priority = request_data['priority']
    seq_type = request_data['seq_type']
    sub_mat = request_data['sub_mat']
    match = int(request_data['match']) if sub_mat == 'DEFAULT' else 0
    mismatch = int(request_data['mismatch']) if sub_mat == 'DEFAULT' else 0

    nw_affine_algorithm = NWExtended(seq_type, sub_mat, request_data['seq_a'][:100],
                      request_data['seq_b'][:100], match, mismatch, opening_gap, extending_gap, priority)

    executer = Executer(nw_affine_algorithm)
    result = executer.get_results()

    resp = {'result': result}


    return jsonify(resp)

@pair_align_bp.route('/sw-affine', methods=['POST'])
def pair_sw_affine():
    request_data = request.get_json()
    
    opening_gap = int(request_data['opening_gap'])
    extending_gap = int(request_data['extending_gap'])
    priority = request_data['priority']
    seq_type = request_data['seq_type']
    sub_mat = request_data['sub_mat']
    match = int(request_data['match']) if sub_mat == 'DEFAULT' else 0
    mismatch = int(request_data['mismatch']) if sub_mat == 'DEFAULT' else 0

    sw_affine_algorithm = SWExtended(seq_type, sub_mat, request_data['seq_a'][:100],
                      request_data['seq_b'][:100], match, mismatch, opening_gap, extending_gap, priority)

    executer = Executer(sw_affine_algorithm)
    result = executer.get_results()

    resp = {'result': result}


    return jsonify(resp)