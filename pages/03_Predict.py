import streamlit as st
import pandas as pandas
import joblib


st.set_page_config(
    page_title='Predict Data',
    page_icon = ':)',
    layout='wide'
)


st.title('Data Prediction')
st.cache_resource(show_spinner='Model loading')
def gradient_pipline():
    models = joblib.load("./modles/graidient_pipeline.joblib")
    return models

st.cache_resource(show_spinner='Model loading')
def naives_pipeline():
    models= joblib.load('./models/Naives_pipeline.joblib')
    return models

def model_selection():
    st.selectbox('choose a model', options=['Gradient Model', 'Naieves model'], key='choose_models')
    if  st.session_state['choose_model'] == 'Gradient Model':
        models = gradient_pipline ()
    else:
       naives = naives_pipeline()

    encoder = joblib.load('./models/encoder.joblib')

    return models, encoder
def data_prediction(models, encoder):
    gender = st.session_state['gender']
    SeniorCitizen = st.session_state['SeniorCitizen']
    Partner = st.session_state['Partner']
    Partner = st.session_state['Partner']
    Dependents = st.session_state['Dependents']
    tenure = st.session_state['tenure']
    PhoneService = st.session_state['PhoneService']
    MultipleLinesr = st.session_state['MultipleLines']
    InternetService = st.session_state['InternetService']
    OnlineSecurity = st.session_state['OnlineSecurity']
    OnlineBackup = st.session_state['OnlineBackup']
    DeviceProtection = st.session_state['DeviceProtection']
    TechSupport = st.session_state['TechSupport']
    StreamingTV = st.session_state['StreamingTV']
    StreamingMovies = st.session_state['StreamingMovies']
    Contract = st.session_state['DeviceProtection']
    PaperlessBilling = st.session_state['PaperlessBilling']
    PaymentMethod= st.session_state['PaymentMethod']
    MonthlyCharges = st.session_state['MonthlyCharges']
    TotalCharges= st.session_state['TotalCharges']

# (['gender', 'SeniorCitizen', 'Partner', 'Dependents', 'tenure',
#        'PhoneService', 'MultipleLines', 'InternetService', 'OnlineSecurity',
#        'OnlineBackup', 'DeviceProtection', 'TechSupport', 'StreamingTV',
#        'StreamingMovies', 'Contract', 'PaperlessBilling', 'PaymentMethod',
#        'MonthlyCharges', 'TotalCharges', 'Churn'],
#       dtype='object')
def create_form():
    
    with st.form('features'):
        col1, col2, col3 = st.columns(3)
        with col1:
            st.write('##### Personal information')
            gender = st.number_input('input age', min_value=18, max_value=60, step=1, key='gender')
            seniorcitizen = st.selectbox('select yes or No', options= ["yes","No"],key='seniorcitizen')
            Partener = st.selectbox('select', options= ["yes","No"], key='partener')
            # st.selectbox('select yes or No', options= ["yes","No"])
        
            tenure = st.number_input('enter number of tenure', min_value=1, max_value=73, step=1, key='tenure')
            contract = st.selectbox(' Select Contract', options=['Month-to-month', 'One year' ,'Two year'])
        with col2:
            st.write('##### Select Types of Services')
            PhoneSevice = st.selectbox('Phone Service', options=['No phone service' ,'No' ,'Yes'],key='phone service')
            multipleLine = st.selectbox('Multiple Line', options=['DSL', 'Fiber optic', 'No'], key='multipleline')
            InternateService = st.selectbox(' Internet Service', options=['No', 'Yes', 'No internet service'], key='internateservice')
            onlineSecurity =st.selectbox('Online security', options=['No', 'Yes', 'No internet service'],key='onlinesecurity')
            onlinebackup = st.selectbox('Online Backup', options=['Yes', 'No','No internet service'], key='onlinebackup')
            deviceprotection = st.selectbox(' Device Protection', options=['No', 'Yes', 'No internet service'],key='deviceoperation')
            techsupport = st.selectbox(' Tech Support', options=['No', 'Yes', 'No internet service'], key='techsupport')
            streamingtv = st.selectbox(' Streaming Tv', options=['No', 'Yes', 'No internet service'],key='streamingtv')
            streamingmovies = st.selectbox(' Streaming Movies', options=['No', 'Yes', 'No internet service'],key='streamingmovies')
        with col3:
            st.write('###### Modes of Payments')
            paperlessbilling = st.selectbox(' Streaming Movies', options=['No', 'Yes'],key='paerlessbill')
            paymentmethods = st.selectbox(' Streaming Movies', options=['Electronic check', 'Mailed check', 'Bank transfer (automatic)',
            'Credit card (automatic)'],key='paymentmethods')
            monthlycharges = st.number_input('Enter Monthly Charges', min_value=20, max_value=120, step=50,key='monthlycharges')
            totalcharges = st.number_input('Enter Total Charges', min_value=20, max_value=7000, step=50,key='totalcharges')
     

    st.form_submit_button('Submit')

if __name__ == "_main_":



 model_selection()


create_form()
st.write(st.session_state)