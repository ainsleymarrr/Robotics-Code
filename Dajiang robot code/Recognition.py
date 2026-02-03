import robomaster
from robomaster import robot
import time
import cv2
robomaster.config.ROBOT_IP_STR = '192.168.50.250'
ep_robot = robot.Robot()
ep_robot.initialize(conn_type='ap')
def on_detect_robot(robot_info):
    print(robot_info)
ep_robot.camera.start_video_stream(display=False)
ep_robot.vision.sub_detect_info(name='robot',callback=on_detect_robot)
while 1:
    a=ep_robot.camera.read_cv2_image(strategy='newest')
    cv2.imshow('robot',a)
    b=cv2.waitKey(40)
    if b==27:
        break
ep_robot.vision.unsub_detect_info(name='robot')
cv2.destroyAllWindows()
ep_robot.camera.stop_video_stream()
ep_robot.close()