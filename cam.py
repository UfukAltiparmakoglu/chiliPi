#!/usr/bin/python3

from picamera import PiCamera
from time import sleep
from datetime import datetime

cam = PiCamera()
timeStamp = str(datetime.now().isoformat()).split('.')[0]

cam.start_preview()
sleep(5)
cam.capture('/home/pi/chiliPi/chili_pic_'+timeStamp+'.jpg')
cam.stop_preview()

