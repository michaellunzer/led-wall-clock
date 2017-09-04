#!/bin/bash

#add this to /etc/apt/sources.list 
echo "deb http://mirrordirector.raspbian.org/raspbian/ jessie main contrib non-free rpi" | sudo tee --append /etc/apt/sources.list

curl -sLS https://apt.adafruit.com/add | sudo bash

sudo apt-get update

sudo apt-get install -y git build-essential python-dev python-smbus python-imaging python-pip python-pil gcc supervisor
sudo apt-get install -y i2c-tools

pip install apscheduler
pip install futures
pip install funcsigs==1.0


# need to configure I2C
# http://learn.adafruit.com/adafruits-raspberry-pi-lesson-4-gpio-setup/configuring-i2c

# Bad interaction with Sound
# https://github.com/hzeller/rpi-rgb-led-matrix#bad-interaction-with-sound

# If sound is enabled on your Pi, this will not work together with the LED matrix, as both need the same internal hardware sub-system (a first test to see if you are affected is to run the progrem with --led-no-hardware-pulse and see if things work fine then).

# If you run lsmod and see the snd_bcm2835 module, this could be causing trouble. (The library actually exits if it finds this module to be loaded).

# In that case, you should create a kernel module blacklist file like the following on your system and update your initramfs:

# CODE:
# cat <<EOF | sudo tee /etc/modprobe.d/blacklist-rgb-matrix.conf
# blacklist snd_bcm2835
# EOF

# sudo update-initramfs -u
# Reboot and confirm that the module is not loaded.



git clone --recursive https://github.com/michaellunzer/led-wall-clock.git
cd /root/led-wall-clock/rpi-rgb-led-matrix/lib

sed -i -e 's/#DEFINES+=-DADAFRUIT_RGBMATRIX_HAT/DEFINES+=-DADAFRUIT_RGBMATRIX_HAT/g' /root/led-wall-clock/rpi-rgb-led-matrix/lib/Makefile
sed -i -e 's/#DEFINES+=-DADAFRUIT_RGBMATRIX_HAT_PWM/DEFINES+=-DADAFRUIT_RGBMATRIX_HAT_PWM/g' /root/led-wall-clock/rpi-rgb-led-matrix/lib/Makefile

make build-python
sudo make install-python

cp -f /root/led-wall-clock/supervisor/conf.d/ledclock.conf /etc/supervisor/conf.d/ledclock.conf
cp -f /root/led-wall-clock/supervisor/conf.d/touch_5pad.conf /etc/supervisor/conf.d/touch_5pad.conf

sed -i -e 's/;[inet_http_server]/[inet_http_server]/g' /etc/supervisord.conf
sed -i -e 's/;port=9001/port=9001/g' /etc/supervisord.conf

sudo mkdir /var/log/ledclock
sudo mkdir /var/log/touch_5pad

#Update Supervisor
#  https://github.com/Supervisor/supervisor/issues/480
#CODE:

# sudo touch /var/run/supervisor.sock
# sudo chmod 777 /var/run/supervisor.sock
# sudo service supervisor restart

supervisorctl reread
supervisorctl update

