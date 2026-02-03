import robomaster
from robomaster import robot
import time
import cv2
robomaster.config.ROBOT_IP_STR = '192.168.50.250'
ep_robot = robot.Robot()
ep_robot.initialize(conn_type='ap')
r=[]
def on_detect_robot(robot_info):
    global r
    r=robot_info
    print(robot_info)
ep_robot.camera.start_video_stream(display=False)
ep_robot.vision.sub_detect_info(name='robot',callback=on_detect_robot)
while 1:
    a=ep_robot.camera.read_cv2_image(strategy='newest')
    if r:
        c=r[0]
        x,y,w,h=c[0]*1280,c[1]*720,c[2]*1280,c[3]*720
        x1=int(x-w/2)
        x2 = int(x+w/2)
        y1=int(y-h/2)
        y2 = int(y+h/2)
        cv2.rectangle(a,(x1,y1),(x2,y2),(230,140,90),10)
    cv2.imshow('robot',a)
    b=cv2.waitKey(40)
    if b==27:
        break
ep_robot.vision.unsub_detect_info(name='robot')
cv2.destroyAllWindows()
ep_robot.camera.stop_video_stream()
ep_robot.close()