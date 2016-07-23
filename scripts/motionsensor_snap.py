from gpiozero import MotionSensor
from time import sleep
from picamera import PiCamera
from datetime import datetime

pir = MotionSensor(4)
camera = PiCamera()

#camera.start_preview()

while True:
	pir.wait_for_motion()
	print("Motion Detected!")
	filename = datetime.now().strftime("%Y-%m-%d_%H.%M.%S.jpg")
	print(filename)
	#camera.capture(filename)
	sleep(5)
#camera.stop_review()
