import color_consts as cc
import utils as u
import LED_commands as lc
from time import sleep
import random as r

import serial as s


ser2 = s.Serial("/dev/ttyACM2", 9600)

while True:
    input("go")
    sleep(1.1)
    u.sendRGB(ser2, 2, cc.YELLOW)
    sleep(1.1)
    u.sendRGB(ser2, 1, cc.YELLOW)
