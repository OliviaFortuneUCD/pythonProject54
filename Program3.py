import pandas as pd

import numpy as np


netflix_data = pd.read_csv("Netflix_titles.csv", index_col = 0)
pd.options.display.max_columns = None
pd.options.display.max_rows = None
pd.set_option('display.max_colwidth', None)

#Count the missing data
missing_values_count = netflix_data.isnull().sum()
#Print columns missing data from 0 to 5.
print(missing_values_count[0:5])

# finding total number of null values
print(netflix_data .isnull().sum())