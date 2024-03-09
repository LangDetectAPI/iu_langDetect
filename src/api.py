

import requests


def detect_language(payload):
    """call the language detection API

    Returns:
        str: the detected language

    
    """

    # call the API
    response = requests.post(
         "https://api.local.com/detect",
         headers={
           "Content-Type": "application/json",
        },
       json={"text": payload},
     )

    response.raise_for_status()
    return response.json()["language"]
    return "fr"





def build_response(payload):
    """build the response message"""

    #lang = detect_language(payload)

    list_lang = ['fr', 'en', 'es', 'de', 'it', 'pt', 'nl', 'pl', 'ru', 'ja', 'zh', 'ar']
    lang = random.choice(list_lang)
    return f'<b>La langue detectée est :</b> {lang}'
