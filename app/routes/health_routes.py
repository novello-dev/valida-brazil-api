# Import dependencies
from flask import Blueprint, jsonify

# Health check endpoint
health_bp = Blueprint('health', __name__)

@health_bp.route('/health', methods=['GET'])
def health_check():
    # Simple OK response
    return jsonify({"status": "ok"}), 200
