from time import sleep
from picamera import PiCamera
from datetime import datetime
import sys
import logging

camera = PiCamera()
app_dir = '/app/scout_auto/'
log_dir = app_dir + 'logs/'
dat_dir = app_dir + 'data/'

log_prefix = "scout_auto_"

log_filename = log_prefix + datetime.now().strftime("%Y-%m-%d_%H.%M.%S.log")

logging.basicConfig(filename=log_dir + log_filename,level=logging.INFO)

SLEEP_TIME=3

while True:
	try:
		
		#Image Capture	
		pic_filename = "scout_pic_" + datetime.now().strftime("%Y-%m-%d_%H.%M.%S.jpg")
		logging.debug("Capturing Pic " + pic_filename)
		camera.capture(log_dir + pic_filename)
	

		sleep(SLEEP_TIME)
	except (KeyboardInterrupt, SystemExit):
		print "Keyboard Interrupt"
		sys.exit(0)
