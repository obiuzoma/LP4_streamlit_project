import streamlit as st
import pandas as pd
import streamlit_authenticator as stauth
import yaml
from yaml.loader import SafeLoader

st.set_page_config(
    page_title='Home',
    page_icon = ':)',
    layout='wide'
)
st.title('Home Page',"🏛️home:")
st.image('time_series_image.jpg')

with open('config.yaml') as file:
    config = yaml.load(file, Loader=SafeLoader)

authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days'],
    config['preauthorized']
)
authenticator.login()


if st.session_state["authentication_status"]:
    authenticator.logout()
    st.write(f'Welcome *{st.session_state["name"]}*')
    st.title('Some content')
elif st.session_state["authentication_status"] is False:
    st.error('Username/password is incorrect')
elif st.session_state["authentication_status"] is None:
    st.warning('Please enter your username and password')



 
