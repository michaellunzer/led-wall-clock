#!/bin/bash

sudo apt-get install git -y
sudo apt-get install build-essential -y
sudo apt-get install gcc -y
sudo apt-get install python-dev -y
sudo apt-get install -y supervisor

git clone --recursive https://github.com/michaellunzer/led-wall-clock.git
cd led-wall-clock/rpi-rgb-led-matrix

sed -i -e 's/#DEFINES+=-DADAFRUIT_RGBMATRIX_HAT/DEFINES+=-DADAFRUIT_RGBMATRIX_HAT/g' /led-wall-clock/rpi-rgb-led-matrix/lib/Makefile
sed -i -e 's/#DEFINES+=-DADAFRUIT_RGBMATRIX_HAT_PWM/DEFINES+=-DADAFRUIT_RGBMATRIX_HAT_PWM/g' /led-wall-clock/rpi-rgb-led-matrix/lib/Makefile

make build-python
sudo make install-python

cp -f /root/led-wall-clock/supervisor/conf.d/ledclock.conf /etc/supervisor/conf.d/ledclock.conf
cp -f /root/led-wall-clock/supervisor/conf.d/touch_5pad.conf /etc/supervisor/conf.d/touch_5pad.conf

sed -i -e 's/;[inet_http_server]/[inet_http_server]/g' /etc/supervisord.conf
sed -i -e 's/;port=9001/port=9001/g' /etc/supervisord.conf

sudo mkdir /var/log/ledclock
sudo mkdir /var/log/touch_5pad

supervisorctl reread
supervisorctl update
