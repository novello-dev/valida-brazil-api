# Import dependencies
import requests

def get_address_data(cep):
    # Build ViaCEP URL
    url = f"https://viacep.com.br/ws/{cep}/json/"

    try:
        # HTTP request to ViaCEP
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()

        # Invalid CEP case from provider
        if data.get('erro'):
            return {"error": "CEP not found"}, 404

        return data, 200

    except requests.Timeout:
        # Network timeout
        return {"error": "Request timed out"}, 504

    except requests.RequestException:
        # Any other request error
        return {"error": "Failed to reach ViaCEP API"}, 502
