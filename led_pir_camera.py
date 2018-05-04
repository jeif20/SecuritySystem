import RPi.GPIO as GPIO
import time
from picamera import PiCamera #library for raspberry pi camera
from datetime import datetime 


GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.IN) #PIR motion sensor input pin
GPIO.setup(3, GPIO.OUT) #LED output pin
camera = PiCamera() #Camera output pin

while True:
        i=GPIO.input(4) 
        if i==0:    #When output from motion sensor is LOW will print no intruders
                print "No intruders",i 
                GPIO.output(3, 0)   #the LED will be OFF
                time.sleep(1)
        elif i==1:    #When output from motion sensor is HIGH will print intruder detected
                print "Intruder detected",i
                GPIO.output(3, 1)   #The LED will be ON
                camera.start_preview()    #The camera will be activated and will record a video of 10 seconds
                filename = datetime.now().strftime('%Y-%m-%d_%H.%M.%S.h264')    #The file recorded will be name with the date and time
                camera.start_recording(filename)
                time.sleep(10)
                camera.stop_recording()
                camera.stop_preview()
                time.sleep(1)

