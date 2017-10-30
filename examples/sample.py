import time
from WifiBulb import WifiBulb

# create a bulb
light1 = WifiBulb("10.42.0.232") # put your actual IP here

# connect
light1.connect()

# set to green
light1.setColor((0,255,0))
time.sleep(2)

# set to white
light1.warmwhite(255)
time.sleep(1)
# dim
light1.warmwhite(127)
time.sleep(1)

# turn off first
light1.setColor((0,0,0))

# disconnect when finished
# note that disconnecting wont turn it off
light1.disconnect()
