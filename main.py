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
# st.image('time_series_image.jpg')

def project_description():
    col1, col2 = st.columns(2)
    with col1:

        st.markdown('#### Customer Churn Prediction')
        ('''
         
        customer churn prediction app is designed to help managers predict the likelyhood of customers leaving their company or not

        **Key Features**
        - Home page: Login details and app descriptions
        - Data page:Sample of data use for the traing of the models
        - Dashboard: contain the KPI and EDA of the customer data interactive visualization and insights
        -  Prediction Page:A form to predict wether a customer will stop using company product
        - History Page:Table containing the data of predicted cuntomers
    ''')
    with col2:
        pass
        ('''
        **How to run the app**
        - clone this repositary on your local machine
        
        cd my_folder
        clone https://github.com/obiuzoma/LP4_streamlit_project.git
         
        
        - Change into the cloned repository
        cd LP4_streamlit_project
        - Create a virtual environment:

        python -m virtual_env env
        - Activate the virtual environment:
        virtual_env/scripts/activate

        **Need Help?**

        Congtact @: uzyivy@gmail.com
        ''')


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



 
