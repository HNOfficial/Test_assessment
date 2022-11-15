IMP: Run the code files in the following sequence;
Pre_processing.py
report_generator.py
main.py

NOTE: Before running, please ensure that 'Trip-Info.csv' 'EOL-dump' folder are residing in your project folder.

'Pre_processing.py' will pre-process your raw data, and concatenate all the csv files in your 'EOL-dump' folder
into one big csv file. It will also transform standard datetime format to epoch timestamps.
Running this file will generate two csv files (trip_info_filtered.csv, EoL_dump_filtered.csv) which will further
be used in the remaining part of the project.

'report_generator.py' contains the function for the haversine formula and another function for generating the
report as directed in the task. These functions will directly be called into 'main.py'.

'main.py' is the final code that deploys your project as a streamlit API.
