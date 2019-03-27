from requests import get
import matplotlib.pyplot as plt
from dateutil import parser

url= 'https://apex.oracle.com/pls/apex/raspberrypi/weatherstation/getallmeasurements/505307'

weather= get (url).json()

#print weather['items'][0]['ambient_temp']

temperatures=[] #temperature list
timestamps=[]

for record in weather ['items']:
	temp= record ['ambient_temp']
	time=record['reading_timestamp']
	temp= temp * (9/5) +32 # convert Celsius to Fahrenheit
	temperatures.append(temp)
	timestamps.append(parser.parse(time))

# create a plot of timestamps against temperature and show it

plt.plot(timestamps, temperatures)
plt.ylabel('Temperature')
plt.xlabel('Time')
plt.show()
