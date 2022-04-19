import time
import statistics
from datetime import datetime
import Adafruit_GPIO.SPI as SPI
import Adafruit_MCP3008
import Adafruit_DHT
import sys
import logging

#Software SPI config
CLK = 18
MISO = 23
MOSI = 24
CS = 25
mcp = Adafruit_MCP3008.MCP3008(clk=CLK, cs=CS, miso=MISO, mosi=MOSI)

Ra = float(4700)
Rb = float(878)
Rc = float(4700)
Vin = float(5)

tempList = []

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

tempMean = float(0)
humidity = float(0)
temperature = float(0)


try:
	for i in range(60):
		#read ADC values in a list
		values =  [0]*8
		for i in range(8):
			values[i] = mcp.read_adc(i)
		value = float(values[0]) #CH0

		voltage = (value/1024)*5
		gain = 20
		Vb = voltage/gain
		R = (Rc*(Rb*Vin+Ra*Vb+Rb*Vb))/(Ra*Vin-Ra*Vb-Rb*Vb)
		T = 0.257*R-257

		tempList.append(T)
		time.sleep(1)

	tempMean = statistics.mean(tempList)
	tempMean = round(tempMean, 1)
	tempList = []

	date = datetime.now()
	datestr = date.strftime("%d.%b %H:%M")

	humidity, temperature = Adafruit_DHT.read_retry(Adafruit_DHT.DHT22, 12)
	if type(humidity) == int or type(humidity) == float:
		humidity = round(humidity, 1)
	if type(temperature) == int or type(temperature) == float:
		temperature = round(temperature, 1)

	with open('mittaukset.csv','a') as f:
                sys.stdout = f
                print(str(tempMean)+","+str(humidity)+","+str(temperature)+","+datestr)
                sys.stdout = sys.stdout #reset standard output

except OSError:
        pass

