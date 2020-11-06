import requests
import json

class CoronaApi(object):
    """
    API for current corona statistics
    """

    urlAll: str = 'https://onemocneni-aktualne.mzcr.cz/api/v2/covid-19/nakaza.min.json'

    def __init__(self):
        pass

    def get(self) -> dict:
        """
        Returns a dictionary containing response from api.
        """
        response = requests.get(self.urlAll)
        return json.loads(response.text)