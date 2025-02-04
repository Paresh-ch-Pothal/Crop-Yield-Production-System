import streamlit as st
import numpy as np
import pandas as pd
import pickle

pipe=pickle.load(open("pipe.pkl","rb"))
new_df=pickle.load(open("new_df.pkl","rb"))

st.title("Crop Yield Production System")
st.markdown("---")
area=st.selectbox("Select The Area",key=4,options=new_df["Area"].unique())
item=st.selectbox("Select The Item",key=5,options=new_df["Item"].unique())
temp=st.slider("Select The Average Temperature (degree Celcius)",key=1,min_value=new_df["avg_temp"].min(),max_value=new_df["avg_temp"].max(),value=new_df["avg_temp"].min())
pest=st.slider("Use of Pesticides in (Tonnes)",key=2,min_value=new_df["Pesticides Value"].min(),max_value=new_df["Pesticides Value"].max(),value=new_df["Pesticides Value"].min())
rain=st.slider("Average Rainfall in (mm)",key=3,min_value=new_df["Average RainFall"].min(),max_value=new_df["Average RainFall"].max(),value=new_df["Average RainFall"].min())
btn=st.button("Predict")
if btn:
    user_input = {
        "Area": area,
        "Item": item,
        "Average RainFall": rain,
        "avg_temp": temp,
        "Pesticides Value": pest
    }
    user_input_df = pd.DataFrame([user_input])
    ypred=pipe.predict(user_input_df)
    st.subheader("Predicted Value: ")
    st.subheader(f"{ypred[0]:,.2f} hectograms per hectare")


