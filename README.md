# EC-Online

## An online counter, made for Endercube

This is a set of code that gets the online count of a minecraft server and displays it on a 10 bar bar graph. By default this uses [http://mcapi.xdefcon.com/](http://mcapi.xdefcon.com/) and [http://worldtimeapi.org](http://worldtimeapi.org) for the time.

## The time i hear you say?

Yes! This gets the time and automagicly turns off the display between 9AM and 9PM.

## Usage

To use this, wire up a 10 bar bar graph to GPIO 0-9 on a Raspberry Pi Pico W [set up for MicroPython](https://projects.raspberrypi.org/en/projects/get-started-pico-w/1) and install all of the `.py` files. Once that is done edit `secrets.py` for your WIFI details, minecraft server and timezone.
