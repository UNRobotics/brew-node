#!/usr/bin/python
import datetime
import sys
import smbus
import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(11, GPIO.OUT)

bus = smbus.SMBus(1)

DEVICE_ADDRESS = 0x48

config_file = "config/app.settings" # Configuration file, this is the default setting.
log_file = "logs/client.log" # Log file, default setting.
servers = {"localhost"} #Dictionary listing clients IP addresses.
debug = True #set to false to run on production system.

# Open and init the log file.
logFile = open(log_file, "w", -1)
def log(message):
    timestamp = datetime.datetime.now()
    completeMessage = str(timestamp) + ": " + message
    logFile.write(completeMessage)
    if debug:
        print(completeMessage)
    
log("Starting Robobrew")

# Start defining functions here.
def getTemp():
    #Pull the temp from the I2C probe. Return it.
    #I2C address: 0x48 (1 to read, 0 to write)
	

    return convertReadings(conversion1, conversion3)

def convertReadings( channel0, channel3 ):
	#Mesured resistors, needs to be changed.
	R1 = 17914
	R2 = 11926
	R3 = 17972
	C1 = R3/(R3+R2)
	M = (((-1*channel3)*1.024*2**15)/(channel0*4.096)) + C1
	RT = (R1*M)/(2**15 - M)
	
	return RT

def sendToServers(temp):
    #For each server in servers, send to the REST api
    for server in servers:
        log("Sending to server " + server)
        #TODO: Finish this
# Read configuration file and set variables appropriately. If missing value, exit.

# Gather temp and send it
log("Temp: " + str(getTemp()))

logFile.close()
