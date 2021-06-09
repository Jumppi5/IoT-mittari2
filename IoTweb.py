PT100temp = 1
DHTtemp = 2
humid = 3

text = '''
<!DOCTYPE html>
<html>
<body>

<h1 style="text-align:left;">Temperature and humidity</h1>

<p id = "PT100 temperature" ><b>PT100 temperature:	'''+PT100temp+''' Celsius</b></p>'''
+'''<p id = "DHT temperature" ><b>DHT temperature:	'''+DHTtemp+''' Celsius</b></p>'''
+'''<p id = "Humidity" ><b>Humidity:	'''+humid+''' %RH</b></p>'''

</body>
</html>


file = open("IoT-mittari.html","w")
file.write(text)
file.close()
