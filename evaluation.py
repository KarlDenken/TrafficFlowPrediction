import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt
import h5py 
import torch

# ## Read data
data_path = 'data/metr-la.h5'
h5 = h5py.File(data_path, 'r')
data = h5['df']
speeds = data['block0_values'][:] # speeds (34272, 207)
df = pd.DataFrame(speeds)
print(df)

def ha_predict(df, period=12 * 24 * 7, test_ratio=0.2, null_val=0.):
    '''
    Calculates the historical average of sensor reading
    :param df: data frame
    :param period: default 1 week
    :param test_ratio:
    :param null_val: default 0
    :return:
    '''
    n_sample, n_sensor = df.shape
    n_test = int(round(n_sample * test_ratio))
    n_train = n_sample - n_test
    y_test = df[-n_test:]
    y_predict = pd.DataFrame.copy(y_test)

    for i in range(n_train, min(n_sample, n_train + period)):
        inds = [j for j in range(i % period, n_train, period)]
        historical = df.iloc[inds, :]

