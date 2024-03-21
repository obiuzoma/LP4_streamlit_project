import streamlit as st
import pandas as pd
import pyodbc
from dotenv import dotenv_values


st.set_page_config(
    page_title='View Data',
    page_icon = ':)',
    layout='wide'    
)

st.title('🛢️Data Page',"data:")
# # # Load environment variables from .env file into a dictionary
# # environment_variables = dotenv_values('.env')

# # # Get the values for the credentials you set in the '.env' file
# # server = environment_variables.get("SERVER")
# # database = environment_variables.get("DATABASE")
# # username = environment_variables.get("USERNAME")
# # password = environment_variables.get("PASSWORD")

# # # code to connect to the server, user name, password, database and table

# # conn_str =f"DRIVER={{SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}"


# # # connection to the server using the pyodbc
# # connection = pyodbc.connect(conn_str)

# # query = "SELECT * FROM LP2_Telco_churn_first_3000"

# def
# # data = pd.read_sql(query, connection)

# # # st.dataframe(data)
df = pd.read_csv('data_churn.csv')
# st.dataframe(df)

col1, col2 = st.columns(2)
with col2:
    choose_options = st.selectbox('Select Data Columns', options=('Data columns','Numerical Columns','Categorical columns'))


if choose_options == "Numerical Columns":
    st.subheader('Numerical columns')
    st.write(df.select_dtypes(include='number'))
elif choose_options == "Categorical columns":
    st.subheader('Categorical columns')
    st.write(df.select_dtypes(include='object'))
else:
    st.subheader('Data Columns')
    st.write(df)







