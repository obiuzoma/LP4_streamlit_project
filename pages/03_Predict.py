import streamlit as st
import pandas as pd
import joblib
import numpy as np
import os
import datetime

# create page lay out
st.set_page_config(
    page_title='Predict Data',
    page_icon = ':)',
    layout='wide'
)


# write title for preiction page
st.title('♣️ Prediction Page')

# create funtion for gradient boost pipiline

# def gradient_pipline():
#     models = joblib.load("./models/gradient_pipeline.joblib")
#     return models

st.cache_resource(show_spinner='Model loading')
def random_forest():
   models = joblib.load("./models/random_forest_pipeline.joblib")
   return models

# code to cache the model
st.cache_resource(show_spinner='Model loading')
# create function for naives pipline
def guass_pipeline():
    models = joblib.load('./models/gauss_pipeline.joblib')
    return models

# create function for model selection
def model_selection():
    st.selectbox('choose a model', options=['Random Forest Model', 'GuassianNB model'], key='choose_model')
    if  st.session_state['choose_model'] == 'Random Forest Model':
        models = random_forest()
    else:
        models = guass_pipeline()
    encoder = joblib.load('./models/label_encoder.joblib')
    return models, encoder


if 'prediction' not in st.session_state:
    st.session_state['prediction'] = None
if 'probability' not in st.session_state:
    st.session_state['probability'] = None

if os.path.exist('./data/history.csv'):
        os.mkdir('./data')

# code to make a preidction
def data_prediction(models, encoder):
    gender = st.session_state['gender']
    partner = st.session_state['partner']
    dependents = st.session_state['dependents']
    tenure = st.session_state['tenure']
    phoneservice = st.session_state['phoneservice']
    multiplelines = st.session_state['multiplelines']
    internetservice = st.session_state['internetservice']
    onlinesecurity = st.session_state['onlinesecurity']
    onlinebackup = st.session_state['onlinebackup']
    deviceprotection = st.session_state['deviceprotection']
    techsupport = st.session_state['techsupport']
    streamingtv = st.session_state['streamingtv']
    streamingmovies = st.session_state['streamingmovies']
    contract = st.session_state['contract']
    paperlessbilling= st.session_state['paperlessbilling']
    paymentmethod = st.session_state['paymentmethod']
    monthlycharges = st.session_state['monthlycharges']
    totalcharges = st.session_state['totalcharges']
    seniorcitizen = st.session_state['seniorcitizen']

    columns =['gender', 'SeniorCitizen', 'Partner', 'Dependents','tenure', 'PhoneService',
       'MultipleLines', 'InternetService', 'OnlineSecurity', 'OnlineBackup',
       'DeviceProtection', 'TechSupport', 'StreamingTV', 'StreamingMovies',
       'Contract', 'PaperlessBilling', 'PaymentMethod','MonthlyCharges', 'TotalCharges']

    data = [[gender,  seniorcitizen, partner, dependents,tenure, phoneservice, multiplelines, internetservice, onlinesecurity,
              onlinebackup, deviceprotection, techsupport, streamingtv, streamingmovies, contract, paperlessbilling,
              paymentmethod, monthlycharges, totalcharges]]
    
# create  a data frame
    df = pd.DataFrame(data, columns = columns)
    
    
# make prediction
    pred = models.predict(df)
    pred = int(pred[0])
    prediction = encoder.inverse_transform([pred])

    df['Prediction Time'] = datetime.date.today()
    df['Model Used'] = model_display_name
    
    history_dir = './history_data'
    if not os.path.exists(history_dir):
        os.makedirs(history_dir)
    
    df.to_csv(os.path.join(history_dir, 'history.csv'), mode='a', header=not os.path.exists(os.path.join(history_dir, 'history.csv')), index=False)
   
    probability = models.predict_proba(df)

    st.session_state['prediction'] = prediction
    st.session_state['probability'] = probability

    return prediction , probability


# create a form
def create_form():
    models, encoder = model_selection()
    with st.form('features'):

        
        col1, col2 = st.columns(2)
        with col1:
           
            st.write('##### Customrs Information')
        
            st.number_input('input age', min_value=18, max_value=60, step=1, key='gender')
            st.selectbox('select yes or No', options= ["yes","No"],key='seniorcitizen')
            st.selectbox('select', options= ["yes","No"], key='partner')
            st.selectbox('select yes or No', options= ["yes","No"], key= 'dependents')
        
            st.number_input('enter number of tenure', min_value=1, max_value=73, step=1, key='tenure')
            st.selectbox('Phone Service', options=['No phone service' ,'No' ,'Yes'],key='phoneservice')
            st.selectbox('Multiple Line', options=['DSL', 'Fiber optic', 'No'], key='multiplelines')
            st.selectbox(' Internet Service', options=['No', 'Yes', 'No internet service'], key='internetservice')
            
   
        with col2:
            fg1, fg2 = st. columns(2)
            with fg1:
                pass
            with fg2:
                pass
            st.selectbox('Online security', options=['No', 'Yes', 'No internet service'],key='onlinesecurity')
            st.selectbox('Online Backup', options=['Yes', 'No','No internet service'], key='onlinebackup')
            st.selectbox(' Device Protection', options=['No', 'Yes', 'No internet service'],key='deviceprotection')
            st.selectbox(' Tech Support', options=['No', 'Yes', 'No internet service'], key='techsupport')
            st.selectbox(' Streaming Tv', options=['No', 'Yes', 'No internet service'],key='streamingtv')
            st.selectbox(' Streaming Movies', options=['No', 'Yes', 'No internet service'],key='streamingmovies')
            st.selectbox(' Select Contract', options=['Month-to-month', 'One year' ,'Two year'], key='contract')
            st.selectbox(' Streaming Movies', options=['No', 'Yes'],key='paperlessbilling')
            st.selectbox(' Streaming Movies', options=['Electronic check', 'Mailed check', 'Bank transfer (automatic)',
            'Credit card (automatic)'],key='paymentmethod')
        st.number_input('Enter Monthly Charges', min_value=20, max_value=120, step=50,key='monthlycharges')
        st.number_input('Enter Total Charges', min_value=20, max_value=7000, step=50,key='totalcharges')
       
        st.form_submit_button("Make Prediction", on_click= data_prediction, kwargs=dict(models = models, encoder = encoder))
       




if __name__ == "_main_":
    
    st.title('Data Prediction')
create_form()
prediction = st.session_state['prediction']
probability = st.session_state['probability']

if not prediction:
    st.markdown('#### Prediction will show here')
if prediction =='Yes':
    probability_yes = probability[0][1] * 100
    st.markdown(f'The employee will leave the company with the probability of {round(probability_yes, 2)}%')
else:
    probability_no = probability[0][0] * 100
    st.markdown(f'The employee will leave the company with the probability of {round(probability_no, 2)}%')    
    
        #  model_selection()
final_prediction = st.session_state['prediction']


   
# st.write('final_prediction')
# st.write(st.session_state)