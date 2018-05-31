import socket
import sys
import binascii

import time

# Mode for setting RGB color
MODE_RGB = '31'
MODE_PULSERGB = '41'

MODE_CUSTOM_GRADUAL = '3a'
MODE_CUSTOM_JUMPING = '3b'
MODE_CUSTOM_STROBE = '3c'

MODE_CUSTOM_NO_COLOR = '01020300'

def getChecksumValue(byteArray):
        """ returns the checksum value as a byte from an array of bytes """
        #sum all the values
        sumOfValues = 0
        for x in range(len(byteArray)):
            sumOfValues += byteArray[x]
        # return
        return sumOfValues % pow(2, len(byteArray) + 1) % 256

class WifiBulb(object):
    """class for controlling a wifi lightbulb"""


    mode = "31" # default mode
    magicBytes = "00f00f" # have yet to investigate what these do
    PORT = 5577

    def __init__(self, IP):
        """ constructor with IP address """
        self.IP = IP
        self.useDebug = False
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect(self):
        """ connects the socket """
        print ("Connecting to " + self.IP + " : " + str(WifiBulb.PORT) )
        try:
            self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.s.connect((self.IP, WifiBulb.PORT))
            print ("Connected to " + self.IP + ":" + str(WifiBulb.PORT))
        except:
            print ("Failed to connect to " +  self.IP + ":" + str(WifiBulb.PORT))

    def _sendmessage(self, message):
        """
        appends the given message with the checksum
        and sends it
        """
        b = bytearray.fromhex(message)
        chk = getChecksumValue(b)
        b.append(chk)
        try:
            self.s.send(b)
            # send it NOW
            # self.s.flush()
        except:
            print("Failed to set color!")

    def disconnect(self):
        """ disconnects the socket """
        self.s.close()

    def warmwhite(self, brightness = 255):
        message = WifiBulb.mode + "000000" + format(brightness, "02x") + "0f0f"
        self._sendmessage(message)

    # def nightlight(self, value):
    #     data = "31ffc39200f00f" # 07 39 changes
    #     message = WifiBulb.mode + "ff39ff" + "00f00f"
    #     self._sendmessage(message)

    def setColor(self, color):
        """sets the color the given tuple in the format (R, G, B)"""
        # print("Sending color: " + str(color))
        # mode + red + green + blue + magicBytes + checksum
        message = WifiBulb.mode + format(color[0], "02x") + format(color[1], "02x") + format(color[2], "02x") + WifiBulb.magicBytes
        self._sendmessage(message)

    def setRGBW(self, r, g, b, white):
        message = MODE_RGB + format(r, "02x") + format(g, "02x") + format(b, "02x") + format(white, "02x") + 'f00f'
        self._sendmessage(message)

    def off(self):
        b = bytearray.fromhex('71240fa4')
        self.s.send(b)

    def on(self):
        b = bytearray.fromhex('71230fa3')
        self.s.send(b)

    def pulseColor(self, color):
        message = '41' + format(color[0], "02x") + format(color[1], "02x") + format(color[2], "02x") + '00f00f'
        self._sendmessage(message)

    # seven color cross fade 6125100fa5
    # speed 50
    # speed 0                61251f0fb4

    # seven color jumping change 61381c0fc4
    # speed 88 6138040fac

    def sevenColorCrossFade(self, speed):
        message = '6125' + format(speed, '02x') + '0f'
        self._sendmessage(message)

    def sevenColorJumpingChange(self, speed):
        message = '6138' + format(speed, '02x') + '0f'
        self._sendmessage(message)

    def testing(self):
        message = '6125020f97'
        self._sendmessage(message)

    # night light very far left
    # 31ffc39200f00f84

    # strobe with speed 30, red 1, white 4
    #
    #
    # 51
    # ff000
    # 2000102030001020300
    # ffffff
    # 00010203000102030001020300010203000102030001020300010203000102030001020300010203000102030001020300023cff0fef

    # strobe
    # red green blue white
    # speed 30
    # 51ff000200ffbd3f0001020300ffffff00010203000102030001020300010203000102030001020300010203000102030001020300010203000102030001020300023cff0fe4

    # jumping
    # speed 26

    # 51ff00000000ff00000000ff00ffffff00ff6250000102030001020300010203000102030001020300010203000102030001020300010203000102030001020300063aff0f8c

    # gradual speed 26

    # 51ff00000000ff00000000ff00ffffff00ff6250000102030001020300010203000102030001020300010203000102030001020300010203000102030001020300063aff0f8c

    # lots of colors 26 jumping
    # jumping
    # 51
    # ff000000
    # 00ff0000
    # 0000ff00
    # ffffff00
    # ff181700
    # 16ff4100
    # 004df800
    # 00000000
    # ff080000
    # 00000000
    # 0019ff00
    # ffb7b200
    # a1fdff00
    # ff040000
    # 00ff2800
    # ff00ea00
    # 06 # speed
    # 3b # 3a gradual 3b jumping 3c strobe
    # ff0f9a

    # few colors
    # 51
    # ff000000
    # 00ff0000
    # 171bf200
    # 01020300 # 01020300 is the 'default color'
    # 010203000102030001020300010203000102030001020300010203000102030001020300010203000102030001020300033bff0f0d

    def customMode(self, colors, mode, speed):
        message = '51'
        for color in colors:
            message += format(color[0], "02x") + format(color[1], "02x") + format(color[2], "02x") + format(color[3], "02x")
        for x in range(16 - len(colors)):
            message += MODE_CUSTOM_NO_COLOR
        message += format(speed, "02x")
        message += mode
        message += 'ff0f'
        self._sendmessage(message)




# allow CLI for setting colors
#python3 WifiBulb.py <IP> <R> <G> <B>
# this should be expanded, could include warmwhite
if __name__ == "__main__":
    # create a bulb
    bulb = WifiBulb(sys.argv[1])
    # connect
    bulb.connect()
    # setColor
    # color = (int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]))
    # bulb.setColor(color)

    #bulb.sevenColorCrossFade(0x25)
    # bulb.testing()
    # bulb.sevenColorJumpingChange(1)

    bulb.customMode(
        [
            (255, 255, 255, 0),
            (255, 0, 0, 0),
            (0, 255, 0, 0),
            (0, 0, 255, 0),
            (0, 0, 0, 255),
            # (255, 0, 0, 255),
        ],
        # speed goes between 0x1f and 1, where 1 is faster
        MODE_CUSTOM_STROBE, 1
    )



    # disconnect
    bulb.disconnect()
