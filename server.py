from flask import Flask, request, jsonify
import Narutogamebot_stats_persistent  # pour importer tes fonctions

app = Flask(__name__)

@app.route('/')
def home():
    return "Bot stats API is running!"

@app.route('/save', methods=['POST'])
def save_stats():
    data = request.json
    # Appelle ici les fonctions de ton script si besoin
    print("Reçu :", data)
    return jsonify({"status": "ok", "received": data})