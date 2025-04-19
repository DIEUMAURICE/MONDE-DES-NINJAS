from flask import Flask, request, jsonify
import os

app = Flask(__name__)

@app.route('/')
def home():
    return "API is running on Render"

@app.route('/save', methods=['POST'])
def save_stats():
    data = request.json
    print("Données reçues :", data)
    # Ici tu peux appeler des fonctions de Narutogamebot_stats_persistent.py si besoin
    return jsonify({"status": "ok", "received": data})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 10000))
    app.run(host='0.0.0.0', port=port)
