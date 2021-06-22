"""Script created to experiment with different python packages and methods.
A data envrionment can be set up using the req.txt file."""

import os, itertools, time
import pandas as pd
import numpy as np
from pandas import DataFrame as df

dates1 = pd.date_range("2020-06-01","2021-05-01",freq="MS")
data1 = df({"col1":[1,2,1,2,1,2,1,2,1,2,1,2],"col2": [3,3,3,4,4,4,3,3,3,4,4,4],"col3":["testing"]},index=dates1)
dates2 = pd.date_range("2020-06-01","2021-05-01",freq="MS")
data2 = df({"col1":[3,2,1,3,2,1,3,2,1,3,2,1],"col2": [5,5,5,6,6,6,5,5,5,7,7,7]},index=dates2)
data = pd.concat([data1,data2]).reset_index()
pivoted = data.pivot_table(columns='col1')
pivoted2 = data.pivot(columns='col2')
idx = pd.IndexSlice

print(data)
print(pivoted2.reset_index().melt(id_vars=["col2"],value_vars=["col3"]))