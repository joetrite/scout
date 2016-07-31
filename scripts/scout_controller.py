from time import sleep
from gpiozero import MotionSensor
from picamera import PiCamera
from datetime import datetime
import sys
import logging
from openalpr import Alpr

pir = MotionSensor(4)
camera = PiCamera()

SLEEP_TIME=.5
DATA_DIR='/app/scout_plates/data/incoming/'

print("Waiting for PIR to settle")
pir.wait_for_no_motion()

while True:
	try:
		print("Ready")
		pir.wait_for_motion()
		timestamp=datetime.now().strftime("%Y-%m-%d_%H.%M.%S")

		print("motion detected at: " + timestamp)
		#Image Capture	
		pic_filename = timestamp + '.jpg'

		camera.capture(DATA_DIR + pic_filename)

		sleep(SLEEP_TIME)
	except (KeyboardInterrupt, SystemExit):
		print "Keyboard Interrupt"
		sys.exit(0)
