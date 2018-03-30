# Pi Camera Application

from picamera import PiCamera
from time import sleep

def camLive(camera, duration):
    camera.rotation = 180
    camera.start_preview()
    sleep(duration)
    camera.stop_preview()

myCamera = PiCamera()
camLive(myCamera, 5)
