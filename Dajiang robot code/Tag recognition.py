import robomaster
from robomaster import robot
import time
robomaster.config.ROBOT_IP_STR = '192.168.50.250'
ep_robot = robot.Robot()
ep_robot.initialize(conn_type='ap')
def on_detect_marker(marker_info):
    global markers, count
    if marker_info:
        markers= marker_info
        count = 0
    else:
        count += 1
        if count >= 10:
            count = 0
            markers.clear()
markers=[]
count=0
ep_robot.vision.sub_detect_info(name='marker', callback=on_detect_marker)

ep_robot.camera.start_video_stream(display=True, resolution='360p')

n=0
while n < 100:
    print(markers)
    time.sleep(0.1)
    n += 1
    if markers:
        ep_robot.led.set_led(comp='all', r=255, g=0, b=0,effect='on', freq=1)
    else:
        ep_robot.led.set_led(comp='all', r=255, g=0, b=0, effect='off', freq=1)
time.sleep(10)
ep_robot.camera.stop_video_stream()

ep_robot.close()