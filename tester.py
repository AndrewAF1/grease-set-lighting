import color_consts as cc
import utils as u
import LED_commands as lc

import serial as s


ser = s.Serial('/dev/ttyACM0', 9600)
ser.write(b"test")


#lc.flash(ser, 1, cc.BLUE, 100, 500)
#lc.fadeUp(ser, 1, 150, 5, (100, 100, 100))
u.manual(ser)
