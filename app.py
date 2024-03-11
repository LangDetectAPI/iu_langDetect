
from flask import Flask
from flask import render_template
from flask import request

from api import Client

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

    return Client().call_detect(text)


if __name__ == '__main__':
    app.run(debug=True, port=5002)

# Run the app
# $ python app.py
