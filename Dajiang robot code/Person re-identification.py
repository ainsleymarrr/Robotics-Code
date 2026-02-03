import robomaster
from robomaster import robot
import time
import cv2
robomaster.config.ROBOT_IP_STR = '192.168.50.250'
ep_robot = robot.Robot()
ep_robot.initialize(conn_type='ap')
p=[]
def on_detect_person(person_info):
    global p
    p=person_info
    print(person_info)
ep_robot.gimbal.moveto(pitch=25,yaw=0,pitch_speed=50,yaw_speed=50).wait_for_completed()
ep_robot.camera.start_video_stream(display=False)
ep_robot.vision.sub_detect_info(name='person',callback=on_detect_person)
while 1:
    a=ep_robot.camera.read_cv2_image(strategy='newest')
    if p:
        c=p[0]
        x,y,w,h=c[0]*1280,c[1]*720,c[2]*1280,c[3]*720
        x1=int(x-w/2)
        x2 = int(x+w/2)
        y1=int(y-h/2)
        y2 = int(y+h/2)
        cv2.rectangle(a,(x1,y1),(x2,y2),(230,140,90),10)
        ep_robot.chassis.drive_speed(x=2,y=0,z=0,timeout=1)
    cv2.imshow('person',a)
    b=cv2.waitKey(40)
    if b==27:
        break
ep_robot.vision.unsub_detect_info(name='person')
cv2.destroyAllWindows()
ep_robot.camera.stop_video_stream()
ep_robot.close()