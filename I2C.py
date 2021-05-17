from time import sleep 
from gpiozero import DistanceSensor
from signal import signal, SIGTERM, SIGHUP, pause


sensor = DistanceSensor(echo = 17, trigger = 4)

def terminate():
    exit(1)

signal(SIGTERM, terminate)
signal(SIGHUP, terminate)

while True:
    distance = sensor.value
    print("distance:")
    print(distance)
    if distance > 1:
        print("No object detected")
    if 1 > distance > 0.8:
        print("Object detected")
    if 0.8 > distance > 0.5:
        print("Object approaching")
    if 0.5 > distance > 0.2:
        print("Object is very close")
    if 0.2 > distance > 0:
        print("collision imminent")
    sleep(1)



        
            

            
    