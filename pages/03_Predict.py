import streamlit as st
import pandas as pd
import joblib
import numpy as np

# create page lay out
st.set_page_config(
    page_title='Predict Data',
    page_icon = ':)',
    layout='wide'
)


# write title for preiction page
st.title('♣️ Prediction Page')

# create funtion for gradient boost pipiline
st.cache_resource(show_spinner='Model loading')
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


if 'prediction' not in st.session_state:
    st.session_state['prediction'] = None
if 'probability' not in st.session_state:
    st.session_state['probability'] = None


# code to make a preidction
def data_prediction(models, encoder):
    gender = st.session_state['gender']
    seniorcitizen = st.session_state['seniorcitizen']
    partener = st.session_state['partener']
    dependants = st.session_state['dependants']
    tenure = st.session_state['tenure']
    phoneservice = st.session_state['phoneservice']
    multiplelines = st.session_state['multiplelines']
    internateservice = st.session_state['internateservice']
    onlinesecurity = st.session_state['onlinesecurity']
    onlinebackup = st.session_state['onlinebackup']
    deviceprotection = st.session_state['deviceprotection']
    techsupport = st.session_state['techsupport']
    streamingtv = st.session_state['streamingtv']
    streamingmovies = st.session_state['streamingmovies']
    contract = st.session_state['contract']
    paperlessbilling = st.session_state['paperlessbilling']
    paymentmethods = st.session_state['paymentmethods']
    monthlycharges = st.session_state['monthlycharges']
    totalcharges= st.session_state['totalcharges']

    columns =['gender', 'SeniorCitizen', 'Partner', 'Dependents', 'tenure',
        'PhoneService', 'MultipleLines', 'InternetService', 'OnlineSecurity',
        'OnlineBackup', 'DeviceProtection', 'TechSupport', 'StreamingTV',
        'StreamingMovies', 'Contract', 'PaperlessBilling', 'PaymentMethod',
        'MonthlyCharges', 'TotalCharges']
    
    data = [[gender, seniorcitizen, partener, dependants,tenure, phoneservice, multiplelines, internateservice, onlinesecurity,
              onlinebackup, deviceprotection, techsupport, streamingtv, streamingmovies, contract, paperlessbilling,
              paymentmethods, monthlycharges, totalcharges]]
    
# create  a data frame
    df = pd.DataFrame(data, columns=columns)

# make prediction
    # pred = models.predict(df)
    # # pred = int(pred[0])
    # prediction = encoder.inverse_transform(pred)

  # Make prediction
    pred = models.predict(df)
    # Iconverting  it to a 1D array
    pred = np.array([pred])
    # Now 'pred' is a 1D array with a single element
    prediction = encoder.inverse_transform(pred)
   
    

    probability = models.predict_proba(pred)


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
        
            gender = st.number_input('input age', min_value=18, max_value=60, step=1, key='gender')
            seniorcitizen = st.selectbox('select yes or No', options= ["yes","No"],key='seniorcitizen')
            Partener = st.selectbox('select', options= ["yes","No"], key='partener')
            dependants = st.selectbox('select yes or No', options= ["yes","No"], key= 'dependants')
        
            tenure = st.number_input('enter number of tenure', min_value=1, max_value=73, step=1, key='tenure')
            contract = st.selectbox(' Select Contract', options=['Month-to-month', 'One year' ,'Two year'], key='contract')
            Phoneservice = st.selectbox('Phone Service', options=['No phone service' ,'No' ,'Yes'],key='phoneservice')
            multiplelines = st.selectbox('Multiple Line', options=['DSL', 'Fiber optic', 'No'], key='multiplelines')
            internateservice = st.selectbox(' Internet Service', options=['No', 'Yes', 'No internet service'], key='internateservice')
            
           
        with col2:
            fg1, fg2 = st. columns(2)
            with fg1:
                pass
            with fg2:
                pass
            onlinesecurity =st.select_slider('Online security', options=['No', 'Yes', 'No internet service'],key='onlinesecurity')
            onlinebackup = st.select_slider('Online Backup', options=['Yes', 'No','No internet service'], key='onlinebackup')
            deviceprotection = st.select_slider(' Device Protection', options=['No', 'Yes', 'No internet service'],key='deviceprotection')
            techsupport = st.select_slider(' Tech Support', options=['No', 'Yes', 'No internet service'], key='techsupport')
            streamingtv = st.select_slider(' Streaming Tv', options=['No', 'Yes', 'No internet service'],key='streamingtv')
            streamingmovies = st.select_slider(' Streaming Movies', options=['No', 'Yes', 'No internet service'],key='streamingmovies')
            paperlessbilling = st.select_slider(' Streaming Movies', options=['No', 'Yes'],key='paperlessbilling')
            paymentmethods = st.select_slider(' Streaming Movies', options=['Electronic check', 'Mailed check', 'Bank transfer (automatic)',
            'Credit card (automatic)'],key='paymentmethods')
        monthlycharges = st.number_input('Enter Monthly Charges', min_value=20, max_value=120, step=50,key='monthlycharges')
        totalcharges = st.number_input('Enter Total Charges', min_value=20, max_value=7000, step=50,key='totalcharges')
       
        st.form_submit_button("Make Prediction", on_click= data_prediction, kwargs=dict(models = models, encoder = encoder))
       


create_form()

if __name__ == "_main_":
    
    st.title('Data Prediction')

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
# final_prediction = st.session_state['prediction']


   
# st.write('final_prediction')
# st.write(st.session_state)