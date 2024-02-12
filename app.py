import random

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
    print("message:", payload)
    list_lang = ['fr', 'en', 'es', 'de', 'it', 'pt', 'nl', 'pl', 'ru', 'ja', 'zh', 'ar']
    lang = random.choice(list_lang)
    return f'<b>La langue detectée est :</b> {lang}'


def call_api(payload):
    return build_response(payload)


if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000)

# Run the app
# $ python app.py
