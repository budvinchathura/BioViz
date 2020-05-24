from flask import Blueprint, jsonify, request

from MSA.Executer import Executer
from MSA.Algorithms.Progressive import Progressive
from MSA.Algorithms.ProgressiveOptimal import ProgressiveOptimal
from MSA.Validators.msa_validator import validate_msa_progessive
from MSA.Validators.msa_validator import validate_msa_progessive_optimal

msa_bp = Blueprint('msa_bp', __name__)


@msa_bp.route('/progressive', methods=['POST'])
def progressive():
    """
    function handler for /progressive route.
    returns json output
    """
    request_data = request.get_json()
    status, errors = validate_msa_progessive(request_data)
    if not status:
        return jsonify(errors), 400

    match = int(request_data['match'])
    mismatch = int(request_data['mismatch'])
    gap = int(request_data['gap'])
    progressive_algorithm = Progressive(
        request_data['sequences'], request_data['order'], match, mismatch, gap)

    executer = Executer(progressive_algorithm)
    result = executer.get_results()

    resp = {'result': result}
    return jsonify(resp)


@msa_bp.route('/progressive-optimal', methods=['POST'])
def progressive_optimal():
    """
    function handler for /progressive-optimal route.
    returns json output
    """
    request_data = request.get_json()
    status, errors = validate_msa_progessive_optimal(request_data)
    if not status:
        return jsonify(errors), 400

    match = int(request_data['match'])
    mismatch = int(request_data['mismatch'])
    gap = int(request_data['gap'])
    progressive_algorithm = ProgressiveOptimal(
        request_data['sequences'], match, mismatch, gap)

    executer = Executer(progressive_algorithm)
    result = executer.get_results()

    resp = {'result': result}
    return jsonify(resp)
