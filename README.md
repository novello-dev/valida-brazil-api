# Valida Brasil
[![Ask DeepWiki](https://devin.ai/assets/askdeepwiki.png)](https://deepwiki.com/novello-dev/valida-brasil)

A simple and lightweight API service for validating common Brazilian document formats.

## Features

-   CPF (Cadastro de Pessoas Físicas) validation
-   CNPJ (Cadastro Nacional da Pessoa Jurídica) validation

## Setup and Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/novello-dev/valida-brasil.git
    cd valida-brasil
    ```

2.  **Create and activate a virtual environment (recommended):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3.  **Install the dependencies:**
    The project dependencies are managed in the `requirements` directory. To install them, run:
    ```bash
    pip install -r requirements
    ```

## Running the API Locally

Once the dependencies are installed, you can start the API server using an ASGI server like Uvicorn.

```bash
uvicorn app.main:app --reload
```

The API will be available at `http://127.0.0.1:8000`.

## API Endpoints

The API provides endpoints for various validation types. Requests and responses are in JSON format.

### CPF Validation

-   **Endpoint:** `POST /validate/cpf`
-   **Description:** Validates a Brazilian CPF number. The CPF can be sent with or without punctuation.
-   **Request Body:**
    ```json
    {
      "cpf": "123.456.789-00"
    }
    ```
-   **Success Response (200 OK):**
    ```json
    {
      "document": "12345678900",
      "valid": true
    }
    ```
-   **Error Response (422 Unprocessable Entity):**
    ```json
    {
      "document": "12345678901",
      "valid": false,
      "message": "Invalid CPF"
    }
    ```

### CNPJ Validation

-   **Endpoint:** `POST /validate/cnpj`
-   **Description:** Validates a Brazilian CNPJ number. The CNPJ can be sent with or without punctuation.
-   **Request Body:**
    ```json
    {
      "cnpj": "11.222.333/0001-81"
    }
    ```
-   **Success Response (200 OK):**
    ```json
    {
      "document": "11222333000181",
      "valid": true
    }
    ```
-   **Error Response (422 Unprocessable Entity):**
    ```json
    {
      "document": "11222333000182",
      "valid": false,
      "message": "Invalid CNPJ"
    }
    ```

### Example usage with cURL

You can test the endpoints using a tool like `cURL`.

**CPF:**
```bash
curl -X POST "http://127.0.0.1:8000/validate/cpf" \
     -H "Content-Type: application/json" \
     -d '{"cpf": "12345678900"}'
```

**CNPJ:**
```bash
curl -X POST "http://127.0.0.1:8000/validate/cnpj" \
     -H "Content-Type: application/json" \
     -d '{"cnpj": "11222333000181"}'