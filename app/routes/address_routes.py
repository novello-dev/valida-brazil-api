# Import dependencies
from flask import Blueprint, request, jsonify
from app.services.viacep_service import get_address_data
from app.utils.validators import validate_cep

# Address endpoints
address_bp = Blueprint('address', __name__)

@address_bp.route('/address', methods=['GET'])
def get_address():
    # Read query param
    cep = request.args.get('cep')

    # Require CEP
    if not cep:
        return jsonify({"error": "The 'cep' parameter is required"}), 400

    # Validate format
    is_valid, result = validate_cep(cep)
    if not is_valid:
        return jsonify({"error": result}), 400

    # Fetch from ViaCEP and forward status code
    data, status_code = get_address_data(result)
    return jsonify(data), status_code
