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

def project_description():
    col1, col2 = st.columns(2)
    with col1:

        st.markdown('#### Customer Churn Prediction')
        st.write('customer churn prediction app is designed to help managers predict the likelyhood of customers leaving their company or not')
        st.subheader('Key Features')
        st.markdown('##### * Home page')
        st.write('Login details of the app')
        st.markdown('##### * Data page')
        st.write('Sample of data use for the traing of the models')
        st.markdown('##### * Dashboard')
        st.write('This page contain the KPI and EDA of the customer data')
        st.markdown('##### * Prediction Page')
        st.write('A form to predict wether a customer will stop using company product')
        st.markdown('##### * History Page')
        st.write('Table containing the data of predicted cuntomers')
    with col2:
        st.subheader('How to run the app')
        st.write('clone this repositary on your local machine')
        st.write('cd my_folder')
        st.write('clone https://github.com/obiuzoma/LP4_streamlit_project.git')
        st.write('Change into the cloned repository')
        st.write('cd LP4_streamlit_project')
        st.write('Create a virtual environment')
        st.write('python -m virtual_env env')
        st.write('Activate the virtual environment')

        st.markdown('##### * Need Help?')
        st.write('Congtact @: uzyivy@gmail.com')
st.write('login Details')
st.write('User Name: uzoma')
st.write('Passward: abc')

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
    project_description()
elif st.session_state["authentication_status"] is False:
    st.error('Username/password is incorrect')
elif st.session_state["authentication_status"] is None:
    st.warning('Please enter your username and password')



 
