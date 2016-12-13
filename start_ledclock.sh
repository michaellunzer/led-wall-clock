#!/bin/bash
PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/root/led-wall-clock

echo "loading ledclock.py ... please wait"

sudo python /root/led-wall-clock/ledclock.py -d start &


echo "should be running"
