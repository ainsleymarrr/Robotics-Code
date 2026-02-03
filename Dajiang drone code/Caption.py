from robomaster import robot
import time
# if __name__ == '__main__':
tl_drone = robot.Drone()
tl_drone.initialize(conn_type='sta')
# tl_drone.config_sta(ssid='ROBOROBO', password='61919801')
cross='''000rr000000rr000000rr000rrrrrrrrrrrrrrrr000rr000000rr000000rr000'''
heart='''000000000r0000r0rrr00rrrrrrrrrrrrrrrrrrr0rrrrrr000rrrr00000rr000'''
# tl_drone.led.set_led_blink(freq=4,r1=255,g1=0,b1=0,r2=0,g2=0,b2=255)
tl_drone.led.set_mled_char(display_char='A')
time.sleep(1)
tl_drone.close()
