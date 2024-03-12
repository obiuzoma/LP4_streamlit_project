Table of content

* Customers Churn Behaviour
Custome Churn Behavior app is  designed to help companies  to predict wheather a customer will stop using  their phone services or not
* features


| Column           | Description                                           |
|------------------|-------------------------------------------------------|
| Gender           | Whether the customer is a male or a female            |
| SeniorCitizen    | Whether a customer is a senior citizen or not          |
| Partner          | Whether the customer has a partner or not (Yes, No)   |
| Dependents       | Whether the customer has dependents or not (Yes, No)  |
| Tenure           | Number of months the customer has stayed with the company |
| Phone Service    | Whether the customer has a phone service or not (Yes, No) |
| MultipleLines    | Whether the customer has multiple lines or not        |
| InternetService  | Customer's internet service provider (DSL, Fiber Optic, No) |
| OnlineSecurity   | Whether the customer has online security or not (Yes, No, No Internet) |
| OnlineBackup     | Whether the customer has online backup or not (Yes, No, No Internet) |
| DeviceProtection | Whether the customer has device protection or not (Yes, No, No internet service) |
| TechSupport      | Whether the customer has tech support or not (Yes, No, No internet) |
| StreamingTV      | Whether the customer has streaming TV or not (Yes, No, No internet service) |
| StreamingMovies  | Whether the customer has streaming movies or not (Yes, No, No Internet service) |
| Contract         | The contract term of the customer (Month-to-Month, One year, Two years) |
| PaperlessBilling | Whether the customer has paperless billing or not (Yes, No) |
| Payment Method   | The customer's payment method (Electronic check, mailed check, Bank transfer(automatic), Credit card(automatic)) |
| MonthlyCharges   | The amount charged to the customer monthly            |
| TotalCharges     | The total amount charged to the customer              |
| Churn            | Whether the customer churned or not (Yes or No)       |

### Built with
 Tech Stack
 ### Front End
* Streamlit
#### Back End
    * Python
#### Database
    * Microsoft SQL Server
#### Deployment and Hosting
    * Render
### Key Features
    * Home page with the login feature and description of what the application is all about
    * View of proprietary data loaded from server
    *Dashboaord page for visualization OF KPI and EDA
    * prediction page in which users can save for futher analysis
    * History  page in which user can view their prediction values
### Getting Started
#### Prereqiites
To run this app on your machine you must have the following inatlled on your machine
    *Python
#### Set Up 
clone this repositary on your loca machine
cd my_folder
clone https://github.com/obiuzoma/LP4_streamlit_project.git

Change into the cloned repository
cd LP4_streamlit_project

Create a virtual environment
python -m virtual_env env

Activate the virtual environment
virtual_env/Scripts/activate

### Install

Install all the packages needed for the project
pip install -r requirement.txt

### Usagess
Write the following command

streamlit run main.py

* A web page opens up to view the application
* Login to the app with username = uzoma, password= abc



