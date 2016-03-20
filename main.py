#!/usr/bin/python
import datetime
import sys

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