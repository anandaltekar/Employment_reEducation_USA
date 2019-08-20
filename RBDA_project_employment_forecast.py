import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime
from statsmodels.tsa.arima_model import ARIMA

'''IMPORT DATA AND CONVERT TO DATETIME'''
dataset = pd.read_csv("allDatasets/dataset_54.csv")
name = 'leisure_and_hospitality_allEmployees'
dataset['Timestamp'] = pd.to_datetime(dataset['Timestamp'])
dataset = dataset.set_index('Timestamp')
dataset = dataset.drop(['series_id', 'year', 'period'], axis=1)
dataset = dataset.drop(dataset.columns[0], axis=1)

'''DECOMPOSE & PLOT'''
from statsmodels.tsa.seasonal import seasonal_decompose
decomposition = seasonal_decompose(dataset)
trend = decomposition.trend
seasonal = decomposition.seasonal
residual = decomposition.resid

# plt.subplot(411)
# plt.plot(dataset, label='Original', color='red')
# plt.legend(loc='best')
# plt.subplot(412)
# plt.plot(trend, label='Trend')
# plt.legend(loc='best')
# plt.subplot(413)
# plt.plot(seasonal, label='Seasonal')
# plt.legend(loc='best')
# plt.subplot(414)
# plt.plot(residual, label='Residual')
# plt.legend(loc='best')
# plt.tight_layout()
# plt.show()

'''AUTO ARIMA'''
from pyramid.arima import auto_arima
stepwise_model = auto_arima(dataset, start_p=1, start_q=1,
                           max_p=6, max_q=3, m=21,
                           start_P=0, seasonal=True,
                           d=1, D=1, trace=True,
                           error_action='ignore',
                           suppress_warnings=True,
                           stepwise=True)
print(stepwise_model.aic())

stepwise_model.fit(dataset)

future_forecast = list(stepwise_model.predict(n_periods=12))
#print(future_forecast)

temp_future = [
    ['2019-01-01', future_forecast[0]],
    ['2019-02-01', future_forecast[1]],
    ['2019-03-01', future_forecast[2]],
    ['2019-04-01', future_forecast[3]],
    ['2019-05-01', future_forecast[4]],
    ['2019-06-01', future_forecast[5]],
    ['2019-07-01', future_forecast[6]],
    ['2019-08-01', future_forecast[7]],
    ['2019-09-01', future_forecast[8]],
    ['2019-10-01', future_forecast[9]],
    ['2019-11-01', future_forecast[10]],
    ['2019-12-01', future_forecast[11]],
]
future = pd.DataFrame(temp_future, columns = ['Timestamp', 'value'])
future['Timestamp'] = pd.to_datetime(future['Timestamp'])
future = future.set_index('Timestamp')
frames = [dataset, future]
result = pd.concat(frames)
print(result.tail(24))

output_path = 'results/employment_forcasts/tables'
#result.to_csv
filepath = os.path.join(output_path, name+'.csv')
result.to_csv(filepath)
