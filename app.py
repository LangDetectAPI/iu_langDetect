import random

import requests
from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


# route avec la méthode POST
@app.route('/prompt', methods=['POST'])
def prompt():
    # get the message body the form
    text = request.get_json().get('text', None)

    # check if the text is empty
    if text is None or text.strip() == '':
        return 'Veuillez entrer un texte'

    return call_api(text)


def build_response(payload: dict):
    """ Build the response

    Args:
        payload (dict): The response from the API

        Returns:
            str: The response to send to the user
    """

    print("message:", payload)

    lang = payload.get('lang', None)
    proba = payload.get('proba', None)

    return f'<b>La langue detectée :</b> {lang} <br> <b>score :</b> {proba}'


def call_api(text):
    """ Call the API and return the response
        POST https://apicoc.com/detect
        {
            "text": "Bonjour, comment ça va ?"
        }
    """
    # call the API
    url = 'http://127.0.0.1:8080/detect'
    json = {'text': text}
    response = requests.post(url=url, json=json)

    # check if the response is 200
    if response.status_code != 200:
        return 'Une erreur est survenue'

    # get the response
    payload = response.json()

    return build_response(payload)


if __name__ == '__main__':
    app.run(debug=True, port=5002)

# Run the app
# $ python app.py
