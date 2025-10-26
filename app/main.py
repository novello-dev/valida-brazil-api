# Importing dependencies
from flask import Flask, request, jsonify, make_response
import re
import requests

app = Flask(__name__)

# Configure JSON to display accents properly
app.config["JSON_AS_ASCII"] = False


@app.get("/health")
def health():
    """Healthcheck endpoint"""
    return jsonify({"status": "ok"}), 200


@app.get("/address")
def address():
    """Fetch address data from ViaCEP based on a given CEP"""
    cep = request.args.get("cep", "")
    cep_digits = re.sub(r"\D", "", cep)  # Remove any non-numeric characters

    # Validate CEP length
    if len(cep_digits) != 8:
        return jsonify({"error": "CEP deve ter 8 dígitos"}), 400

    # Request data from ViaCEP API
    try:
        r = requests.get(f"https://viacep.com.br/ws/{cep_digits}/json/", timeout=5)
    except requests.RequestException:
        return jsonify({"error": "Failed to reach ViaCEP API"}), 502

    data = r.json()

    # Handle invalid CEPs
    if data.get("erro"):
        return jsonify({"error": "CEP não encontrado"}), 404

    # Create a formatted JSON response
    response = make_response(jsonify(data), 200)
    response.headers["Content-Type"] = "application/json; charset=utf-8"
    return response


if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)
