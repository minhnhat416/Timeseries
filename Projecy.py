# I Data Preparation
# 1. Load Time Series Data

from pandas import read_csv

series = read_csv(r'D:\UEL\Nam_3\Hoc_ki_6\timeseries\Data\Taichinh.csv', header=0, index_col=0, parse_dates=True,
squeeze=True)
series.insert(0,'row_id',range(0, 0 + len(series)), allow_duplicates=False) # Add row_id column to dataset
print(series.head())
print(series.columns)
print("Dataframe before filtering: ", len(series.index))

code_need = ['E1VFVN30', 'FUESSV50', 'FUCTVGF3','FUCVREIT', 'HCM']
series = series[series.code.isin(code_need)]
print("Dataframe after filtering: ", len(series.index))



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