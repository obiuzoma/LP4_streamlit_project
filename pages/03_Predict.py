import streamlit as st
import pandas as pd
import joblib

# create page lay out
st.set_page_config(
    page_title='Predict Data',
    page_icon = ':)',
    layout='wide'
)


# write title for preiction page
st.title('Data Prediction')


st.cache_resource(show_spinner='Model loading')

# create funtion for gradient boost pipiline
def gradient_pipline():
    models = joblib.load("./models/gradient_pipeline.joblib")
    return models

# code to cache the model
st.cache_resource(show_spinner='Model loading')

# create function for naives pipline
def naives_pipeline():
    models = joblib.load('./models/Naives_pipeline.joblib')
    return models

# create function for model selection
def model_selection():
    st.selectbox('choose a model', options=['Gradient Model', 'Naieves model'], key='choose_model')
    if  st.session_state['choose_model'] == 'Gradient Model':
        models = gradient_pipline ()
    else:
        models = naives_pipeline()

    encoder = joblib.load('./models/encoder.joblib')

    return models, encoder


# code to make a preidction
def data_prediction(models, encoder):
    gender = st.session_state['gender']
    seniorcitizen = st.session_state['seniorcitizen']
    partener = st.session_state['partner']
    dependants = st.session_state['dependants']
    tenure = st.session_state['tenure']
    phoneservice = st.session_state['phoneservice']
    multipleLines = st.session_state['multipleLines']
    internateservice = st.session_state['internateservice']
    onlinesecurity = st.session_state['onlinesecurity']
    onlinebackup = st.session_state['onlinebackup']
    deviceoperation = st.session_state['deviceoperation']
    techsupport = st.session_state['techsupport']
    streamingtv = st.session_state['streamingtv']
    streamingmovies = st.session_state['streamingmovies']
    contract = st.session_state['contract']
    paperlessbilling = st.session_state['PaperlessBilling']
    paymentmethods = st.session_state['paymentmethods']
    monthlycharges = st.session_state['monthlycharges']
    totalcharges= st.session_state['totalcharges']
    columns =['gender', 'SeniorCitizen', 'Partner', 'Dependents', 'tenure',
        'PhoneService', 'MultipleLines', 'InternetService', 'OnlineSecurity',
        'OnlineBackup', 'DeviceProtection', 'TechSupport', 'StreamingTV',
        'StreamingMovies', 'Contract', 'PaperlessBilling', 'PaymentMethod',
        'MonthlyCharges', 'TotalCharges',]
    data = [[gender,seniorcitizen, partener, dependants,tenure,phoneservice,multipleLines, internateservice, onlinesecurity,
              onlinebackup,deviceoperation,techsupport,streamingtv,streamingmovies, contract,paperlessbilling,
              paymentmethods,monthlycharges,totalcharges]]
    
# create  a d ata frame
    df = pd.DataFrame(data, columns=columns)
    prediction = models.predict(df)

    st.session_state['prediction'] = prediction
    return prediction


# create a form
def create_form():
    with st.form('features'):
        models, encoder = model_selection()
        col1, col2, col3 = st.columns(3)
        with col1:
            st.write('##### Personal information')
            gender = st.number_input('input age', min_value=18, max_value=60, step=1, key='gender')
            seniorcitizen = st.selectbox('select yes or No', options= ["yes","No"],key='seniorcitizen')
            Partener = st.selectbox('select', options= ["yes","No"], key='partener')
            dependants = st.selectbox('select yes or No', options= ["yes","No"])
        
            tenure = st.number_input('enter number of tenure', min_value=1, max_value=73, step=1, key='tenure')
            contract = st.selectbox(' Select Contract', options=['Month-to-month', 'One year' ,'Two year'])
        with col2:
            st.write('##### Select Types of Services')
            Phoneservice = st.selectbox('Phone Service', options=['No phone service' ,'No' ,'Yes'],key='phone service')
            multipleLine = st.selectbox('Multiple Line', options=['DSL', 'Fiber optic', 'No'], key='multipleline')
            internateservice = st.selectbox(' Internet Service', options=['No', 'Yes', 'No internet service'], key='internateservice')
            onlinesecurity =st.selectbox('Online security', options=['No', 'Yes', 'No internet service'],key='onlinesecurity')
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
    
    summitted= st.form_submit_button("Submit")
    if summitted:
        st.write( models, encoder = model_selection())
        data_prediction(models, encoder)

create_form()


if __name__ == "_main_":
    
    st.title('Data Prediction')
# create_form()
        #  model_selection()
final_prediction = st.session_state['prediction']


   
st.write('final_prediction')
st.write(st.session_state)