from flask import Blueprint, jsonify, request

from MSA.Executer import Executer
from MSA.Algorithms.Progressive import Progressive

msa_bp = Blueprint('msa_bp', __name__)


@msa_bp.route('/progressive', methods=['POST'])
def progressive():
    request_data = request.get_json()
    # print(request_data)
    match = int(request_data['match'])
    mismatch = int(request_data['mismatch'])
    gap = int(request_data['gap'])
    progressive_algorithm = Progressive(
        request_data['sequences'], match, mismatch, gap)

    executer = Executer(progressive_algorithm)
    result = executer.get_results()

    resp = {'result': result}
    return jsonify(resp)


@msa_bp.route('/progressive-optimal', methods=['POST'])
def progressive_optimal():
    return jsonify({})
