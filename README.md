# Earthquake Data Parsing and Visualization    

## Installation    

Please install requirements using pip:

```pip install -r requirements.txt

```



## Usage  

In the util folder, run

```
python earthquake_data.py -m mode_name -l library_name -p us_state_name
```



There are three arguments for the program: `--mode`, `--library`, `--place` (all are required).
For `--mode`, there are two options: `log`, and `plot`.

For `--libraries`, there are four (conditional) options: `naive`, `pandas`, `geopands`, and `plotly`.

The `--place` is the desired location of the earthquake data to output. This argument should be the name of a US state in Sentence case.

In `log` mode, the user can choose to process the data with one of two libraries(approaches): `naive` and `pandas`. 
In `plot` mode, the user can choose to plot the data with one of two libraries: `geopands` and `plotly`



## Example  

To log all earthquakes in California state in the past month:

```python
python earthquake_data.py -m log -l naive -p California
```

To plot the data of earthquakes in Oregon state in the past month on a map:

```python
python earthquake_data.py -m plot -l plotly -p Oregon
```

