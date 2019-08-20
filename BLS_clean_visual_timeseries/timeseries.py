import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
#import statsmodels.api as sm
#from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
#from statsmodels.tsa.stattools import adfuller
#from numpy import log
#from statsmodels.tsa.arima_model import ARIMA
#import pmdarima as pm

dataset = pd.read_csv("allDatasets/dataset_0.csv")
dataset['Timestamp'] = pd.to_datetime(dataset['Timestamp'])
dataset = dataset.set_index('Timestamp')
dataset = dataset.drop(['series_id', 'year', 'period'], axis=1)
dataset = dataset.drop(dataset.columns[0], axis=1)
#print(dataset.head())
#plt.plot(dataset)
#plt.show()
ts = dataset['value']

from statsmodels.tsa.stattools import adfuller
def test_stationarity(timeseries):

    #Determing rolling statistics
    rolmean = timeseries.rolling(window=12, center=False).mean()
    rolstd = timeseries.rolling(window=12, center=False).std()
    #rolmean = pd.rolling_mean(timeseries, window=12)
    #rolstd = pd.rolling_std(timeseries, window=12)
    #Plot rolling statistics:
    plt.plot(timeseries, color='blue',label='Original')
    plt.plot(rolmean, color='red', label='Rolling Mean')
    plt.plot(rolstd, color='black', label = 'Rolling Std')
    plt.legend(loc='best')
    plt.title('Rolling Mean & Standard Deviation')
    plt.show()
    #Perform Dickey-Fuller test:
    print ('Results of Dickey-Fuller Test:')
    dftest = adfuller(timeseries, autolag='AIC')
    dfoutput = pd.Series(dftest[0:4], index=['Test Statistic','p-value','#Lags Used','Number of Observations Used'])
    for key,value in dftest[4].items():
        dfoutput['Critical Value (%s)'%key] = value
    print (dfoutput)

#test_stationarity(ts)

ts_log = np.log(ts)
#plt.plot(ts_log)
#plt.show()

moving_avg = ts_log.rolling(window=12, center=False).mean()
#plt.plot(ts_log)
#plt.plot(moving_avg, color='red')
#plt.show()

ts_log_moving_avg_diff = ts_log - moving_avg
ts_log_moving_avg_diff.dropna(inplace=True)
#print(ts_log_moving_avg_diff.head(12))

#test_stationarity(ts_log_moving_avg_diff)

#expweighted_avg = pd.ewma(ts_log, halflife=12)
expweighted_avg = ts_log.ewm(halflife=12, ignore_na=False, min_periods=0, adjust=True).mean()
#plt.plot(ts_log)
#plt.plot(expweighted_avg, color='blue')
#plt.show()

ts_log_ewma_diff = ts_log - expweighted_avg
#test_stationarity(ts_log_ewma_diff)

#Seasonality, take the first diff:
ts_log_diff = ts_log - ts_log.shift()
#plt.plot(ts_log_diff)
#plt.show()

ts_log_diff.dropna(inplace=True)
#test_stationarity(ts_log_diff)

from statsmodels.tsa.seasonal import seasonal_decompose
decomposition = seasonal_decompose(ts)

trend = decomposition.trend
seasonal = decomposition.seasonal
residual = decomposition.resid

# plt.subplot(411)
# plt.plot(ts, label='Original', color='red')
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

#Remove seasonality and trend to use residual:

ts_log_decompose = residual
ts_log_decompose.dropna(inplace=True)
#test_stationarity(ts_log_decompose)


'''FORECAST'''
# p : This is the number of AR (Auto-Regressive) terms . Example — if p is 3 the predictor for y(t) will be
# y(t-1),y(t-2),y(t-3).
# q : This is the number of MA (Moving-Average) terms . Example — if p is 3 the predictor for y(t) will be
# y(t-1),y(t-2),y(t-3).
# d :This is the number of differences or the number of non-seasonal differences .

#FIND VALUES OF p AND q:

# Autocorrelation Function (ACF): It just measures the correlation between two consecutive (lagged version).
# example at lag 4, ACF will compare series at time instance t1…t2 with series at instance t1–4…t2–4
# Partial Autocorrelation Function (PACF): is used to measure the degree of association between y(t) and y(t-p).

from statsmodels.tsa.arima_model import ARIMA
#ACF and PACF plots:
from statsmodels.tsa.stattools import acf, pacf
lag_acf = acf(ts_log_diff, nlags=20)
lag_pacf = pacf(ts_log_diff, nlags=20, method='ols')

#plot ACF:
# plt.subplot(121)
# plt.plot(lag_acf)
# plt.axhline(y=0, linestyle='--', color='gray')
# plt.axhline(y=-1.96/np.sqrt(len(ts_log_diff)), linestyle='--', color='gray')
# plt.axhline(y=1.96/np.sqrt(len(ts_log_diff)), linestyle='--', color='gray')
# plt.title('Autocorrelation Function')

#Plot PACF:
# plt.subplot(122)
# plt.plot(lag_pacf)
# plt.axhline(y=0, linestyle='--', color='gray')
# plt.axhline(y=-1.96/np.sqrt(len(ts_log_diff)), linestyle='--', color='gray')
# plt.axhline(y=1.96/np.sqrt(len(ts_log_diff)), linestyle='--', color='gray')
# plt.title('Partial Autocorrelation Function')
# plt.tight_layout()

#plt.show()

'''ARIMA MODEL'''

model = ARIMA(ts_log, order = (8, 1, 2))
results_ARIMA = model.fit(disp=-1)
# plt.plot(ts_log_diff)
# plt.plot(results_ARIMA.fittedvalues, color='red')
# plt.title('RSS: %.4f' % sum((results_ARIMA.fittedvalues - ts_log_diff)**2))
# plt.show()

# get the predicted values and store it as series. You will notice the first month is missing because we took a
# lag of 1(shift).
prediction_ARIMA_diff = pd.Series(results_ARIMA.fittedvalues, copy=True)
print (prediction_ARIMA_diff.tail())

# convert differencing to log scale: find the cumulative sum and add it to a new series with a base value
# (here the first-month value of the log series).

prediction_ARIMA_diff_cumsum = prediction_ARIMA_diff.cumsum()
print (prediction_ARIMA_diff_cumsum.tail())

# take the exponent of the series from above (anti-log) which will be the predicted value —
# the time series forecast model.
prediction_ARIMA_log = pd.Series(ts_log.ix[0], index= ts_log.index)
prediction_ARIMA_log = prediction_ARIMA_log.add(prediction_ARIMA_diff_cumsum, fill_value=0)
print (prediction_ARIMA_log.tail())

# plot the predicted values with the original
prediction_ARIMA = np.exp(prediction_ARIMA_log)
plt.plot(ts)
plt.plot(prediction_ARIMA)
plt.title('RMSE: %.4f' % np.sqrt(sum((prediction_ARIMA-ts)**2)/len(ts)))
plt.show()
print(prediction_ARIMA.tail())
