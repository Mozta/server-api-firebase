import firebase_admin
from firebase_admin import credentials, firestore
import datetime
import requests

# Remplaza la URL por la de tu servidor
url = 'http://127.0.0.1:8080/add'

def send_data_api(temp):
    try:
        print("Enviando datos...\n")
        response = requests.post(url, json={"temp": temp})
        print(response.content)

    except requests.exceptions.HTTPError as err:
        print("Error...\n")
        raise SystemExit(err)


send_data_api(38)