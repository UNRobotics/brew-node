#!/usr/bin/python
import datetime
import sys

config_file = "config/app.settings" # Configuration file, this is the default setting.
log_file = "logs/client.log" # Log file, default setting.
clients = {} #Dictionary listing clients IP addresses.


# Open and init the log file.
logFile = open(log_file, "w", -1)
def log(message):
    timestamp = datetime.datetime.now()
    completeMessage = str(timestamp) + ": " + message
    logFile.write(completeMessage)
    print(completeMessage)
    
log("Starting Robobrew")

# Read configuration file and set variables appropriately. If missing value, exit.
sys.exit(1)