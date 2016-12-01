# PythonWifiLedBulbController
A python script and class for controlling "MagicLight Wifi Smart LED Light Bulbs". Standalone from the Android or iOS app.

## Usage
This requires that your bulb is connected to your local network, and you have it's IP address. You can obtain the IP by looking in the app, or using NMAP to search for port 5577.

### CLI

Bulb color can be set from the command line as well. Ensure that `python` is python 3 not python 2. Tested in windows command line and Bash shell.

```
python3 WifiBulb.py 192.168.x.x 255 0 0
```

### In code

A test usage can be seen in [testProgram.py](WifiLight/testProgram.py), however here's a quick snippet:
```python
# import the class
from WifiBulb import WifiBulb

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

## Notes on packet structure

A while back I used Wireshark to view some packets going to the lights and managed to get this working.
Here's a sample of what the data in a packet may look like: `31FF00FF00F00FXX`

- '31' is the "mode" of the bulb. I noticed that when I changed to a different mode, this value would change. This is the only mode I've tested so far.

- 'FF00FF' is the color. In this case #FF00FF (purple).

- '00F00F' are some "magic bytes". I don't know what they do, but they never changed in this pattern, so I wasn't concerned about it.

- 'XX' is the checksum value.
