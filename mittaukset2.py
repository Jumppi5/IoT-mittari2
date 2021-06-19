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

while True:
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
                tempMean = round(tempMean, 2)
                tempList = []
                dateTimeObj = datetime.now()
                timeObj = dateTimeObj.time()
                humidity, temperature = Adafruit_DHT.read_retry(Adafruit_DHT.DHT22, 12)
                humidity = round(humidity, 2)
                temperature = round(temperature, 2)
		
                text = '''
                <!DOCTYPE html>
                <html>
                <body>
                <h1 style="text-align:left;">Temperature and humidity</h1>
                <p id = "PT100 temperature" ><b>PT100 temperature:      '''+str(tempMean)+''' Celsius</b></p>
                <p id = "DHT temperature" ><b>DHT temperature:  '''+str(temperature)+''' Celsius</b></p>
                <p id = "Humidity" ><b>Humidity:        '''+str(humidity)+''' %RH</b></p>

                </body>
                </html>'''

                with open('mittaukset.html','w') as f:
                        sys.stdout = f
                        print(text)
                        sys.stdout = sys.stdout #reset standard output
        except Exception as error:
                logger.exception(error)

