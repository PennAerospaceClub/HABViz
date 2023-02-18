from ipywidgets.widgets.trait_types import date_from_json
import plotly.express as px
import plotly.graph_objs as go
import pandas as pd
import numpy as np
from scipy import stats

def tracker(data_path, columns):
    df = pd.read_csv(data_path)

    lat = df[columns[0]]
    lon = df[columns[1]]
    height = df[columns[2]]
  
    df = {'a': lat, 'b': lon, 'c' : height}
    fig = px.scatter_3d(df, x = 'a', y = 'b', z = 'c', color = "c", color_continuous_scale=px.colors.sequential.Bluered.reverse())
    fig.show()


# df = pd.read_csv (r'Test Data Analysis.csv')
# df = pd.DataFrame(df, columns= ['latitude (degrees)','longitude (degrees)', 'altitude (meters)'])

# df = df[(np.abs(stats.zscore(df)) < 3).all(axis=1)]

# lat = df['latitude (degrees)']
# lon = df['longitude (degrees)']
# height = df['altitude (meters)']
# tracker(lat, lon, height)