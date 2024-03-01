import streamlit as st
import pandas as pd
import altair as alt
import plotly.express as px

st.set_page_config(
    page_title='Customers Churn Dashboard',
    page_icon = "🏂",
    layout='wide',
    # initial_sidebar_state="expanded"
)
alt.themes.enable("dark")
st.title('🏂 Customers Churn Dashboard')


# read data table for dashboard
df = pd.read_csv('data_churn.csv')

col1, col2 = st.columns(2)
with col1:
    pass
with col2:
    choose_options = st.selectbox('Choose Dashboard', options=('KPI', 'EDA'))




#  understand the churn rate of customers
total_customers = len(df["Churn"])
churn_customer = len(df[df['Churn'] == 1])
non_churn_customer = len(df[df['Churn'] == 0])
churn_rate = churn_customer / total_customers * 100

# create four columns
kpi1, kpi2, kpi3, kpi4 = st.columns(4)

def create_kpi():   
# fill in those three columns with respective metrics or KPIs
    kpi1.metric(
        label="Total Customer ⏳",
        value=round(total_customers),
        # delta=round(total_customers),
)

    kpi2.metric(
        label="Churn Customers 💍",
        value=round(churn_customer),
        # delta=round(churn_customer),
)

    kpi3.metric(
        label="Non Churn Customer",
        value=int(non_churn_customer),
        # delta=int(non_churn_customer),
)
    kpi4.metric(
        label="Churn Rate",
        value=int(churn_rate),
        # delta=int(churn_rate),
)

# create two columns for charts
    fig_col1, fig_col2, fig_col3= st.columns(3)

    with fig_col1:
        st.markdown("#### Density Heatmap for Numerical columns")
        num_df = df.select_dtypes(include='number')
        fig = px.density_heatmap(data_frame = num_df)
        st.write(fig)
    
    
   
    with fig_col2:
        st.markdown("#### Box plot for Mumerical columns")
        num_df = df.select_dtypes(include='number')
        fig2 = px.box(data_frame = num_df)
        st.write(fig2)
    # with fig_col3:
    #     pass
def create_eda():
    eda_col1, eda_col2, eda_col3 = st.columns
    with eda_col1:
        fig_eda1 = px.histogram(data_frame = df, x='Churn', color_discrete_sequence=['orange', 'blue'])
        # fig_eda1.update_layout(barmode='group')
        st.write(fig_eda1)

if choose_options == 'KPI':
    
    st.subheader('KPIn Dashboard')
    create_kpi()
else:
    choose_options == 'EDA'
    create_eda()