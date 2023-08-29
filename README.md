# Forex-News-Analysis and Forcasting Project

![image](https://github.com/tkhendrix22/Forex-News-Analysis/assets/113871039/f13e2520-cdef-42ee-a5fc-2b09d084199f)




By: Troy Hendrickson

# Project Overview
This project is a fusion of machine learning and time series forecasting techniques aimed at predicting the sentiment (positive or negative) of Forex news articles. By combining traditional machine learning models and the Facebook Prophet time series forecasting model, the project provides insights into how news impacts the foreign exchange market.

# Business Overview
Predicting the influence of Forex news articles is vital for traders and investors looking to forecast market movements driven by economic events. The project addresses this challenge by developing two predictive models—one centered on machine learning and another leveraging time series forecasting. These models offer actionable insights to guide trading strategies.

# Data Analysis
The project utilizes a comprehensive dataset comprising Forex news articles and their associated attributes, including advanced metrics and economic indicators. Each column corresponds to a distinct economic indicator or event, along with the sentiment associated with the news. Spanning from 2010 to 2023, the dataset captures historical market trends and sentiment shifts. The data was collected from [Kaggle](https://www.kaggle.com/datasets/saeedaghasoleimani/forex-fundumental-news-for-usd). 

### Columns Overview:
`Date`: Date of the news article

`ISM Manufacturing PMI`: Institute for Supply Management Manufacturing Purchasing Managers Index

`ISM Services PMI`: Institute for Supply Management Non-Manufacturing Purchasing Managers Index

`Housing Starts`: Number of housing construction projects started

`Non-Farm Employment Change`: Change in the number of employed people

`Unemployment Rate`: Percentage of unemployed individuals in the labor force

`Consumer Price Index (CPI)`: Measure of inflation

`Producer Price Index (PPI)`: Measure of average change in selling prices

`Retail Sales`: Total retail sales of consumer goods

# Exploratory Data Analysis
During the exploratory data analysis phase, historical trends in the sentiment of each economic indicator are uncovered. Over the period from 2010 to 2023, the analysis demonstrates that the market sentiment for most indicators has predominantly been positive. These insights underscore the importance of each economic indicator as significant news that influences market sentiment.

![CPI pic](https://github.com/tkhendrix22/Forex-News-Analysis/assets/113871039/3ff08224-0ee1-4a24-91ef-b0d11434e1ef)



![nonfarm](https://github.com/tkhendrix22/Forex-News-Analysis/assets/113871039/a7a1d0fa-0034-4d27-a1f6-2a8753311991)


![unemployment](https://github.com/tkhendrix22/Forex-News-Analysis/assets/113871039/cfef469d-0578-4aa9-a3f0-173f3f722ecf)



![pos neg ppi](https://github.com/tkhendrix22/Forex-News-Analysis/assets/113871039/37ed3dd9-e25f-43f4-ab0d-46cfccd9aece)


# Machine Learning Modeling
The project employs established machine learning models, including the Random Forest classifier and K-Nearest Neighbors (KNN), to predict news sentiment. Each model is trained on historical data to forecast whether forthcoming news articles will yield a positive or negative market impact. Model performance is evaluated using metrics such as precision, recall, and F1-score.

### Machine Learning Results:
<u> Random Forest Model </u>:
Results for different columns:

`ISM Manufacturing PMI`: Precision, Recall, F1-score, and Accuracy are all 1.00

`ISM Services PMI`: Precision, Recall, F1-score, and Accuracy are all 1.00

`Housing Starts`: Precision, Recall, F1-score, and Accuracy are all 1.00

`Non-Farm Employment Change`: Precision, Recall, F1-score, and Accuracy indicate high performance

`Unemployment Rate`: Precision, Recall, F1-score, and Accuracy are all 1.00

`Consumer Price Index (CPI)`: Precision, Recall, F1-score, and Accuracy indicate solid performance

`Producer Price Index (PPI)`: Precision, Recall, F1-score, and Accuracy show satisfactory results

`Retail Sales`: Precision, Recall, F1-score, and Accuracy show good performance


<u> K-Nearest Neighbors (KNN) Model </u>:
Results for different columns:

`ISM Manufacturing PMI`: Precision, Recall, F1-score, and Accuracy are all 1.00

`ISM Services PMI`: Precision, Recall, F1-score, and Accuracy are all 1.00

`Housing Starts`: Precision, Recall, F1-score, and Accuracy are all 1.00

`Non-Farm Employment Change`: Precision, Recall, F1-score, and Accuracy indicate high performance

`Unemployment Rate`: Precision, Recall, F1-score, and Accuracy are all 1.00

`Consumer Price Index (CPI)`: Precision, Recall, F1-score, and Accuracy show satisfactory results

`Producer Price Index (PPI)`: Precision, Recall, F1-score, and Accuracy show good performance

`Retail Sales`: Precision, Recall, F1-score, and Accuracy show moderate performance

# Time Series Forecasting with Facebook Prophet
In addition to machine learning, the project employs the Facebook Prophet time series forecasting model to predict sentiment trends over time. This approach takes into account temporal dependencies and seasonal patterns. For each economic indicator, the model is trained, and users can input a future date to forecast whether the sentiment will be positive or negative.

# Time Series Forecasting Results:
The Facebook Prophet time series model provides forecasts of sentiment trends over time for each economic indicator.

# Limitations & Next Steps
The models have limitations, including the potential influence of external factors not captured in the dataset and the need for real-time data integration. Future steps may involve improving model accuracy by incorporating real-time data, refining feature engineering techniques, and building an interactive platform to provide real-time sentiment predictions for traders.

# Observations & Conclusions
This project seamlessly combines machine learning and time series forecasting to predict the sentiment of Forex news articles. By integrating these two approaches, it offers comprehensive insights into the influence of economic indicators and events on the foreign exchange market. These insights empower traders with valuable information to make informed decisions and devise effective trading strategies.

Disclaimer: The content of this project is for informational purposes only and should not be considered as financial advice or trading recommendations. Forex trading involves risk, and individuals should conduct thorough research and seek professional advice before making trading decisions.

