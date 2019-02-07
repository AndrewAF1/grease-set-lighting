import serial as s

#ser = s.Serial('/dev/tty.usbserial', 9600)

#ser.write(b"test")


def manual():
    #wait for user input and repeat
    while(True):
        usr_red = input("red: ")
        usr_blue = input("blue: ")
        usr_green = input("green: ")
        sendRGB(usr_red, usr_green, usr_blue)


def sendRGB(r, b, g):
    #ser.write("RGB:" + r.encode() + b" " + b.encode() + b" " + g.encode())
    print("sent red " + r + ", blue " + b + " and green " + g)


manual()
