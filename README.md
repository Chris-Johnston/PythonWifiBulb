# WifiLedClass
A python class for controlling "MagicLight Wifi Smart LED Light Bulbs". Standalone from the Android or iOS app.

## Usage
This requires that your bulb is connected to your local network, and you have it's IP address. You can obtain the IP by looking in the app, or using NMAP to search for port 5577.

A test usage can be seen in [WifiBulb.py](WifiLight/WifiBulb.py), however here's a quick snippet:
```
# import the class
from WifiBulbClass import WifiBulb

# create a new object and assign it's IP address
IP = "192.168.x.x"
myLightBulb = WifiBulb(IP)

# connect to the bulb
myLightBulb.connect()

# send it some colors
myLightBulb.setColor((255, 0, 0))

# disconnect when finished
myLightBulb.disconnect()
```

## What type of Wifi enabled lightbulbs work?
So far I've used this with these bulbs: [Magic Light Wifi Smart Light Bulb](https://www.amazon.com/MagicLight-WiFi-Smart-Light-Bulb/dp/B00SIDVZSW).
I have used two versions of these bulbs, but they both worked with the same Android app. They list themselves as v5 and v7.
