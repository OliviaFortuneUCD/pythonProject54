import pandas as pd

import numpy as np
#Code here takes in a csv file and reads it.

netflix_data = pd.read_csv("Netflix_titles.csv", index_col = 0)

#Column headings to get rid of dots

pd.options.display.max_columns = None
pd.options.display.max_rows = None
pd.set_option('display.max_colwidth', None)


#print(netflix_data)
#print(netflix_data.head())
print(netflix_data.shape)
print(netflix_data.columns)