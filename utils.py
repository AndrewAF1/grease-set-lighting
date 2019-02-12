import LED_commands as com
import color_consts as cc
import random as r
import time


def manual(serial_interface):
    #wait for user input and repeat
    while(True):

        usr_red, usr_green, usr_blue = collect_usr_input()
        sendRGB(serial_interface, (usr_red, usr_green, usr_blue))

        #if (input() == "red"):
            #sendRGB(cc.RED)
        #red = r.randint(0, 255)
        #green = r.randint(0, 150)
        #blue = r.randint(0, 200)

        #sendRGB((red, green, blue))

        #time.sleep(2)



def sendRGB(ser_interface, strip_num, rgb):

    #convert numbers to three-digit format
    r, g, b = str(rgb[0]), str(rgb[1]), str(rgb[2])

    while len(r) < 3:
        r = "0" + r
    while len(g) < 3:
        g = "0" + g
    while len(b) < 3:
        b = "0" + b


    if strip_num == 1:
        ser_interface.write(("1RGB: " + r + " " + g + " " + b + "\n").encode())
    if strip_num == 2:
        ser_interface.write(("2RGB: " + r + " " + g + " " + b + "\n").encode())

    print("sent red " + r + ", green " + g + " and blue " + b)


def collect_usr_input():
    while True:
        usr_red = input("red: ")
        if int(usr_red) <= 255 and int(usr_red) >= 0:
            break
    while True:
        usr_green = input("green: ")
        if int(usr_green) <= 255 and int(usr_green) >= 0:
            break
    while True:
        usr_blue = input("blue: ")
        if int(usr_blue) <= 255 and int(usr_blue) >= 0:
            break

    return usr_red, usr_green, usr_blue
