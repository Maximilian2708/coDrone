from codrone_edu.drone import *

drone = Drone()
drone.pair()

drone.takeoff()
drone.hover(1)

drone.move_forward(67, "in", 1)
drone.turn_right(90)

drone.move_forward(38, "in", 1)
drone.turn_left(90)

drone.move_forward(70, "in", 1)
drone.turn_right(90)

drone.move_forward(90, "in", 1)

drone.land()
drone.close()