from robomaster import robot
# if __name__ == '__main__':
tl_drone = robot.Drone()
tl_drone.initialize()
#     tl_drone.config_sta(ssid='ROBOROBO', password='61919801')
tl_drone.flight.takeoff().wait_for_completed()
for i in range(3):
    tl_drone.flight.go(100,0,100,100).wait_for_completed()
    tl_drone.flight.go(100, 0, -100, 100).wait_for_completed()
    tl_drone.flight.go(-100, 0, 100, 100).wait_for_completed()
    tl_drone.flight.go(-100, 0, -100, 100).wait_for_completed()
tl_drone.flight.land().wait_for_completed()
tl_drone.close()