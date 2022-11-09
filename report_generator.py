from math import radians, cos, sin, asin, sqrt
import numpy as np
import glob
import datetime as dt
import os
import pandas as pd

trip_info_filtered = pd.read_csv('/Users/harshaannehal/Downloads/Data test/trip_info_filtered.csv')
Eol_dump_filtered = pd.read_csv('/Users/harshaannehal/Downloads/Data test/EoL_dump_filtered.csv')


Eol_dump_filtered = Eol_dump_filtered.sort_values('lic_plate_no')
trip_info_filtered = trip_info_filtered.sort_values('vehicle_number')
start_time_list = Eol_dump_filtered['tis'].tolist()

def haversine(lat1, lon1, lat2, lon2):
    R = 6372.8  # this is in km.  For Earth radius in miles use 3959.87433

    dLat = radians(lat2 - lat1)
    dLon = radians(lon2 - lon1)
    lat1 = radians(lat1)
    lat2 = radians(lat2)

    a = sin(dLat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dLon / 2) ** 2
    c = 2 * asin(sqrt(a))

    return R * c


def generator(start_time, end_time):
    Lic = []
    Dst = []
    trp = []
    avgspd = []
    Trname = []
    viol = []
    x = 0
    count = 0
    sum_spd = 0
    viols = 0
    i=0
    while i<8166078:
        if start_time_list[i] > start_time and i < end_time:
            lat1 = Eol_dump_filtered.at[Eol_dump_filtered.index[i], 'lat']
            lon1 = Eol_dump_filtered.at[Eol_dump_filtered.index[i], 'lon']
            lat2 = Eol_dump_filtered.at[Eol_dump_filtered.index[i + 1], 'lat']
            lon2 = Eol_dump_filtered.at[Eol_dump_filtered.index[i + 1], 'lon']
            x = x + haversine(lat1, lon1, lat2, lon2)
            count = count +1
            sum_spd = sum_spd + Eol_dump_filtered.at[Eol_dump_filtered.index[i], 'spd']
            if Eol_dump_filtered.at[Eol_dump_filtered.index[i], 'osf'] == True:
                viols = viols+1
            if Eol_dump_filtered.at[Eol_dump_filtered.index[i], 'lic_plate_no'] not in Lic:
                Lic.append(Eol_dump_filtered.at[Eol_dump_filtered.index[i], 'lic_plate_no'])
                Dst.append(x)
                trp.append(count)
                avgspd.append(sum_spd/count)
                viol.append(viols)
                x=0
                count=0
                sum_spd=0
                viols=0
        i=i+1
    return pd.DataFrame({
        'License plate number': Lic,
        'Distance': Dst,
        'Number of Trips Completed': trp,
        'Average Speed': avgspd,
        'Number of Speed Violations':viol
    })




