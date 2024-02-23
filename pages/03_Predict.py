import streamlit as st
import pandas as pandas


st.set_page_config(
    page_title='Predict Data',
    page_icon = ':)',
    layout='wide'
)
st.title('Data Prediction')
# (['gender', 'SeniorCitizen', 'Partner', 'Dependents', 'tenure',
#        'PhoneService', 'MultipleLines', 'InternetService', 'OnlineSecurity',
#        'OnlineBackup', 'DeviceProtection', 'TechSupport', 'StreamingTV',
#        'StreamingMovies', 'Contract', 'PaperlessBilling', 'PaymentMethod',
#        'MonthlyCharges', 'TotalCharges', 'Churn'],
#       dtype='object')
def create_form():
   col1, col2, col3, col4 = st.columns(4)
   with st.form('features'):

    with col1:
        st.write('##### Personal information')
        gender = st.number_input('input age', min_value=18, max_value=60, step=1)
        senorcitizen = st.selectbox('select yes or No', options= ["yes","No"])
        Partener = st.selectbox('select', options= ["yes","No"])
        # st.selectbox('select yes or No', options= ["yes","No"])
    with col2:
        st.write('#### Work Information')
        tenure = st.number_input('enter number of tenure', min_value=1, max_value=73, step=1)
        contract = st.selectbox(' Select Contract', options=['Month-to-month', 'One year' ,'Two year'])
    with col3:
        st.write('##### Select Types of Services')
        PhoneSevice = st.selectbox('Phone Service', options=['No phone service' ,'No' ,'Yes'])
        multipleLine = st.selectbox('Multiple Line', options=['DSL', 'Fiber optic', 'No'])
        InternateService = st.selectbox(' Internet Service', options=['No', 'Yes', 'No internet service'])
        onlineSecurity =st.selectbox('Online security', options=['No', 'Yes', 'No internet service'])
        onlinebgackup = st.selectbox('Online Backup', options=['Yes', 'No','No internet service'])
        deviceprotection = st.selectbox(' Device Protection', options=['No', 'Yes', 'No internet service'])
        techsupport = st.selectbox(' Tech Support', options=['No', 'Yes', 'No internet service'])
        streamingtv = st.selectbox(' Streaming Tv', options=['No', 'Yes', 'No internet service'])
        streamingmovies = st.selectbox(' Streaming Movies', options=['No', 'Yes', 'No internet service'])
    with col4:
       st.write('###### Modes of Payments')
       paperlessBilling = st.selectbox(' Streaming Movies', options=['No', 'Yes'])
       paymentmethods = st.selectbox(' Streaming Movies', options=['Electronic check', 'Mailed check', 'Bank transfer (automatic)',
                    'Credit card (automatic)'])
       monthlycharges = st.number_input('Enter Monthly Charges', min_value=20.000, max_value=120.000, step=50)
       totalcharges = st.number_input('Enter Total Charges', min_value=20.000, max_value=7000.000, step=50)



                                                     

    st.form_submit_button('Submit')
create_form()