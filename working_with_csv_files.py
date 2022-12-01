from email import header
from gettext import npgettext
import numpy as np
import urllib.request
from xml.etree.ElementTree import Comment
urllib.request.urlretrieve('https://gist.githubusercontent.com/BirajCoder/a4ffcb76fd6fb221d76ac2ee2b8584e9/raw/4054f90adfd361b7aa4255e99c2e874664094cea/climate.csv','climate.txt')
climate_data=np.genfromtxt('climate.txt',delimiter=',',skip_header=1)
weights=([0.3,0.2,0.5])
yields=climate_data@weights
yields1=yields.reshape(10000,1)
print(yields1)
print(climate_data)
climate_results=np.concatenate((climate_data,yields1),axis=1)
np.savetxt ('climate_after.txt',climate_results,fmt='%.2f',delimiter=',',header='temp,rainfall,humidity,yield')
