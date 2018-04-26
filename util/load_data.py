import json
import requests


def _check_json_properties(data):
    # make sure structure of json data is suitable for parsing

    assert ('features' in data), 'key features not in json data'

    for feature in data['features']:
        assert ('properties' in feature), 'key properties not in feature'
        assert ('time' in feature['properties']), 'key time not in feature[\'properties\']'
        assert ('place' in feature['properties']), 'key place not in feature[\'properties\']'
        assert ('mag' in feature['properties']), 'key mag not in feature[\'properties\']'


def load(URL, FILEPATH):
    """
    Loads GeoJSON data.
    Requests latest file from https://earthquake.usgs.gov, or load local backup file.
    """
    try:
        resp = requests.get(URL)
        resp_json = resp.json()
        _check_json_properties(resp_json)

        with open(FILEPATH, 'w') as f:
            json.dump(resp_json, f)
        return resp_json

    # use local backup file
    except Exception:
        with open(FILEPATH, 'r') as f:
            data = json.load(f)
            _check_json_properties(data)
            return data
