# Red White & Blue
# sample program for the 4th of july

import time
from WifiBulb import WifiBulb

# define IPs
IP_left =   "192.168.88.51"
IP_mid =    "192.168.88.50"
IP_right =  "192.168.88.47"

light_left = WifiBulb(IP_left)
light_mid = WifiBulb(IP_mid)
light_right = WifiBulb(IP_right)

# re-use these methods over and over again
def red(bulb):
    bulb.setColor((255,0,0))

def white(bulb):
    bulb.warmwhite(255)

def blue(bulb):
    bulb.setColor((0,0,255))

# loop forever
while(True):
    # since I don't have any state checking, just keep re-connecting
    light_left.connect()
    light_mid.connect()
    light_right.connect()

    print("setting to red, white, blue")
    red(light_left)
    white(light_mid)
    blue(light_right)

    time.sleep(5)

    print("setting to red")
    red(light_right)
    red(light_mid)
    red(light_left)

    time.sleep(5)

    print("setting to white")
    white(light_right)
    white(light_mid)
    white(light_left)

    time.sleep(5)

    print("setting to blue")
    blue(light_right)
    blue(light_mid)
    blue(light_left)

    time.sleep(5)
