import requests
import json
from typing import Dict


# MVC pattern - model part
class Gas(object):

    def __init__(self) -> None:
        super().__init__()

    def get_prices(self) -> Dict:
        """
        Get gas prices for Canada
        :return: Dictionary of gas prices per province
        """

        url = "https://canadian-gas-prices.p.rapidapi.com/canada"

        headers = {
            "X-RapidAPI-Key": "e55b25d3a9msheda0da5c1d266dcp175371jsna6bfb18f28b7",
            "X-RapidAPI-Host": "canadian-gas-prices.p.rapidapi.com"
        }

        response = requests.request("GET", url, headers=headers)
        gas_dict = json.loads(response.text)
        return gas_dict["prices"]
