# Python2-Final-Project
 
This is a interactive dash project showing Covid-19 cases and death rate in United States.

This project uses an interactive bar plot to show Covid cases. User can filter data by simply entering conditions in the panel. e.g. enter >50000 in box below cases.

Also, each barplot is segmented according to county. Therefore, users can easily find out which county has the most cases and are able to further examine it by filtering the data to the state it belongs to. 



# Dataset and data cleaning

The data comes from Kaggle: https://www.kaggle.com/headsortails/covid19-us-county-jhu-data-demographics

It's a large and comprehensive dataset. I filtered out three days as representative dates in Cleaned_data. In the final dash application, I only use the date "2020-11-30".



# Barplot and Choropleth Map

Barplot is interactive and user can modify the plot they want to see by filtering the data.

Choropleth Map shows the death rate of each county. Counties with higher death rate will represent in a brighter color. 
