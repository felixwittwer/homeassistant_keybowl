# Firmware

This is a small guide about the structure of the firmware and how to install it on your pi zero 2.

## structure

low level code for all the individual parts

**-> components**

some routines

**-> routines**

the dashboards to show

**-> dashboards**

besides the folder there is the **main.py** which is the main script that needs to be executed. 

## setup the firmware

### General and Python Setup 

Install Raspberry Pi OS Lite

``` bash
sudo apt update && sudo apt upgrade -y
sudo apt install python3 python3-pip git
```

### clone the Repo

``` bash
git clone https://github.com/felixwittwer/homeassistant_keybowl.git
```

``` bash
cd homeassistant_keybowl
```

### Install the required python packages

``` bash
pip install -r requirements.txt
```

### Enable I2C and Serial

``` bash
sudo raspi-config
```

- (enable I2C)
- enable Serial (disable shell, enable hardware serial)

Reboot!

### SPI Setup

- Make sure SPI is enabled on your Pi

``` bash
sudo raspi-config
```
(Interface Options -> SPI -> Enable)

Reboot if asked!

- confirm SPI device nodes:
``` bash
ls /dev/spidev0.*
```

### MQTT Setup for Homeassistant

(this command is not really neadded when you installed everything via the requirements.txt)

``` bash
pip install paho-mqtt
```

Inside Homeassistant make sure you have a MQTT Broker like Mosquitto installed and enabled.

### Neopixel Setup

``` bash
sudo pip install rpi_ws281x adafruit-circuitpython-neopixel
sudo python -m pip install --force-reinstall adafruit-blinka
```

### Run the firmware

``` bash
python3 main.py
```

### Setup autostart on boot

open with

``` bash
sudo nano /etc/rc.local
```

and add :
``` bash
python3 /home/pi/homeassistant_keybowl/main.py 
```

above exit 0