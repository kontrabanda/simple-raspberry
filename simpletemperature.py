import w1thermsensor
from time import sleep
 
sensor = w1thermsensor.W1ThermSensor()
 
while True:
    temp = sensor.get_temperature()
    print(temp)
    sleep(5)
