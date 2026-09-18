🚗 Car Price Prediction System

A machine learning data product that predicts car prices based on selected vehicle characteristics.

📌 Project Overview

This project uses machine learning to estimate the price of a car based on selected features.

The project covers the main stages of a data science workflow, including:

- Data understanding
- Data cleaning
- Exploratory data analysis
- Data preprocessing
- Feature selection
- Machine learning model training
- Model comparison and evaluation
- Model deployment using Streamlit

🤖 Machine Learning

Several regression models were evaluated during the modelling stage, including:

- Linear Regression
- Random Forest Regression
- Ordinary Least Squares (OLS)
- Polynomial Regression

The Random Forest Regressor was selected based on its performance on the evaluation metrics.

Model Performance

Model| MAE| MSE| R²
Random Forest| 1943.20| 7,635,113.38| 0.8955
Linear Regression| 2379.82| 12,273,132.20| 0.8707
OLS| 2379.94| 12,272,658.26| 0.8707
Polynomial Regression| 2107.75| 19,554,355.28| 0.7146

🛠️ Technologies

- Python
- Pandas
- NumPy
- Scikit-learn
- Jupyter Notebook
- Streamlit
- Joblib

🌐 Data Product

The trained model was integrated into a Streamlit application that allows users to interact with the prediction system through a simple interface.

The application includes:

- 🚗 Car price prediction
- 📊 Data visualizations
- 🏢 Company-based predictions
- 📥 CSV prediction functionality

📁 Project Structure

car-price-prediction/
│
├── final.py
├── clean_car_data.csv
├── random_forest_model.pkl
├── preprocessor.pkl
├── README.md
└── images/

🎓 Project Context

This project was developed as part of my practical learning in Data Science Management & Analytics (DSMA) at the Uganda Institute of Information and Communications Technology (UICT).

👨‍💻 Author

Yabiraku Reagan

Data Science Student | Machine Learning & Data Analytics

GitHub: REAGANreya

Expected Graduation: 2027

📍 Kampala, Uganda
