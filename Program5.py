import pandas as pd

import numpy as np


netflix_data = pd.read_csv("Netflix_titles.csv", index_col = 0)
pd.options.display.max_columns = None
pd.options.display.max_rows = None
pd.set_option('display.max_colwidth', None)

# filling null values of country with most occuring country
netflix_data.country.fillna("United_states",inplace= True)


print(netflix_data[['country']])