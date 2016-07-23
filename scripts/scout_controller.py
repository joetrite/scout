from time import sleep
from picamera import PiCamera
from sense_hat import SenseHat
from datetime import datetime
import sys
import logging

camera = PiCamera()
sense = SenseHat()

SLEEP_TIME=5

while True:
	try:

		log_filename = "scout_log_" + datetime.now().strftime("%Y-%m-%d_%H.%M.%S.log")

		#Image Capture	
		pic_filename = "scout_pic_" + datetime.now().strftime("%Y-%m-%d_%H.%M.%S.jpg")
		logging.debug("Capturing Pic " + pic_filename)
		camera.capture('/app/scout/data/' + pic_filename)
	
		#Temperature, Humitity, Pressure
		sense.clear()

		o = sense.get_orientation_radians()
		t = sense.get_temperature()
		p = sense.get_pressure()
		h = sense.get_humidity()

		t = round(t, 1)
		p = round(p, 1)
		h = round(h, 1)

		msg = "%s,%s,%s,%s" % (datetime.now().strftime("%Y%m%d%H%M%S"),t,p,h) + ",{pitch},{roll},{yaw}".format(**o)
		#sense.show_message(msg, scroll_speed=0.10)
		#logging.info(msg)

		target = open('/app/scout/logs/' + log_filename, 'w')
		target.write(msg)
		target.close

		sleep(SLEEP_TIME)
	except (KeyboardInterrupt, SystemExit):
		print "Keyboard Interrupt"
		sense.clear()
		sys.exit(0)
