import color_consts as cc
import utils as u
from time import sleep
import serial as s

ser0 = s.Serial("/dev/ttyACM0", 9600)
ser1 = s.Serial("/dev/ttyACM1", 9600)
ser2 = s.Serial("/dev/ttyACM2", 9600)

while True:
    input("go")
    u.sendRGB(ser2, 1, cc.YELLOW_WHITE)
    sleep(1.1)
    u.sendRGB(ser2, 2, cc.YELLOW_WHITE)
