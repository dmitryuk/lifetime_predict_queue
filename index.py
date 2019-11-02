from lifelines import WeibullAFTFitter
from lifelines import LogLogisticAFTFitter
import pandas as pd
import numpy as np
from matplotlib import pyplot
from pickle import loads, dump


df = pd.read_csv('data.csv')

seconds_in_week = 7*24*60*60
df['sin_time'] = np.sin(2*np.pi*df.start_from_week_seconds/seconds_in_week)
df['cos_time'] = np.cos(2*np.pi*df.start_from_week_seconds/seconds_in_week)
df = df.drop('start_from_week_seconds', axis=1)
#sudo apt-get install python3-tk
pyplot.plot(df['sin_time'], df.cos_time, 'o')

#pyplot.show()
wf = WeibullAFTFitter().fit(df, "duration")
wf.print_summary()
file = open('model.data', 'wb')
dump(wf, file)

#wf.predict_survival_function(df,conditional_after=)