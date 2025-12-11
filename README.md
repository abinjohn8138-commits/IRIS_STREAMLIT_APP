# IRIS_FLASK_APP
 Iris Classification Flask App

A simple Flask web application that uses a trained machine-learning model to classify Iris flowers into three species:

Iris setosa

Iris versicolor

Iris virginica

The model is trained on the classic Iris dataset and exposes a lightweight web interface + REST endpoint for predictions.

 Features

 Trained ML model (e.g., Logistic Regression / SVM / RandomForest)

 Clean Flask web server

 Input form for sepal & petal dimensions

 /predict API route for JSON requests

 Easy to deploy (local or cloud)

 How It Works

1,train_model.py loads the Iris dataset from scikit-learn

2,Trains a classifier

3,Saves it to model.pkl

4,app.py loads the model at runtime

5,Accepts values through a form or API call

6,Returns a predicted species

 Requirements

* Python 3.8+

* Flask

* scikit-learn

* pandas

* numpy

Deployment

* Render

* Railway

* Heroku

* Azure App Services

* AWS Elastic Beanstalk
