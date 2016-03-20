# brew-node
Temperature Logging Software for Raspberry Pi

Created by UN Robotics at the University of Nebraska-Omaha in conjunction with the [Farnam House Brewing Company](http://www.farnamhousebrewing.com)

Note: Any Raspberry Pi running this code will require the I2C libraries installed and kernel modules loaded. To do this run
````
sudo apt-get install python-smbus
sudo apt-get install i2c-tools
````
and then enable via 
````
sudo raspi-config 
````
under advance options. More information [here](https://learn.adafruit.com/adafruits-raspberry-pi-lesson-4-gpio-setup/configuring-i2c).
