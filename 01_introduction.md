# 2018 SFEI RMP Data Challenge

## Machine Learning Analysis of Nutrients in the SF Bay

### Author: Walter Yu, P.E.

### Abstract

Nutrients present in the SF Bay are linked to higher algae blooms and toxins which result in lower dissolved oxygen (DO), negative impacts to fish habitat and lower overall water quality. This topic featured in the 2017 Pulse of the Bay$^{1}$, which included data analysis of SF Bay monitoring results; as a result, this study continues such analysis with machine learning to identify other potential insights from nutrient monitoring data.

### Introduction

This study outlines the data, methods and results used to identify trends in the SF Estuary Institute (SFEI) Regional Monitoring Program (RMP) water quality and toxicity monitoring results from the Contaminant Data Display and Download (CD3) database$^{2}$. Specifically, it seeks to answer the following questions:

1. Which data attributes most influence DO, chlorophyll-a (Chl-a), ammonium (as N) and ammonia (as NH^3) levels?
2. Does identifying these attributes lead to insights regarding possible causes for increasing nutrients?
3. What trends were identified with this study?
4. What are some next steps and recommendations based on additional analysis?

### Data Source

This study analyzes the DO, chlorophyll-a (Chl-a), ammonium (as N) and ammonia (as NH^3) from the CD3 dataset. Specifically, nutrient monitoring results were analyzed to identify potential insights. The data was retrieved from the CD3 database by filtering for basic water quality and toxicity.

### Tools and Process

The tools and process listed below were used to analyze data and provide recommendations:

1. Jupyter Notebook - Exploratory data cleaning and organization were completed using this notebook; machine learning models were run in Microsoft Azure Machine Learning (AML) Studio
2. Python Modules - The required modules are listed within the source code and need to be installed in order to run this notebook.
3. Microsoft Azure Machine Learning (ML) Studio - ML Studio was used to identify important data features, compare machine learning algorithms and publish results.
