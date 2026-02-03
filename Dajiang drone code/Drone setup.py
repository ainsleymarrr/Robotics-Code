from robomaster import robot
if __name__ == '__main__':
    tl_drone = robot.Drone()
    tl_drone.initialize()
    tl_drone.config_sta(ssid='ROBOROBO', password='61919801')
    tl_drone.close()
