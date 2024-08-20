import streamlit as st
import pickle

with open('wine.pkl', 'rb') as f:
    data = pickle.load(f)

encoder = data[0]
model   = data[1]


st.title('Wine Quality Estimator')
st.write('''Description:

This datasets is related to red variants of the Portuguese "Vinho Verde" wine.The dataset describes the amount of various chemicals present in wine and their effect on it's quality. The datasets can be viewed as classification or regression tasks. The classes are ordered and not balanced (e.g. there are much more normal wines than excellent or poor ones).Your task is to predict the quality of wine using the given data.

A simple yet challenging project, to anticipate the quality of wine.
The complexity arises due to the fact that the dataset has fewer samples, & is highly imbalanced.
Can you overcome these obstacles & build a good predictive model to classify them?

This data frame contains the following columns:

Input variables (based on physicochemical tests):\
1 - fixed acidity\
2 - volatile acidity\
3 - citric acid\
4 - residual sugar\
5 - chlorides\
6 - free sulfur dioxide\
7 - total sulfur dioxide\
8 - density\
9 - pH\
10 - sulphates\
11 - alcohol\
Output variable (based on sensory data):\
12 - quality (score between 0 and 10)
Acknowledgements:
''')
with st.form("myform"):
    fa = st.number_input(label = 'Fixed Acidity', min_value=5.0, max_value = 20.0)
    va = st.number_input(label = "Volatile Acidity", min_value = 0.0, max_value = 1.0)#
    ca = st.number_input(label = "Citric Acid", min_value = 0.0, max_value = 1.0)
    rs = st.number_input(label = "Residual Sugar", min_value = 1.0, max_value = 3.0)
    cl = st.number_input(label = 'Chlorides', min_value = 0.0, max_value = 0.1, step = 0.002)
    fso= st.number_input(label = 'Free SO2', min_value = 5.0, max_value = 20.0, step = 1.0)
    tso= st.number_input(label = "Total SO2", min_value = 25.0, max_value = 80.0, step = 2.0)
    rho= st.number_input(label = "Density", min_value = 0.9000, max_value = 1.000, step = 0.001)
    ph = st.number_input(label = 'pH', min_value = 3.0, max_value = 4.0, step = 0.01)
    su = st.number_input(label = "Sulphates", min_value = 0.3, max_value = 0.8, step = 0.02)
    OH = st.number_input(label = "Alcohol", min_value = 7.0, max_value = 10.0, step = 0.1)

    submitted = st.form_submit_button("Quality Estimator")
    x = [fa, va, ca, rs, cl, fso, tso, rho, ph, su, OH]

    if submitted:
        prediction = model.predict([x])
        if prediction == 1:
            st.write("This is :green[GOOD] quality wine")
        else:
            st.write("This is :red[BAD] quality wine")
