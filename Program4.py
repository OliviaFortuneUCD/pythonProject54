import pandas as pd

import numpy as np


netflix_data = pd.read_csv("Netflix_titles.csv", index_col = 0)
pd.options.display.max_columns = None
pd.options.display.max_rows = None
pd.set_option('display.max_colwidth', None)

#drop the director.

netflix_data=netflix_data.drop(["director"],axis=1)
# finding total number of null values
print(netflix_data .isnull().sum())