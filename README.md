# led-wall-clock
A fancy RGB LED matrix wall clock controlled by a Raspberry Pi.

![picture](http://michaellunzer.com/img/lunzpi_finished2.jpg)

# Parts List
- [https://www.adafruit.com/product/420](https://www.adafruit.com/product/420)
- [Adafruit RGB Matrix + Real Time Clock Hat](https://www.adafruit.com/product/2345)
- Raspberry Pi 2 Model B
- [Acrylic Mount Plate](http://www.ponoko.com/build-your-own/furniture/led-wall-clock-plate-13293#) ([with light sensor](http://www.ponoko.com/build-your-own/furniture/led-wall-clock-plate-rev2-13311))

# Dependencies
Python libraries
- [rpi-rgb-led-matrix](https://github.com/hzeller/rpi-rgb-led-matrix)
- requests
- apscheduler
- daemonify
- Supervisor (to start program at boot)

# RGB Matrix Hat Modification
The brightness can be controlled by pulse-width-modulating the OE pin of the LED matrix.  Unfortunately, the hat does not have the PWM pin of the Raspberry Pi connected to the OE pin.  To correct this, jumper a wire between pins labeled 4 and 18 on the hat.

# RGB Matrix Library Build Instructions
Clone this repository and submodules to your Raspberry Pi
```
git clone --recursive https://github.com/jeffkub/led-wall-clock.git
cd led-wall-clock/rpi-rgb-led-matrix
```
Edit `lib/Makefile` and uncomment the following two DEFINES
```
# Uncomment the following line for Adafruit Matrix HAT gpio mappings.
# If you have an Adafruit HAT ( https://www.adafruit.com/products/2345 ),
# you need to use this option as the HAT swaps pins around that are not
# compatible with the default mapping.
DEFINES+=-DADAFRUIT_RGBMATRIX_HAT

# Uncomment if you want to use the Adafruit HAT with stable PWM timings.
# The newer version of this library allows for much more stable (less flicker)
# output, but it does not work with the Adafruit HAT unless you do a
# simple hardware hack on them:
# connect GPIO 4 (old OE) with 18 (the new OE); there are
# convenient solder holes labeled 4 and 18 on the Adafruit HAT, pretty
# close together.
# Then uncomment the following define and recompile.
DEFINES+=-DADAFRUIT_RGBMATRIX_HAT_PWM
```
Build and install the Python library
```
make build-python
sudo make install-python
```
# Starting the Clock
To start the clock as a daemon
```
cd led-wall-clock
sudo ./ledclock.py -d start
```

# Starting at Boot
I was having trouble running a python script at boot. I tried putting the path to the script in /etc/init.d and was having some problems.
I tried cron -- it didn't work
I tried calling it with a bash script -- didn't work either

I thought maybe there were some permission issues with controlling the GPIO because the program was running, but not actually displaying anything on the display.

I found [Supervisor](http://supervisord.org/) and used it to run the python scripts at boot. Also, it monitors the script, so if it crashes, they get restarted.

Here is a good [tutorial](https://serversforhackers.com/monitoring-processes-with-supervisord)

# Light Sensor

I used an analog light sensor to adjust the screen brightness. This is updated every 3 seconds, because if there wasn't a delay, the screen would flicker whenever a shadow passed over the sensor. Now, it is more consistant and only changes when there is a noticible change - like turning off a light switch. 

# To Do
- Use a more generic weather API
- Move configuration to a separate file
- Add forecast screen (toggle on a timer)
