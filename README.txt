This Github repo contains files for IoT temperature and humidity meter that is built using Raspberry Pi Zero W.
"mittaukset.html" and "mittaukset.csv" files are committed automatically in this repo by the Raspberry. "mittaukset.html" is the primary webpage for the user. "mittaukset.csv" is available for the user if he wants to do analysis of his own.
Other files are not necessary for the user.

Instructions for reading the website:
There are two temperatures. PT1000 sensor is the one in my own circuitry and DHT temperature is included in the humidity measurement module. DHT temperature is the goto temperature to be read. PT1000 sensor accuracy is not spesified and seems to be worse. 

Sensor accuracies:
DHT temperature +- 1 Celsius
DHT humidity +- 3 %RH
PT1000 not specified.

Measurement data resets every 10 days!
