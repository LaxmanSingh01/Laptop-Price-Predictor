import streamlit as st
import pickle
import numpy as np

# import the model
model = pickle.load(open('model.pkl','rb'))
data = pickle.load(open('data.pkl','rb'))

st.title("Laptop Price Predictor")

# brand
company = st.selectbox('Brand',data['Company'].unique())

# type of laptop
type = st.selectbox('Type',data['TypeName'].unique())

# Ram
ram = st.selectbox('RAM(in GB)',[2,4,6,8,12,16,24,32,64])

# weight
weight = st.number_input('Weight of the Laptop')

# Touchscreen
touchscreen = st.selectbox('Touchscreen',['No','Yes'])

# IPS
IPS = st.selectbox('IPS',['No','Yes'])

# screen size
screen_size = st.number_input('Screen Size')

# resolution
resolution = st.selectbox('Screen Resolution',['1920x1080','1366x768','1600x900','3840x2160','3200x1800','2880x1800','2560x1600','2560x1440','2304x1440'])

#cpu
cpu = st.selectbox('CPU',data['cpu_processor'].unique())

hdd = st.selectbox('HDD(in GB)',[0.0,128.0,256.0,512.0,1024.0,2048.0])

ssd = st.selectbox('SSD(in GB)',[0.0,8.0,128.0,256.0,512.0,1024.0])

gpu = st.selectbox('GPU',data['gpu'].unique())

os = st.selectbox('OS',data['OpSys'].unique())

if st.button('Predict Price'):
    # query
    ppi = None
    if touchscreen == 'Yes':
        touchscreen = 1
    else:
        touchscreen = 0

    if IPS == 'Yes':
        IPS = 1
    else:
        IPS = 0



    X_res = int(resolution.split('x')[0])
    Y_res = int(resolution.split('x')[1])
    ppi = ((X_res**2) + (Y_res**2))**0.5/screen_size
    query = np.array([company,type,ram,os,weight,cpu,touchscreen,IPS,ppi,hdd,ssd,gpu])
    query = query.reshape(1,12)
    st.title("The predicted price of this Laptop is " + str(int(np.exp(model.predict(query)[0]))))