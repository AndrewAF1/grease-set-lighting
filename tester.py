import color_consts as cc
import utils as u
import LED_commands as lc

import serial as s


ser = s.Serial('/dev/ttyACM0', 9600)
ser.write(b"test")


lc.flash(ser, 100, 1.1, cc.RED)
#u.manual(ser)
