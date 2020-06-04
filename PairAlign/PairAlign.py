from flask import Blueprint, jsonify, request
from PairAlign.Algorithms.NW import NW
from PairAlign.Algorithms.SW import SW
from PairAlign.Algorithms.NW_extended import NWExtended
from PairAlign.Algorithms.SW_extended import SWExtended
from PairAlign.Validators.basic import validate_pair_align_basic
from PairAlign.Validators.extended import validate_pair_align_extended

from PairAlign.Executer import Executer

PAIR_ALIGN_BP = Blueprint('PAIR_ALIGN_BP', __name__)


@PAIR_ALIGN_BP.route('/nw', methods=['POST'])
def pair_nw():
    ''' Handle NW endpoint'''
    request_data = request.get_json()
    status, errors = validate_pair_align_basic(request_data)
    if not status:
        return jsonify(errors), 400

    match = int(request_data['match'])
    mismatch = int(request_data['mismatch'])
    gap = int(request_data['gap'])
    nw_algorithm = NW(request_data['seq_a'][:1000],
                      request_data['seq_b'][:1000], match, mismatch, gap)

    executer = Executer(nw_algorithm)
    result = executer.get_results()

    resp = {'result': result}

    return jsonify(resp)


@PAIR_ALIGN_BP.route('/sw', methods=['POST'])
def pair_sw():
    ''' Handle SW endpoint'''
    request_data = request.get_json()
    status, errors = validate_pair_align_basic(request_data)
    if not status:
        return jsonify(errors), 400

    match = int(request_data['match'])
    mismatch = int(request_data['mismatch'])
    gap = int(request_data['gap'])

    sw_algorithm = SW(request_data['seq_a'][:1000],
                      request_data['seq_b'][:1000], match, mismatch, gap)

    executer = Executer(sw_algorithm)
    result = executer.get_results()

    resp = {'result': result}

    return jsonify(resp)


@PAIR_ALIGN_BP.route('/nw-affine', methods=['POST'])
def pair_nw_affine():
    ''' Handle NW Affine enpoint'''
    request_data = request.get_json()
    status, errors = validate_pair_align_extended(request_data)
    if not status:
        return jsonify(errors), 400

    opening_gap = int(request_data['opening_gap'])
    extending_gap = int(request_data['extending_gap'])
    priority = request_data['priority']
    seq_type = request_data['seq_type']
    sub_mat = request_data['sub_mat']
    match = int(request_data['match']) if sub_mat == 'DEFAULT' else 0
    mismatch = int(request_data['mismatch']) if sub_mat == 'DEFAULT' else 0

    nw_affine_algorithm = NWExtended(seq_type, sub_mat,
                                     request_data['seq_a'][:1000], request_data['seq_b'][:1000],
                                     match, mismatch, opening_gap, extending_gap, priority)

    executer = Executer(nw_affine_algorithm)
    result = executer.get_results()

    resp = {'result': result}

    return jsonify(resp)


@PAIR_ALIGN_BP.route('/sw-affine', methods=['POST'])
def pair_sw_affine():
    ''' Handle SW Affine endpoint'''
    request_data = request.get_json()
    status, errors = validate_pair_align_extended(request_data)
    if not status:
        return jsonify(errors), 400

    opening_gap = int(request_data['opening_gap'])
    extending_gap = int(request_data['extending_gap'])
    priority = request_data['priority']
    seq_type = request_data['seq_type']
    sub_mat = request_data['sub_mat']
    match = int(request_data['match']) if sub_mat == 'DEFAULT' else 0
    mismatch = int(request_data['mismatch']) if sub_mat == 'DEFAULT' else 0

    sw_affine_algorithm = SWExtended(seq_type, sub_mat,
                                     request_data['seq_a'][:1000], request_data['seq_b'][:1000],
                                     match, mismatch, opening_gap, extending_gap, priority)

    executer = Executer(sw_affine_algorithm)
    result = executer.get_results()

    resp = {'result': result}
    return jsonify(resp)
