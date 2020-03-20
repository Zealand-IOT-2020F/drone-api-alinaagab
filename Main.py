import sys
from Drone import Drone
import time
#here you should interact with the drone
 
drone = Drone("192.168.10.1",8889)
drone.connect()
drone.takeOff()
time.sleep(1)
i = 0
while (i<4) :
    drone.forward(50)
    time.sleep(1)
    drone.right(50)
    time.sleep(1)
    drone.cw(180)
    time.sleep(1)
    drone.forward(50)
    time.sleep(1)
    drone.ccw(270)
    time.sleep(1)
    drone.forward(50)
    time.sleep(1)
    drone.cw(90)
    i +=1

drone.land()
drone.end()
