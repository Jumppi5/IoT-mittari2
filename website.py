import csv
import sys
import logging
import io

def print_to_string(list):
    output = io.StringIO()
    print(list, file=output)
    contents = output.getvalue()
    output.close()
    return contents

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

csvpt1k = []
csvhumidity = []
csvtemperature = []
csvdate = []

try:
    with open('mittaukset.csv') as f:
        csvdata = csv.reader(f, delimiter=',')
        for row in csvdata:
            csvpt1k.append(row[0])
            csvhumidity.append(row[1])
            csvtemperature.append(row[2])
            csvdate.append(row[3])

    htmlcode = '''
                <!DOCTYPE html>
                <html>
                <body style="background-color:#F0F8FF;">
                <h1 style="text-align:left;">Temperature and humidity </h1>

                <p id = "PT100 temperature" ><b>PT1000 temperature:      '''+str(csvpt1k[-1])+''' Celsius</b></p>
                <p id = "DHT temperature" ><b>DHT temperature:  '''+str(csvtemperature[-1])+''' Celsius</b></p>
                <p id = "Humidity" ><b>Humidity:        '''+str(csvhumidity[-1])+''' %RH</b></p>
                
                <style type="text/css">
                    .chart-container {
                        width: 800px;
                        height: 400px;
                    }
                </style>

                <div class="chart-container" style="background-color:#FFFFFF;">
                    <canvas id="myChart"></canvas>
                </div>
                <div class="chart-container" style="background-color:#FFFFFF;">
                    <canvas id="myChart2"></canvas>
                </div>
                <div class="chart-container" style="background-color:#FFFFFF;">
                    <canvas id="myChart3"></canvas>
                </div>
                
                <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
                <script>
                const ctx = document.getElementById('myChart').getContext('2d');
                const myChart = new Chart(ctx, {
                    type: 'line',
                    data: {
                        labels: '''+print_to_string(csvdate)+''',
                        datasets: [{
                            label: 'PT1000',
                            data: '''+print_to_string(csvpt1k)+''',
                            backgroundColor: [
                                'rgba(255, 99, 132, 0.2)',
                                'rgba(54, 162, 235, 0.2)',
                                'rgba(255, 206, 86, 0.2)',
                                'rgba(75, 192, 192, 0.2)',
                                'rgba(153, 102, 255, 0.2)',
                                'rgba(255, 159, 64, 0.2)'
                            ],
                            borderColor: [
                                'rgba(255, 99, 132, 1)',
                                'rgba(54, 162, 235, 1)',
                                'rgba(255, 206, 86, 1)',
                                'rgba(75, 192, 192, 1)',
                                'rgba(153, 102, 255, 1)',
                                'rgba(255, 159, 64, 1)'
                            ],
                            borderWidth: 1,
                            pointRadius: 0
                        }]
                    },
                    options: {
                        scales: {
                            x: {
                                ticks: {
                                	maxTicksLimit: 32
                                }
                            },
                            y: {
                                beginAtZero: true
                            }
                        }
                    }
                });

                const ctx2 = document.getElementById('myChart2').getContext('2d');
                const myChart2 = new Chart(ctx2, {
                    type: 'line',
                    data: {
                        labels: '''+print_to_string(csvdate)+''',
                        datasets: [{
                            label: 'Humidity',
                            data: '''+print_to_string(csvhumidity)+''',
                            backgroundColor: [
                                'rgba(255, 99, 132, 0.2)',
                                'rgba(54, 162, 235, 0.2)',
                                'rgba(255, 206, 86, 0.2)',
                                'rgba(75, 192, 192, 0.2)',
                                'rgba(153, 102, 255, 0.2)',
                                'rgba(255, 159, 64, 0.2)'
                            ],
                            borderColor: [
                                'rgba(255, 99, 132, 1)',
                                'rgba(54, 162, 235, 1)',
                                'rgba(255, 206, 86, 1)',
                                'rgba(75, 192, 192, 1)',
                                'rgba(153, 102, 255, 1)',
                                'rgba(255, 159, 64, 1)'
                            ],
                            borderWidth: 1,
                            pointRadius: 0
                        }]
                    },
                    options: {
                        scales: {
                            x: {
                                ticks: {
                                	maxTicksLimit: 32
                                }
                            },
                            y: {
                                beginAtZero: true
                            }
                        }
                    }
                });

                const ctx3 = document.getElementById('myChart3').getContext('2d');
                const myChart3 = new Chart(ctx3, {
                    type: 'line',
                    data: {
                        labels: '''+print_to_string(csvdate)+''',
                        datasets: [{
                            label: 'DHT temperature',
                            data: '''+print_to_string(csvtemperature)+''',
                            backgroundColor: [
                                'rgba(255, 99, 132, 0.2)',
                                'rgba(54, 162, 235, 0.2)',
                                'rgba(255, 206, 86, 0.2)',
                                'rgba(75, 192, 192, 0.2)',
                                'rgba(153, 102, 255, 0.2)',
                                'rgba(255, 159, 64, 0.2)'
                            ],
                            borderColor: [
                                'rgba(255, 99, 132, 1)',
                                'rgba(54, 162, 235, 1)',
                                'rgba(255, 206, 86, 1)',
                                'rgba(75, 192, 192, 1)',
                                'rgba(153, 102, 255, 1)',
                                'rgba(255, 159, 64, 1)'
                            ],
                            borderWidth: 1,
                            pointRadius: 0
                        }]
                    },
                    options: {
                        scales: {
                            x: {
                                ticks: {
                                	maxTicksLimit: 32
                                }
                            },
                            y: {
                                beginAtZero: true
                            }
                        }
                    }
                });
                </script>
                </body>
                </html>'''

    f2 = open('mittaukset.html','w')
    f2.write(htmlcode)
    f2.close()

    csvpt1k = []
    csvhumidity = []
    csvtemperature = []
    csvdate = []

except Exception as error:
    logger.exception(error)
