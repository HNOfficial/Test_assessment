import numpy as np
import glob
import datetime as dt
import os
import pandas as pd

df = pd.read_csv('Trip-Info.csv')

df['pd_datetime'] = pd.to_datetime(df['date_time'], format='%Y%m%d%H%M%S')

df['ts'] = df['pd_datetime'].values.astype(np.int64) // 10 ** 9

csv_files = glob.glob('EOL-dump/*.csv')
vehicle_filelist = (pd.read_csv(file) for file in csv_files)
df_vehlist = pd.concat(vehicle_filelist, ignore_index=True)

reg_number = []

for i in os.listdir('EOL-dump/'):
    i = os.path.splitext(i)[0]
    reg_number.append(i)

df_filtered = df[df['vehicle_number'].isin(reg_number)]

df_filtered = df_filtered.sort_values(['vehicle_number', 'ts'], ascending=[True, True])

df_vehlist['latlongsum'] = df_vehlist['lat'] + df_vehlist['lon']

df_vehlist_final = df_vehlist.drop_duplicates(['latlongsum'])

start_time_list = df_filtered['ts'].tolist()

df_vehlist_final = df_vehlist_final.drop(columns=['ign', 'case_open', 'panic', 'latlongsum', 'Unnamed: 0'])

df_filtered = df_filtered.drop(columns=['date_time'])

df_vehlist_final = df_vehlist_final.sort_values(['lic_plate_no', 'tis'], ascending=[True, True])

df_filtered.to_csv('trip_info_filtered.csv')
df_vehlist_final.to_csv('EoL_dump_filtered.csv')



