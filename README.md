# Valida Brasil
[![Status](https://img.shields.io/badge/status-active-brightgreen)](#)
[![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-2.3+-orange.svg)](https://flask.palletsprojects.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

A simple and lightweight API built with **Flask** that validates and retrieves Brazilian address data using the **ViaCEP API**.  
It provides clean, UTF-8 encoded JSON responses, ideal for small projects, tests, or API integration learning.

---

## 🚀 Features

- `GET /health` → Health check endpoint  
- `GET /address?cep=XXXXX-XXX` → Fetches address info from ViaCEP  
- Returns formatted JSON with correct accentuation  
- Lightweight and easy to deploy  

---

## ⚙️ Installation

To set up and run the project locally:

    git clone https://github.com/novello-dev/valida-brasil.git
    cd valida-brasil
    python -m venv .venv

    # Windows (PowerShell)
    .\.venv\Scripts\Activate.ps1

    # macOS/Linux
    source .venv/bin/activate

    pip install -r requirements.txt

---

## ▶️ Running the API

To start the Flask development server:

    # Windows
    python app\main.py

    # macOS/Linux
    python app/main.py

Once running, the API will be available at:

    http://127.0.0.1:5000

---

## 📡 API Endpoints

### 🩺 `/health`

Checks if the API is running.

**Method:** GET  
**Response:**

    {
      "status": "ok"
    }

---

### 📍 `/address`

Retrieves full address data from a given Brazilian postal code (CEP).

**Method:** GET  
**Query parameter:** `cep` — CEP with or without hyphen  

Example:

    http://127.0.0.1:5000/address?cep=01001-000

**Success (200 OK):**

    {
      "cep": "01001-000",
      "logradouro": "Praça da Sé",
      "complemento": "lado ímpar",
      "bairro": "Sé",
      "localidade": "São Paulo",
      "uf": "SP",
      "estado": "São Paulo",
      "regiao": "Sudeste",
      "ddd": "11",
      "siafi": "7107"
    }

**Error responses:**

| Code | Message |
|------|----------|
| 400 | CEP must have 8 digits |
| 404 | CEP not found |
| 502 | Failed to reach API ViaCEP |

> 💡 Tip: Browsers may show escaped Unicode (like `\u00e9`).  
> Use Postman, Insomnia, or a terminal command to see formatted accents:
>
>     curl -s "http://127.0.0.1:5000/address?cep=01001-000" | python -m json.tool

---

## 🧰 Tech Stack

- **Language:** Python 3.11+
- **Framework:** Flask  
- **HTTP Client:** Requests  
- **External API:** ViaCEP  

---

## 🛠️ Roadmap

- [ ] Add `/validate/cpf` endpoint  
- [ ] Add `/validate/cnpj` endpoint  
- [ ] Add SQLite cache support  
- [ ] Deploy on Render/Railway  

---

## 👨‍💻 Author

**João Pedro Novello**  
🔗 [github.com/novello-dev](https://github.com/novello-dev)

---

## 🪪 License

This project is licensed under the **MIT License** — see the LICENSE file for details.
