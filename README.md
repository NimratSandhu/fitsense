FitSense
========

FitSense is a heart disease prediction tool that leverages machine learning to analyze user inputed health data and predict the likelihood of heart disease. The project involves training a machine learning model using health-related datasets and deploying the model in a user-friendly interface.

Table of Contents
-----------------

- Project Overview
- Features
- Installation
- Usage
- Model Training and Evaluation
- Deployment

Project Overview
----------------

The goal of the FitSense project is to predict heart disease in patients based on various health metrics. The project is built with Python, and the machine learning model is trained using a dataset containing various health statistics. The model is then deployed to allow users to input their health data and receive predictions.

Features
--------

- **Heart Disease Prediction**: Predict whether a patient has heart disease based on their health metrics.
- **User-Friendly Interface**: Simple command-line interface for users to input their data.
- **Model Deployment**: The trained machine learning model is saved and deployed to be used in real-time predictions.

Installation
------------

### Prerequisites

- Python 3.8+
- Virtual environment (optional but recommended)

### Clone the Repository

Usage
-----

### Running the Prediction Script

After installing the necessary packages, you can run the prediction script:
python script/fitsense.py
The script will prompt you to enter health-related metrics, and it will output the prediction (whether the patient is likely to have heart disease).


Model Training and Evaluation
------------------------------

### Training the Model

The model was trained using a dataset containing various health metrics. The training process involved parameter tuning using Random Forest and testing several models like Logistic Regression, SVM, and XGBoost to achieve the best performance.

### Evaluation

The model was evaluated using accuracy and F1 score metrics. The best-performing model achieved an accuracy of 99% on the test set.

### Feature Importance

The most important features contributing to the prediction were:

1. ca
2. thalach
3. oldpeak
4. cp
5. thal

Deployment
----------

The trained model is saved using `joblib` and can be loaded for making predictions in real-time.
