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


def build_response(payload):
    """ Build the response

    Args:
        payload (dict): The response from the API

        Returns:
            str: The response to send to the user
    """

    print("message:", payload)
    list_lang = ['fr', 'en', 'es', 'de', 'it', 'pt', 'nl', 'pl', 'ru', 'ja', 'zh', 'ar']
    lang = random.choice(list_lang)
    return f'<b>La langue detectée est :</b> {lang}'


def call_api(text):
    """ Call the API and return the response
        POST https://apicoc.com/detect
        {
            "text": "Bonjour, comment ça va ?"
        }
    """
    # call the API
    url = 'https://apicoc.com/detect'
    json = {'text': text}
    response = requests.post(url=url, json=json)

    # check if the response is 200
    if response.status_code != 200:
        return 'Une erreur est survenue'

    # get the response
    payload = response.json()

    return build_response(payload)


if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000)

# Run the app
# $ python app.py
