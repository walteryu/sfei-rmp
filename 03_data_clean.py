import csv
import pandas as pd
import numpy as np
import scipy
from scipy import stats
pd.options.mode.chained_assignment = None

# Plotting packages; documentation consulted for examples:
# Reference: https://seaborn.pydata.org/examples/index.html
import seaborn as sns
import matplotlib.pyplot as plt
plt.rcParams['figure.figsize'] = (15.0, 7.5)

# Statistics packages
import statsmodels
from statsmodels.formula.api import ols

# Image import packages
from IPython.display import Image
from IPython.core.display import HTML

# Exploratory data analysis to evaluate attributes of interest:

# Load csv data
cd3_df = pd.DataFrame.from_csv('./data/cd3-water-quality-toxicity.csv', index_col=None)

# Filter for 'programcode' = 'SF Bay RMP':
rmp_df = cd3_df.loc[cd3_df['programcode'] == 'SF Bay RMP']
# Verify count after filtering data each time:
# print(rmp_df.describe())

# Drop all zero result values:
rmp_df.loc[rmp_df.result > 0]
# Verify count after filtering data each time:
# print(rmp_df.describe())

# Drop null values since they do not contribute to total:
rmp_df.dropna(subset=['result'], inplace=True)
# Verify count after filtering data each time:
# print(rmp_df.describe())

# Print reduced dataset to csv:
rmp_df.to_csv('./data/cd3-rmp-toxicity.csv')

# Convert to datetime for time series analysis:
rmp_df.sampledate = pd.to_datetime(rmp_df.sampledate)

# Copy year/month into separate column as numeric values
rmp_df['year'] = rmp_df['sampledate'].dt.year
rmp_df['month'] = rmp_df['sampledate'].dt.month
rmp_df['day'] = rmp_df['sampledate'].dt.day

print('Script done running!')
