from math import radians, cos, sin, asin, sqrt
import numpy as np
import glob
import datetime as dt
import os
import streamlit as st
import pandas as pd
from report_generator import generator, haversine
from openpyxl.workbook import Workbook


trip_info_filtered = pd.read_csv('trip_info_filtered.csv')
Eol_dump_filtered = pd.read_csv('EoL_dump_filtered.csv')
Eol_dump_filtered = Eol_dump_filtered.sort_values('lic_plate_no')
trip_info_filtered = trip_info_filtered.sort_values('vehicle_number')
start_time_list = Eol_dump_filtered['tis'].tolist()

st.markdown('''
# **Welcome*
This is the **Report Generator** created in Streamlit using the **pandas** library.
---
''')

# Upload CSV data
with st.sidebar.header('Enter start time and end time in epoch format'):
    x = st.sidebar.number_input('Start:')
    y = st.sidebar.number_input('End:')
    st.sidebar.markdown("""
Example epoch timestamp:1519842600)
""")

if st.button('Execute'):
    @st.experimental_memo
    def load_data():
        return generator(x,y)


    # Boolean to resize the dataframe, stored as a session state variable
    st.checkbox("Use container width", value=False, key="use_container_width")

    df = load_data()

    # Display the dataframe and allow the user to stretch the dataframe
    # across the full width of the container, based on the checkbox value
    st.dataframe(df)
    file_path = 'report.xlsx'
    df.to_excel('report.xlsx')
    with open(file_path, 'rb') as my_file:
        st.download_button(label='Download', data=my_file, file_name='excel_report.xlsx',
                           mime='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')

st.write('if you do not see any data, kindly re-enter a different set of timestamps')