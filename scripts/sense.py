from time import sleep
from sense_hat import SenseHat
from datetime import datetime
import sys
import logging

sense = SenseHat()

log_filename = "scout_log_" + datetime.now().strftime("%Y-%m-%d_%H.%M.%S.log")
logging.basicConfig(filename='/app/scout_auto/logs/' + log_filename,level=logging.INFO)

SLEEP_TIME=1800

while True:
	try:
		
		#Temperature, Humitity, Pressure
		sense.clear()
		t = sense.get_temperature()
		p = sense.get_pressure()
		h = sense.get_humidity()

		t = round(t, 1)
		p = round(p, 1)
		h = round(h, 1)

		msg = "%s,%s,%s,%s" % (datetime.now().strftime("%Y%m%d%H%M%S"),t,p,h)
		#sense.show_message(msg, scroll_speed=0.10)
		logging.info(msg)

		sleep(SLEEP_TIME)
	except (KeyboardInterrupt, SystemExit):
		print "Keyboard Interrupt"
		sense.clear()
		sys.exit(0)
