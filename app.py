import streamlit as st 
import pickle 
import numpy as np 
#importing model
 
pipe = pickle.load(open('pipe.pkl' , 'rb'))
df = pickle.load(open('df.pkl' , 'rb'))



st.title("Laptop Price Predictor")

# brand
company = st.selectbox('Brand' , df['Company'].unique())
typeName = st.selectbox('TYPE' , df['TypeName'].unique())
ram = st.selectbox('RAM' , [2,4,6,8,12,16,24,32,64])
weight = st.number_input('Weight of laptop ')
touchscreen = st.selectbox('Touchscreen' , ['No','Yes'])
ips = st.selectbox('IPS Display' , ['No','Yes'])
screen_size = st.number_input('Screen size ')
resolutions = st.selectbox('Resolutions', ['1920x1080','1366x768','1600x900','3840x2160','3200x1800','2880x1800','2560x1600','2560x1440','2304x1440'])
cpu = st.selectbox('Cpu brand ', df['Cpu_brand'].unique())
hdd = st.selectbox('HDD' , [0,256,512,1024,2048])
ssd = st.selectbox('SSD' , [0,8,256,512,1024])
gpu = st.selectbox('GPU Brand ', df['Gpu_brand'].unique())
oss = st.selectbox('Operating system', df['os'].unique())

# 1 step to make an input row 
# 2 step send that row to pipe 
# 3 step and pickup our predection 

# in touchscreen and ips we have yes no and we want 0 , 1
if st.button('predict Price'):
    ppi = None
    
    if touchscreen == 'Yes':
        touchscreen = 1
    else:
        touchscreen = 0 
        
        
    if ips == 'Yes':
            ips = 1
    else:
        ips = 0
        
    x_res = int(resolutions.split('x')[0])        
    y_res = int(resolutions.split('x')[1])      
    if screen_size == 0 :
        screen_size=14;
    ppi = ((x_res**2) + (y_res**2))**0.5 / screen_size  
    query = np.array([company,typeName,ram ,weight,touchscreen,ips,ppi,cpu,hdd,ssd,gpu,oss])

    query = query.reshape(1,12) #  in  1 row and 12 cols   
    
    st.title(int(np.exp(pipe.predict(query))))
   