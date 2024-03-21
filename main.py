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

        st.markdown('#### Customer Churn Prediction App')
        ('''
            
        **Overview:**

        The customer churn prediction app is designed to help managers predict the likelihood of customers leaving their company.

        ### Key Features:

        - **Home Page:** Login details and app descriptions.
        - **Data Page:** Sample data used from Vodafone company.
        - **Dashboard:** Contains Key Performance Indicators (KPI) and Exploratory Data Analysis (EDA) of the customer data with interactive visualization and insights.
        - **Prediction Page:** A form to predict whether a customer will stop using company products.
        - **History Page**: Table containing the data of predicted customers.

        ### User Benefits

        - **Data-deriven Decision:** Make informed decision backed by data analytics
        - **Easy Machine Learning:** utilize powerful machine learning algorithm effortlessy
    ''')

    with col2:
        ('''

        **How to Run the App:**
        1. install requirement.txt
                ```
                pip install reqirement.txt
                ```
        2. Clone this repository to your local machine:

                cd my_folder

                clone https://github.com/obiuzoma/LP4_streamlit_project.git
        
        3. Change into the cloned repository:
            cd LP4_streamlit_project
        4. Create a virtual environment:
            python -m virtual_env env
        5. Activate the virtual environment:
        - On Windows:
        ```
        .\env\Scripts\activate
        ```
        - On macOS and Linux:
        ```
        source env/bin/activate
        ```
        **Need Help?**

        Contact: uzyivy@gmail.com

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



 
