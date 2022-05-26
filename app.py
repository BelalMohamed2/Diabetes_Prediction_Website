import streamlit as st
import pickle
import numpy as np
import pandas as pd
home = open("model.csv", 'rb')
model = pickle.load(home)
st.title("Diabetes Prediction Form")
cholesterol = int(st.number_input("cholesterol level"))
glucose = int(st.number_input("glucose  level"))
hdl_chol = int(st.number_input("hdl_chol  level"))
age = int(st.number_input("age"))
gender = st.selectbox('Gender', ('male', 'female'))
height = int(st.number_input("height in inches"))
weight = int(st.number_input("weight in pounds"))
systolic_bp = int(st.number_input("systolic blood pressure"))
diastolic_bp = int(st.number_input("diastolic blood pressure"))
waist = int(st.number_input("waist in inches"))
hip = int(st.number_input("hip in inches"))


btn = st.button("predict")
if btn:
    if gender == "male":
        z = 1
    else:
        z = 2
    x = (weight/2.2)
    y = (height*height/1562.99)
    bmi = x/y
    waist_hip_ratio = (waist)/(hip)
    chol_hdl_ratio = cholesterol/hdl_chol
    pred = model.predict(np.array([cholesterol, glucose, hdl_chol, chol_hdl_ratio, age, z, height,
                        weight, bmi, systolic_bp, diastolic_bp, waist, hip, waist_hip_ratio]).reshape(1, -1))
    if pred == 2:
        st.header("You are suspected to have Diabetes you must conslut the doctor")
    else:
        st.header("You have No_Diabetes")
