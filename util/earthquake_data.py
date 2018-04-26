"""
This file parses input arguments and output results based on the chosen library

"""

from config import Config
from load_data import load
from logger import logger
from argparse import ArgumentParser
from parse import parse_naive, parse_pandas
from plot import plot_geopandas, plot_plotly


def main(args):

    mode, lib, place = args.mode, args.lib, args.place
    PRESETS = {
                ('log', 'naive'): parse_naive,
                ('log', 'pandas'): parse_pandas,
                ('plot', 'geopandas'): plot_geopandas,
                ('plot', 'plotly'): plot_plotly
            }

    if mode == 'log' and not (lib == 'naive' or lib == 'pandas'):
        parser.error('--library can only be \'naive\' or \'pandas\' when --mode is \'log\'.')
    if mode == 'plot' and not (lib == 'geopandas' or lib == 'plotly'):
        parser.error('--library can only be \'geopandas\' or \'plotly\' when --mode is \'plot\'.')

    data = load(Config.URL, Config.FILEPATH)

    if mode == 'log':
        parse = PRESETS[('log', lib)]
        results = parse(data, place)
        logger(results, place)
    else:
        plot = PRESETS[('plot', lib)]
        plot(data, place)


if __name__ == '__main__':

    parser = ArgumentParser()
    parser.add_argument("-m", "--mode",
                        dest="mode",
                        default='log',
                        choices=['log', 'plot'],
                        required=True,
                        help="log or plot the earthquake data.")
    parser.add_argument("-l", "--library",
                        dest="lib",
                        default='naive',
                        choices=['naive', 'pandas', 'geopandas', 'plotly'],
                        required=True,
                        help="library used to process data.")
    parser.add_argument("-p", "--place",
                        dest="place",
                        default='California',
                        choices=Config.VALID_PLACES,
                        required=True,
                        help="the location of the earthquake data to output in capital case")

    args = parser.parse_args()
    main(args)
