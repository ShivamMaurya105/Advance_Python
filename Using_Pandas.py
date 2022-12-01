import pandas as pd
import numpy as np
import urllib.request
# link of the csv file
a='https://gist.githubusercontent.com/aakashns/f6a004fa20c84fec53262f9a8bfee775/raw/f309558b1cf5103424cef58e2ecb8704dcd4d74c/italy-covid-daywise.csv'
urllib.request.urlretrieve(a,'italy-covid-daywise.csv')
covid_df=pd.read_csv('italy-covid-daywise.csv')
covid_df
type(covid_df)          #Return Type of csv
covid_df.info()         #Return info of csv
covid_df.describe()     #Return description of csv
covid_df.columns        #Return columns of csv
covid_df.shape          #Return shape of csv
