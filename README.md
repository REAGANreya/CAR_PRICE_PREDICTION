🚗 Car Price Prediction System

A machine learning data product that predicts car prices based on selected vehicle characteristics.

📌 Project Overview

The Car Price Prediction System is a machine learning project developed to estimate vehicle prices using data-driven methods.

The project follows a practical data science workflow, from understanding and preparing the dataset to training, evaluating, and deploying a machine learning model through a Streamlit application.

🎯 Project Objective

The main objective is to provide users with a simple way to estimate the price of a car based on selected vehicle characteristics.

🔄 Data Science Workflow

The project followed these major stages:

1. Data Understanding — examining the dataset, variables, data types, and categories.
2. Data Cleaning — checking for missing values, duplicates, and data consistency.
3. Data Preparation — preparing categorical and numerical variables for modelling.
4. Feature Selection — selecting relevant features for the prediction task.
5. Model Development — training different regression algorithms.
6. Model Evaluation — comparing models using MAE, MSE, and R².
7. Model Selection — selecting the Random Forest Regressor based on the evaluation results.
8. Deployment — integrating the trained model into a Streamlit data product.

🤖 Models Evaluated

The following regression models were tested:

- Linear Regression
- Ordinary Least Squares (OLS)
- Polynomial Regression
- Random Forest Regressor

📊 Model Results

Model| MAE| MSE| R²
Random Forest Regressor| 1,943.20| 7,635,113.38| 0.8955
Linear Regression| 2,379.82| 12,273,132.20| 0.8707
OLS| 2,379.94| 12,272,658.26| 0.8707
Polynomial Regression| 2,107.75| 19,554,355.28| 0.7146

The Random Forest Regressor was selected for the deployed application based on its evaluation results.

🌐 Streamlit Data Product

The trained model was integrated into a Streamlit application.

The application provides:

- 🚗 Car price prediction
- 📊 Data visualizations
- 🏢 Company-based predictions
- 📥 CSV prediction functionality

🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- Seaborn
- Plotly
- Streamlit
- Joblib
- Jupyter Notebook

📁 Repository Structure

car-price-prediction/
│
├── final.py
├── model.joblib
├── preprocessor.joblib
├── clean_car_data.csv
├── CarPrice_Assignment.csv
├── requirements.txt
│
├── Data_UNDERSTANDING.ipynb
├── LinearRegression.ipynb
├── Ordinary Least Squares(OLS).ipynb
├── Polynomial Regression.ipynb
├── Random Forest Regressor.ipynb
│
├── RandomForestRegressor.docx
├── UICT.jpg
└── README.md

▶️ Run the Application Locally

Clone the repository and install the required dependencies:

pip install -r requirements.txt

Then start the Streamlit application:

streamlit run final.py

The application will open in your browser.

📚 Project Documentation

The repository contains the Jupyter notebooks used during the different stages of the project, including data understanding, regression modelling, model evaluation, and Random Forest modelling.

🎓 Academic Context

This project was developed as part of my practical learning in Data Science Management & Analytics (DSMA) at the Uganda Institute of Information and Communications Technology (UICT).

👨‍💻 Author

Yabiraku Reagan

Data Science Student | Machine Learning & Data Analytics

Programme: Diploma in Data Science Management & Analytics (DSMA)
Institution: Uganda Institute of Information and Communications Technology (UICT)
Expected Graduation: 2027
Location: Kampala, Uganda

GitHub: REAGANreya
Email: yabirakureagan1@gmail.com
