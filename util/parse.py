import pandas as pd
from time import time
from config import Config
from datetime import datetime


def _test_json_properties(data):
    assert ('features' in data), 'key features not in json data'
    assert ('properties' in data['features']), 'key properties not in feature'
    assert ('time' in data['features']['properties']), 'key time not in feature[\'properties\']'
    assert ('place' in data['features']['properties']), 'key place not in feature[\'properties\']'
    assert ('mag' in data['features']['properties']), 'key mag not in feature[\'properties\']'


def _test_df_columns(df):
    assert ('properties.time' in df), 'column properties.time not in dataframe'
    assert ('properties.place' in df), 'column properties.place not in dataframe'
    assert ('properties.mag' in df), 'column properties.mag not in dataframe'


def _time_secs(timestamp):
    current_time = int(time())
    current_time_digits = len(str(current_time))
    timestamp_digits = len(str(timestamp))
    if timestamp_digits > current_time_digits:
        return int(timestamp) / float(10 ** (timestamp_digits - current_time_digits))
    else:
        return int(timestamp)


def parse_naive(data, place):
    """
    Naively parse the GeoJSON by looping through the dictionary, and output earthquake data of the given location in the desired format.
    """

    # _test_json_properties(data)
    location, location_code = place, Config.STATE_CODES[place]

    # find earthquake records of the given location using state name and abbreviation
    at_location = lambda x: (location in x['properties']['place']) or \
                            (location_code in x['properties']['place'])
    # keep properties relevant to output
    select_fields = lambda x: {'time': x['properties']['time'],
                               'place': x['properties']['place'],
                               'magnitude': x['properties']['mag']}
    # format data for output
    format_place = lambda x: str(x)
    format_mag = lambda x: 'Magnitude: {}'.format(x)
    format_time = lambda x: datetime.utcfromtimestamp(_time_secs(x)).strftime('%Y-%m-%dT%H:%M:%S') + '+00:00'
    format_output = lambda x: '{} | {} | {}'.format(format_time(x['time']),
                                                    format_place(x['place']),
                                                    format_mag(x['magnitude']))

    local = filter(at_location, data['features'])
    local = map(select_fields, local)
    local_sorted = sorted(local, key=lambda x: (x['magnitude'], x['time']))
    results = map(format_output, local_sorted)

    return results


def parse_pandas(data, place):
    """
    Utilize the Pandas library to manipulate the data, and output earthquake data of the given location in the desired format.
    """

    location, location_code = place, Config.STATE_CODES[place]

    # _test_json_properties(data)
    # normalize features and store as DataFrame
    df = pd.io.json.json_normalize(data['features'])
    _test_df_columns(df)
    # keep columns relevant to output
    df = df[['properties.time', 'properties.place', 'properties.mag']]
    # find earthquake records of the given location using state name and abbreviation
    df_local = df[df['properties.place'].str.contains('{}|{}'.format(location, location_code))]
    # sort by magnitude and time of record
    df_local_sorted = df_local.sort_values(['properties.mag', 'properties.time'])

    # format data for output
    format_place = lambda x: str(x)
    format_time = lambda x: datetime.utcfromtimestamp(_time_secs(x)).strftime('%Y-%m-%dT%H:%M:%S') + '+00:00'
    format_mag = lambda x: 'Magnitude: {}'.format(x)
    format_output = lambda (idx, row): '{} | {} | {}'.format(format_time(row['properties.time']),
                                                    format_place(row['properties.place']),
                                                    format_mag(row['properties.mag']))

    results = map(format_output, df_local_sorted.iterrows())
    return results
