import robomaster
from robomaster import robot
import cv2
robomaster.config.ROBOT_IP_STR = '192.168.50.250'
ep_robot = robot.Robot()
ep_robot.initialize(conn_type='ap')
def on_detect_marker(line_info):
    global lines, count
    if line_info:
        lines=line_info
        print(lines)
        count=0
    else:
        count+=1
        if count>=10:
            count=0
            lines.clear()

def line_walking():
    error=lines[1][0]-0.5
    z_val=error*Kp
    ep_robot.chassis.drive_speed(x=0.1,y=0,z=z_val)
lines=[]
count=0
ep_robot.gimbal.moveto(pitch=-20,yaw=0,pitch_speed=100,yaw_speed=100).wait_for_completed()
ep_robot.camera.start_video_stream(display=False)
ep_robot.vision.sub_detect_info(name='line',color='blue',callback=on_detect_marker)
ep_robot.set_robot_mode('chassis_lead')
flag=0
Kp=300
while True:
    img=ep_robot.camera.read_cv2_image(strategy='newest')
    for point in lines[1:]:
        x=int(point[0]*1280)
        y=int(point[1]*720)
        cv2.circle(img,(x,y),2,color=(255,255,255))
    if len(lines)>=2:
        flag=0
        line_walking()
    else:
        flag+=1
        if flag>=20:
            ep_robot.chassis.drive_speed()
    cv2.imshow('Robot',img)
    key = cv2.waitKey(100)
    if key == 27:
        break
ep_robot.camera.stop_video_stream()
cv2.destroyAllWindows()
ep_robot.close()