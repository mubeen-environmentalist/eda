#import libraries
from json import load
from re import A
import numpy as np 
import pandas as pd 
import seaborn as sns 
import streamlit as st
from pandas_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report
#web app title
st.markdown('''
# **Exploratory Data Analysis Web Application**
This app is developed by Muhammad Mubeen (UCAS), called **EDA App**
''')
#How to upload a file from pc
with st.sidebar.header("Upload your dataset(.csv)"):
    uploaded_file = st.sidebar.file_uploader("Upload your file", type=['csv'])
    df = sns.load_dataset('titanic')
    st.sidebar.markdown("[Example CSV file](df)")
#profiling report for pandas
if uploaded_file is not None:
    @st.cache
    def load_csv():
        csv = pd.read_csv(uploaded_file)
        return csv
    df = load_csv()
    pr = ProfileReport(df, explorative=True)
    st.header('**Input DF**')
    st.write(df)
    st.write('---')
    st.header('**Profiling report with Pandas**')
    st_profile_report(pr)
else:
    st.info('Awaiting for CSV File')
    if st.button('Press to use example data'):
        #example 
        def load_data():
            a = pd.DataFrame( np.random.rand(100, 5),
                                columns=['age', 'banana', 'car', 'Drum', 'Ear'])
            return a
        df = load_data()  
        pr = ProfileReport(df, explorative=True)
        st.header('**Input DataFrame**')
        st.write(df)
        st.write('---')
        st.header('**Profiling report with Pandas**')
        st_profile_report(pr)


    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    