#!/usr/bin/python
import datetime
import sys
import smbus
import time
import ADS1x15
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(11, GPIO.OUT)

adc = ADS1x15.ADS1115()

DEVICE_ADDRESS = 0x48
GAIN = 1

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
	
    log("Starting conversion.")
    channel0 = adc.read_adc(0, 1)
    channel1 = adc.read_adc(1, 4)
    channel3 = adc.read_adc_difference(1, gain=4)
    
    log("Channel 0: " + str(channel0))
    log("Channel 1: " + str(channel1))
    log("Channel 3: " + str(channel3))
    
    GPIO.output(11, GPIO.HIGH)
    time.sleep(.02)


    channel0 = adc.read_adc(0, gain=GAIN)
    channel1 = adc.read_adc(1, gain=4)
    channel3 = adc.read_adc(3, gain=4)
    GPIO.output(11, GPIO.LOW)
    log("Channel 0: " + str(channel0))
    log("Channel 1: " + str(channel1))
    log("Channel 3: " + str(channel3))
    
    return 0

def sendToServers(temp):
    #For each server in servers, send to the REST api
    for server in servers:
        log("Sending to server " + server)
        #TODO: Finish this
# Read configuration file and set variables appropriately. If missing value, exit.

# Gather temp and send it
sendToServers(getTemp())

logFile.close()
