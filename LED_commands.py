import color_consts as cc
import time as t
import utils as u
import time as t

#flash at interval
#duration in seconds, interval in milliseconds
def flash(ser_interface, strip_num, rgb, duration, interval):
    #convert numbers to three-digit format
    r, g, b = str(rgb[0]), str(rgb[1]), str(rgb[2])
    duration, interval = str(duration), str(interval)


    while len(r) < 3:
        r = "0" + r
    while len(g) < 3:
        g = "0" + g
    while len(b) < 3:
        b = "0" + b
    while len(duration) < 3:
        duration = "0" + duration
    while len(interval) < 4:
        interval = "0" + interval


    toSend = "BLK: " + r + " " + g + " " + b + " " + duration + " " + interval + "\n"

    if strip_num == 1:
        toSend = "1"+toSend
    if strip_num == 2:
        toSend = "2"+toSend

    ser_interface.write(toSend.strip().encode())
    
    print(toSend)

    print("flashing red " + r + ", green " + g + " and blue " + b + " for duration " + duration + " seconds at interval " + interval + " milliseconds.")

#fade up
def fadeUp(ser_interface, strip_num, intensitydiff, duration, color):
    pass

#fade down








# color modifiers

# adjust brightness by percent
