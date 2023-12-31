## For Data Analysis Report - Visit analysis.ipynb
## For Model training - Visit model.ipynb
### For report see in section with name report.pdf
#### Interactive Dashboard - https://app.powerbi.com/groups/me/reports/352b29f8-661b-489d-bbb5-cc118f8b65b9/ReportSection?experience=power-bi
Predicting Customer Churn in a Telecommunications Company

Objective
The primary aim of this project is to develop a predictive model that identifies customers at risk of churning, enabling proactive measures to retain them and reduce churn rates.

Understanding our Data
•	Customers who left within the last month – the column is called Churn<br>
•	Services that each customer has signed up for – phone, multiple lines, internet, online security, online backup, device protection, tech support, and streaming TV and movies<br>
•	Customer account information – how long they’ve been a customer, contract, payment method, paperless billing, monthly charges, and total charges<br>
•	Demographic info about customers – gender, age range, and if they have partners and dependents<br>
<img width="953" alt="image" src="https://github.com/Rayansh0071505/Predicting-Customer-Churn-in-a-Telecommunications-Company/assets/98272246/72b5e6ac-90b1-4caf-8b1c-e4ed320f75f0">





# Predicting Customer Churn in a Telecommunications Company

## Objective
The primary aim of this project is to develop a predictive model that identifies customers at risk of churning, enabling proactive measures to retain them and reduce churn rates.

## Project Components
- [Exploratory Data Analysis (EDA)](#exploratory-data-analysis-eda)
- [Churn Prediction Model](#churn-prediction-model)
- [Conclusion and Recommendations](#conclusion-and-recommendations)

## Exploratory Data Analysis (EDA)
### Data Analysis Report
- [Visit analysis.ipynb](https://github.com/Rayansh0071505/Predicting-Customer-Churn-in-a-Telecommunications-Company/blob/master/analysis.ipynb)
- [EDA Report PDF](https://github.com/Rayansh0071505/Predicting-Customer-Churn-in-a-Telecommunications-Company/blob/master/Report%20-%20Predicting%20Customer%20Churn%20in%20a%20Telecommunications%20Company.pdf)
- Summary of key insights from EDA:

#### Churn Distribution
- Discuss churn rates and implications.
  
#### Demographic Insights
- Insights on gender distribution, age groups, and their impact on churn.

#### Billing and Payment Preference
- Distribution among payment methods and their relation to churn.

#### Service-related Insights
- Analysis of internet service types, service bundles, and their correlation with churn.

## Churn Prediction Model
### Model Training
- [Visit model.ipynb](https://github.com/Rayansh0071505/Predicting-Customer-Churn-in-a-Telecommunications-Company/blob/master/model.ipynb)
- Data collection and preprocessing steps.
- Machine learning algorithms considered and implemented.
- Model training results and evaluation metrics.

## Conclusion and Recommendations
- Summary of findings from EDA and model insights.
- Recommendations based on identified insights for reducing churn.

## Interactive Dashboard
- [Link to Power BI Dashboard](https://app.powerbi.com/groups/me/reports/352b29f8-661b-489d-bbb5-cc118f8b65b9/ReportSection?experience=power-bi)
- Interactive visualization of key metrics and trends.



•	Fine-tuned hyperparameters using techniques like cross-validation or grid search

Model Training Result

•	'Logistic Regression': 0.7570048309178744<br>
•	'Decision Tree': 0.8893719806763285,<br>
•	'Random Forest': 0.9135265700483092,<br>
•	'Gradient Boosting': 0.8014492753623188,<br>
•	'SVM': 0.5743961352657004,<br>
•	'K-Nearest Neighbors': 0.6714975845410628,<br>
•	'Naive Bayes': 0.7333333333333333<br>




Model Evaluation

Performance Metrics:

Evaluated model performance using appropriate metrics: Accuracy, precision, recall, F1-score, ROC-AUC, etc.

Random Forest classifier gives the best accuracy and result and good performance compared the performance of different models.

 



Evaluation

•	Accuracy: 0.9159<br>
•	Precision: 0.8743<br>
•	Recall: 0.9698<br>
•	F1-score: 0.9196<br>





