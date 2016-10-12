import time
from WifiBulbClass import WifiBulb

# create a couple of WifiBulbs
light1 = WifiBulb("192.168.2.40")
light2 = WifiBulb("192.168.2.37")
light3 = WifiBulb("192.168.2.44")

# connect
light1.connect()
light2.connect()
light3.connect()

# set color according to (R, G, B)
light1.setColor((255,0,0))
light2.setColor((0,255,0))
light3.setColor((0,0,255))

time.sleep(5)

light1.setColor((0,0,0))
light2.setColor((0,0,0))
light3.setColor((0,0,0))

time.sleep(5)

light1.disconnect()
light2.disconnect()
light3.disconnect()