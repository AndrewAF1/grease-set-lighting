import color_consts as cc
import utils as u
import LED_commands as lc
from time import sleep

import serial as s


ser = s.Serial('/dev/ttyACM1', 9600)

#lc.flash(ser, 1, cc.GREEN, 100, 500)
u.manual(ser)
