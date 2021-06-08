import pandas as pd

import numpy as np
import os




netflix_data = pd.read_csv("Netflix_titles.csv", index_col = 0)
pd.options.display.max_columns = None
pd.options.display.max_rows = None
pd.set_option('display.max_colwidth', None)


recent_data=netflix_data[netflix_data["release_year"]<2000]
print(recent_data)
