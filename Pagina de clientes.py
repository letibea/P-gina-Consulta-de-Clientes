from flask import Flask, jsonify, request
from flask_cors import CORS
from datetime import datetime

app = Flask(__name__)
CORS(app)

# dados em memória só para teste
clientes = [
    {"id": 1, "nome": "João da Silva", "email": "joao@email.com", "data_cadastro": str(datetime.now())},
    {"id": 2, "nome": "Maria Souza", "email": "maria@email.com", "data_cadastro": str(datetime.now())}
]

@app.route("/api/clientes", methods=["GET"])
def get_clientes():
    return jsonify(clientes)

if __name__ == "__main__":
    app.run(debug=True, port=5000)
