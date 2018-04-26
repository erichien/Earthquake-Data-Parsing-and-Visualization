import json
import requests


def load(URL, FILEPATH):
    """
    Loads GeoJSON data.
    Requests latest file from https://earthquake.usgs.gov, or load local backup file.
    """
    try:
        resp = requests.get(URL)
        resp_json = resp.json()

        with open(FILEPATH, 'w') as f:
            json.dump(resp_json, f)
        return resp_json

    # use local backup file
    except Exception:
        with open(FILEPATH, 'r') as f:
            return json.load(f)
