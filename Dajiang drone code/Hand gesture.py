import robomaster
from robomaster import robot
from robomaster import led
from robomaster import time
import time
import cv2
robomaster.config.ROBOT_IP_STR="192.168.50.250"
ep_robot=robot.Robot()
ep_robot.initialize(conn_type="ap")

def on_detect_gesture(gesture_info):
    if gesture_info:
        print(gesture_info)

ep_robot.camera.start_video_stream(display=False)
ep_robot.vision.sub_detect_info(name='marker',callback=on_detect_gesture())

while True:
    img=ep_robot.camera.read_cv2_image(strategy='newest')
    cv2.imshow('Robot',img)
    Key=cv2.waitKey(40)
    if Key==27:
        break

ep_robot.camera.stop_video_stream()
ep_robot.vision.unsub_detect_info(name='gesture')
cv2.destroyAllWindows()
ep_robot.close()