from flask import Blueprint, jsonify, request



msa_bp = Blueprint('msa_bp', __name__)


@msa_bp.route('/progressive', methods=['POST'])
def progressive():
    return jsonify({})



@msa_bp.route('/progressive-optimal', methods=['POST'])
def progressive_optimal():
    return jsonify({})