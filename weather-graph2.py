from requests import get
import matplotlib.pyplot as plt
from dateutil import parser

url= 'https://apex.oracle.com/pls/apex/raspberrypi/weatherstation/getallmeasurements/505307'

pages=1

weather= get(url).json()

data=weather['items'] # saving first set of data

#collecting data for 1 month
while 'next' in weather and pages<9:
	url= weather['next']['$ref']
	print url
	weather=get(url).json()
	data+=weather['items']
	pages+=1

temperatures=[] # list of temperatures
timestamps=[]

for record in data: # populating list with temperature and coresponding timestamps
	temp= record ["ambient_temp"]
	time =record["reading_timestamp"]
	temp = temp * (9/5) + 32 # converting Celsius to Fahrenheit
	temperatures.append(temp)
	timestamps.append(parser.parse(time))

# create a plot of timestamps against temperature and show it

plt.plot(timestamps, temperatures)
plt.ylabel('Temperature')
plt.xlabel('Time')
plt.show()
