from time import sleep
from picamera import PiCamera
from datetime import datetime
import sys
import logging

camera = PiCamera()


while True:
	camera.start_preview()

