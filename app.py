import os
from flask import Flask, request, jsonify
import requests
import firebase_admin
from firebase_admin import credentials, firestore
import datetime

app = Flask(__name__)
# Configuraciones para firebase
cred = credentials.Certificate('serviceAccountKey.json')
fire = firebase_admin.initialize_app(cred)
db = firestore.client()
sensor_ref = db.collection('historicos')

@app.route('/')
def home():
    return "<p>Bienvenido a mi API con firebase!</p>"


@app.route('/add', methods=['POST'])
def create():
    try:
        temp = request.json['temp']
        new_data = {'temp':temp, 'created': datetime.datetime.now()}
        sensor_ref.document().set(new_data)
        return jsonify({"success": True}), 200
    except Exception as e:
        return f"An Error Occurred: {e}"

PORT = int(os.environ.get("PORT",8080))
if __name__ == '__main__':
    app.run(threaded=True, host='0.0.0.0', port=PORT)