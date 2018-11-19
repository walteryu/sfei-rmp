### Data Cleaning

Data cleaning was completed prior to analysis as follows:

1. Removed empty and missing values since they may cause errors during analysis.
2. Removed negative values since they may skew summary statistics and results.

After data cleaning, summary statistics were prepared for the dataset per table and bar chart shown below to separate results by analyte into its own dataframe for machine learning analysis.

### Exploratory Data Analysis

Chlorophyll-A, DO and ammonia (as N, NH3 and NH3 unionized) were selected as monitoring results for additional analysis. However, only Chlorophyll-A and dissolved oxygen were used for machine learning analysis since the monitoring results were all zero values with exception of 1 result.

The Chlorophyll-A and DO datasets were extracted into separate files and modified as follows:

1. Added "cd3sampleid" to ID column for future reference or analysis.
2. Added "resultscore" as categorical variable for classification algorithms.
