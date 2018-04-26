# Earthquake Data Parsing and Visualization    



For a comprehensive documentation and results, please visit: https://earthquake-data.herokuapp.com/ 

  

## Problem Description

USGS (US Geological Survey) publishes earthquake data. 

Here’s a feed spanning all domestic earthquakes from the past month: https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_month.geojson

Using this JSON feed:

1. identify every earthquake in California from past month, 

2. list them by increasing magnitude 

3. and finally output in a format resembling the following e.g.: 

   2017-07-13T22:32:48+00:00 | 15km SE of Mammoth Lakes, California | Magnitude: 0.92

   2017-07-13T22:49:58+00:00 | 8km ENE of Mammoth Lakes, California | Magnitude: 0.92

   2017-07-13T22:37:52+00:00 | 12km E of Mammoth Lakes, California | Magnitude: 0.95

   2017-07-13T20:43:37+00:00 | 3km NW of Greenville, California | Magnitude: 1

   2017-07-13T22:31:04+00:00 | 11km E of Mammoth Lakes, California | Magnitude: 1.31

   2017-07-13T22:45:28+00:00 | 37km SE of Bridgeport, California | Magnitude: 1.7

   2017-07-13T22:54:30+00:00 | 3km SE of Atascadero, California | Magnitude: 2.04

   2017-07-13T22:09:53+00:00 | 41km SW of Ferndale, California | Magnitude: 2.76

​    

## Process

### Key Tasks

1. Request GeoJSON file:
   1. The file needs to be requested to produce an up-to-date result
2. Parse GeoJSON to get the relevant information from file for output:
   1. Select earthquakes with location info containing California or CA
   2. Extract time, location, and magnitude info from input data
3. Format output: 
   1. Convert unix timestamp to the format as defined in the requirement
   2. Sort the collected results by magnitude (ascending), then time (ascending)

​    

### Ambiguity and Assumptions 

1. In the description, it asks us to process data from the past month, however the link leads to earthquake data from the past week. I sticked with data from the past month.
2. Earthquakes sometimes are recorded in one state, but the sources are in another. I categorized them by the location the earthquakes were recorded.
3. The type (cause) of the earthquake can also be further divided into earquake, chemical explosion, etc. I decided not to focus on these minor details.

  

## Approaches

I used Python to complete the tasks, and experimented with a few approaches to process the data:

1. Naively loop through the entire json file
2. Use Lambda, Map, and Filter functions to obtain the desired values from input data
3. Convert json to Pandas DataFrame
4. Utilize third-party Python libraries (GeoPandas, Geojsonio) to parse the GeoJSON file

Pandas DataFrame provides more legible structure, and is somewhat easier to manipulate compared to json (nested dictionary). Results show that DataFrame has better performance during parsing and data selection compared to naively looping through the json (dict), but lags behind when outputting with the iterrows() methods. Using Lambda, Map, and Filter functions has the best performance overall while still being scalable. GeoPandas is similar to Pandas, but has simpler ways to import json data and visualize results. Geojsonio is out-of-date.

  

## Additional Feature

I took the liberty of adding a function to make this program more comprehensive. In addition to California, users are able to query earthquake data for any given state within the United States.

  

## Visualization

Through my conversations with Chris and Ahmad, I learned that the team often have to show data with charts in the web apps. It is important to keep our users' needs in mind, and I believe proper visualization turns data into insights, and can help our users understand the data better and faster. For non-technical users, it will also be easier for them to navigate a GUI on a web page instead of the CLI.

Therefore, I included three methods for visualizing the earthquake data: GeoPandas (Python), Plotly (Python), and D3.js (JavaScript).

  

## Installation    

Please install requirements using pip:

```pip install -r requirements.txt
pip install -r requirements.txt
```

  

## Usage  

In the util folder, run

```
python earthquake_data.py -m mode_name -l library_name -p us_state_name
```



There are three arguments for the program: `--mode`, `--library`, `--place` (all are required).
For `--mode`, there are two options: `log`, and `plot`.

For `--libraries`, there are four (conditional) options: `naive`, `pandas`, `geopandas`, and `plotly`.

The `--place` is the desired location of the earthquake data to output. This argument should be the name of a US state in Sentence case.

In `log` mode, the user can choose to process the data with one of two libraries(approaches): `naive` and `pandas`. 
In `plot` mode, the user can choose to plot the data with one of two libraries: `geopandas` and `plotly`

  

## Example  

To log all earthquakes in California state in the past month:

```python
python earthquake_data.py -m log -l naive -p California
```

To plot the data of earthquakes in Oregon state in the past month on a map:

```python
python earthquake_data.py -m plot -l plotly -p Oregon
```

  