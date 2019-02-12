import color_consts as cc
import time as t
import utils as u

#flash at interval
def flash(ser_interface, strip_num, duration, interval, color):
    curTime = 0
    while curTime<duration:
        u.sendRGB(ser_interface, strip_num, color)
        t.sleep(interval)
        u.sendRGB(ser_interface, strip_num, cc.OFF)
        t.sleep(interval)
        curTime+=interval*2;

#fade up

#fade down








# color modifiers

# adjust brightness by percent
