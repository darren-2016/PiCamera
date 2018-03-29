from picamera import PiCamera
from time import sleep


########################################
# Function:    camLive
# Parameters:  camera
#              duration
# Description:
# Returns:  
def camLive(camera, duration):
    camera.rotation = 180
    #camera.start_preview(alpha=200)
    camera.start_preview()
    camera.annotate_text = "Hello World!"
    sleep(duration)
    camera.stop_preview()

########################################
# Function:    camStill
# Parameters:  camera
# Description:
# Returns:  
def camStill(camera):
    camera.rotation = 180
    #camera.start_preview(alpha=200)
    camera.start_preview()
    sleep(5)
    camera.capture('/home/pi/Desktop/image.jpg')
    camera.stop_preview()

########################################
# Function:    camRecord
# Parameters:  camera
# Description:
# Returns:  
def camRecord(camera, duration):
    camera.rotation = 180
    camera.start_preview()
    camera.start_recording('/home/pi/video.h264')
    sleep(duration)
    camera.stop_recording()
    camera.stop_preview()
    

myCamera = PiCamera()

#camLive(myCamera, 5)
camStill(myCamera)
#camRecord(myCamera, 10)
