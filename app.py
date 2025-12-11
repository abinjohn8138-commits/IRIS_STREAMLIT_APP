import streamlit as st
import numpy as np
import joblib
model = joblib.load("iris_model.pkl")

st.title("Iris Flower Prediction 🌸")
st.write("Enter flower measurements to predict species")

sepal_length=st.number_input("Sepal Length(cm)",0.0,10.0,5.1)
sepal_width=st.number_input("Sepal Width (cm)",  0.0, 10.0, 3.5)
petal_length=st.number_input("Petal Length (cm)", 0.0, 10.0, 1.4)
petal_width=st.number_input("Petal Width (cm)",  0.0, 10.0, 0.2)

if st.button("predict"):
    input_data=np.array([[sepal_length, sepal_width, petal_length, petal_width]])
    prediction = model.predict(input_data)[0]
    
    species = ["Setosa", "Versicolor", "Virginica"][prediction]
    st.success(f"The predicted species is **{species}** 🌿")