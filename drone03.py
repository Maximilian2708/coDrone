import time
from codrone_edu.drone import *

drone = Drone()
drone.connect()

drone.set_drone_LED(0, 0, 255, 100)      # blue: getting ready
drone.drone_buzzer(5000, 1000)
time.sleep(1)

drone.takeoff()
drone.set_drone_LED(0, 255, 0, 100)      # green: flying
drone.hover(3)

drone.drone_buzzer(3000, 1000)
drone.flip("back")
time.sleep(1)

drone.drone_buzzer(500, 1000)
drone.set_drone_LED(255, 255, 0, 100)    # yellow: about to land
drone.land()

drone.drone_buzzer(262, 400)
drone.drone_LED_off()

drone.disconnect()