from pathlib import Path
from typing import Dict

import requests


class Client:

    def __init__(self):
        self._url = Client._get_config()["url"]

    @staticmethod
    def _get_config() -> Dict[str, Any]:
        config_path = Path(__file__).parent / "config" / "config.JSON"
        return json.loads(config_path.read_text())  # type: ignore[no-any-return]

    def call_detect(self, text):
        """ Call the API and return the response"""
        # call the API
        url = self._url
        json = {'text': text}
        response = requests.post(url=url, json=json)

        # check if the response is 200
        if response.status_code != 200:
            return 'Une erreur est survenue'

        # get the response
        payload = response.json()

        return payload


