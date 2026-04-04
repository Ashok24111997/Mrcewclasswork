import streamlit as st
import numpy as np
import pickle

model = pickle.load(open("model.pkl", "rb"))

st.title("📱 Mobile Price Predictor")

battery = st.slider("Battery Power", 500, 2000)
blue = st.selectbox("Bluetooth", [0,1])
clock = st.slider("Clock Speed", 0.5, 3.0)
dual_sim = st.selectbox("Dual SIM", [0,1])
fc = st.slider("Front Camera", 0, 20)
four_g = st.selectbox("4G", [0,1])
memory = st.slider("Internal Memory", 2, 128)
m_dep = st.slider("Mobile Depth", 0.1, 1.0)
weight = st.slider("Mobile Weight", 80, 200)
cores = st.slider("Number of Cores", 1, 8)
pc = st.slider("Primary Camera", 0, 20)
px_h = st.slider("Pixel Height", 0, 2000)
px_w = st.slider("Pixel Width", 500, 2000)
ram = st.slider("RAM", 256, 4000)
sc_h = st.slider("Screen Height", 5, 20)
sc_w = st.slider("Screen Width", 1, 20)
talk = st.slider("Talk Time", 2, 20)
three_g = st.selectbox("3G", [0,1])
touch = st.selectbox("Touch Screen", [0,1])
wifi = st.selectbox("WiFi", [0,1])

if st.button("Predict"):
    data = np.array([[battery, blue, clock, dual_sim, fc, four_g,
                      memory, m_dep, weight, cores, pc,
                      px_h, px_w, ram, sc_h, sc_w,
                      talk, three_g, touch, wifi]])

    pred = model.predict(data)[0]

    st.success(f"Predicted Price Range: {pred}")