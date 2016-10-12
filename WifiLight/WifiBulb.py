#import Lightbulb as light1
import time


#light1.IP = "192.168.2.40"
#light1.connect()
#light1.setColor((255,0,0))
#time.sleep(2)
#light1.setColor((0,255,0))
#time.sleep(2)
#light1.setColor((0,0,255))
#time.sleep(2)
#light1.setColor((255,255,255))
#light1.disconnect()

#light1.IP = "192.168.2.37"
#light1.connect()
#light1.setColor((255,0,0))
#time.sleep(2)
#light1.setColor((0,255,0))
#time.sleep(2)
#light1.setColor((0,0,255))
#time.sleep(2)
#light1.setColor((255,255,255))
##if __name__ == "__main__":#
##	


# demo program for using WifiBulb class
from WifiBulbClass import WifiBulb

light1 = WifiBulb("192.168.2.40")
light2 = WifiBulb("192.168.2.37")
light3 = WifiBulb("192.168.2.44")

light1.connect()
light2.connect()
light3.connect()


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