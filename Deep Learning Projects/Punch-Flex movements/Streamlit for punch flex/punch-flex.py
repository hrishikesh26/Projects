import serial
import time
import streamlit as st
# import plotly.graph_objects as go
# import plotly.express as px
# from datetime import datetime
import pandas as pd
from PIL import Image
# from streamlit import caching


# Note: This must be the first command in your app, and must be set only once
# st.set_page_config(layout="wide")

st.header("Punch Flex Classification")



arduino = serial.Serial(port='COM8', baudrate=9600, parity=serial.PARITY_NONE,stopbits=serial.STOPBITS_ONE,bytesize=serial.EIGHTBITS) #Change the COM port to whichever port your arduino is in

flex,punch=st.columns([2,2])


# add_selectbox = st.sidebar.selectbox("Which number do you like?", ())



i = 0



while i < 500:
    flex=0
    punch=0
    # now = datetime.now()
    # current_time = now.strftime("%H:%M:%S")

    # try:
    readings = str(arduino.readline().decode().strip('\r\n'))
    readings=readings.split(',')
    flex=float(readings[0])
    punch=float(readings[1])
    if flex<punch:
        image = Image.open('punch_image.png')
        image2 = image.resize((50,60) )
         #displaying the image on streamlit app
        st.image(image2, caption='Punch')
        st.write(f"Predicted Punch 👊👊👊: {punch}")
    else:
        image = Image.open('flex_image.png')
        image3 = image.resize((50,60) )
         #displaying the image on streamlit app
        st.image(image3, caption='flex')
        st.write(f"Predicted Flex💪💪💪: {flex}")

    
    

    # except:
    #     pass

    # records.loc[i,'Time'] = current_time
    # records.loc[i,'flex'] = flex
    # records.loc[i,'punch'] = punch

    
    i += 1
    


# Type this below commmand in your editor terminal to run streamlit on browser

# streamlit run punch-flex.py