from pickle import load, dump
import pandas as pd
import numpy as np
from matplotlib import pyplot

file = open('model.data', 'rb')
wf = load(file)
#wf.print_summary()

df = pd.read_csv('test.csv')
seconds_in_week = 7*24*60*60
df['sin_time'] = np.sin(2*np.pi*df.start_from_week_seconds/seconds_in_week)
df['cos_time'] = np.cos(2*np.pi*df.start_from_week_seconds/seconds_in_week)

#df = df.drop('start_from_week_seconds', axis=1)

print(wf.predict_median(df))
#wf.print_summary()