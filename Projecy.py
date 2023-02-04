# I Data Preparation
# 1. Load Time Series Data

from pandas import read_csv # Load libraries

series = read_csv(r'Taichinh.csv', header=0, index_col=0, parse_dates=True,
squeeze=True)
series.insert(0,'row_id',range(0, 0 + len(series)), allow_duplicates=False) # Add row_id column to dataset
print(series.head())
print(series.columns)
print("Dataframe before filtering: ", len(series.index))

# filter data by 5 codes
code_need = ['E1VFVN30', 'FUESSV50', 'FUCTVGF3','FUCVREIT', 'HCM']
series_filter = series[series.code.isin(code_need)]
print("Dataframe after filtering: ", len(series_filter.index))

# series.to_csv('data_filter.csv', index=False) # Export data after filter


print(series_filter.info()) # Information About the Data

# Descriptive Statistics about the Data
varible_describe =['close','average', 'adClose', 'adAverage','nmVolume',
                   'nmValue', 'ptVolume', 'ptValue', 'change', 'adChange', 'pctChange']
print(series_filter[varible_describe].describe())

# 2.  Exploring Time Series Data

# II. Feature Engineering
# 1, Feature Engineering for Time Series

# III. Visualization
# 1. Line plots
# 2. Histograms and Density Plots
# 3. Box and Whisker Plots
# 4. Heat Maps
# 5. Lag Plots or Scatter Plots
# 6. Autocorrelation Plots.