import color_consts as cc
import utils as u
import LED_commands as lc
from time import sleep
import random as r

import serial as s


#ser0 = s.Serial('/dev/ttyACM0', 9600)
#ser1 = s.Serial('/dev/ttyACM1', 9600)
ser2 = s.Serial('/dev/ttyACM2', 9600)
#u.manual(ser0)
u.manual(ser2)

#lc.flash(ser, 1, cc.GREEN, 100, 500)
#s_num = int(input("Arduino number: "))
#if s_num == 0:
#    u.manual(ser0)
#elif s_num == 1:
#    u.manual(ser1)

#input()
#u.sendRGB(ser0, 1, cc.BLUE)
#u.sendRGB(ser1, 1, cc.RED)

#input()
#u.sendRGB(ser0, 2, cc.GREEN)
#u.sendRGB(ser1, 2, cc.ORANGE)


#input()
#lc.flash(ser0, 1, cc.BLUE, 100, 500)
#lc.flash(ser1, 1, cc.RED, 100, 500)

#input()
#lc.flash(ser0, 2, cc.GREEN, 100, 500)
#lc.flash(ser1, 2, cc.ORANGE, 100, 500)

#sleep(2)
#siezure mode
#while True:

#    input("siezure")
#    lc.flash(ser0, 1, r.choice(cc.COLORS), 100, 50)
#    lc.flash(ser1, 1, r.choice(cc.COLORS), 100, 50)
#    lc.flash(ser2, 1, r.choice(cc.COLORS), 100, 50)
#
#    sleep(2)

#    lc.flash(ser0, 2, r.choice(cc.COLORS), 100, 50)
#    lc.flash(ser1, 2, r.choice(cc.COLORS), 100, 50)
#    lc.flash(ser2, 2, r.choice(cc.COLORS), 100, 50)

    #input("stop oh god please")
    #u.sendRGB(ser0, 1, cc.OFF)
    #u.sendRGB(ser1, 1, cc.OFF)
    #u.sendRGB(ser2, 1, cc.OFF)
    #sleep(1.1)
    #u.sendRGB(ser0, 2, cc.OFF)
    #u.sendRGB(ser1, 2, cc.OFF)
    #u.sendRGB(ser2, 2, cc.OFF)



input()
u.sendRGB(ser0, 1, cc.OFF)
input()
u.sendRGB(ser0, 2, cc.OFF)
input()
u.sendRGB(ser1, 2, cc.OFF)
