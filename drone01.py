from codrone_edu.drone import *

drone = Drone()
drone.pair()

battery = drone.get_battery()
print("Battery:", battery, "%")

drone.set_drone_LED(0, 255, 0, 100)    # red, green, blue, brightness
drone.drone_buzzer(440, 500)    # 440 Hz for 500 milliseconds

drone.takeoff()      # lift to about 80 cm and hover
drone.hover(6)       # stay there for 6 seconds
drone.land()         # settle down

drone.close()