# PythonWifiLedBulbController
A python script and class for controlling "MagicLight Wifi Smart LED Light Bulbs" without the use of the mobile app.

## Usage
Your bulb must be connected to your local network, as set up inside the app. You can get the bulb's IP address from inside the app.

### CLI Example
Bulb color can be set via the command line by specifying the IP address, and the red, green, and blue components of the color you wish to set.

```
python3 WifiBulb.py 192.168.x.x 255 0 0
```

### Code Example

A test usage can be seen in [sampleProgram.py](src/sampleProgram.py), however here's a brief snippet:
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
I have used two versions of these bulbs, but they both worked with the same Android app. They list themselves as v5 and v7. As far as I know, as long as they work with the MagicLight app, they should work with this.

## Notes on Packet Structure

I used wireshark to capture packets being sent to the bulbs from my  phone. I set up an access point on my laptop, connected both my phone and the bulb to it, and listened for all traffic between them on that interface.

The app would send TCP packets on ports 5577, and 55649. It seemed port 5577 was used for incoming traffic on the bulb.

Here's a sample of what the data in a packet may look like: `31FF00FF00F00FXX31FF00FF00F00FXX31FF00FF00F00FXX31FF00FF00F00FXX`

Note that this data is repeated. It appears that if the connection is slow, more data will be appended.


#### RGB Color
This data represents a single message to the bulb to change it to a specified RGB color.
`31FF00FF00F00FXX`

- '31' I'm not certain what this does. When using a color-picking function in the app, all messages begin with this. When using a preset, the 31 is missing from the messages.

- 'FF00FF' is the color. In this case #FF00FF (purple).

- '00F00F' are some "magic bytes". I don't know what they do, but they never changed in this pattern, so I wasn't concerned about it.

- 'XX' is the checksum value.

#### "Warm" white color
The bulb contains RGB leds as well as some white leds that give a warmer color than what the RGB leds can produce.

A "warm white" color message looks like this:
`31000000ff0f0fXX`

Again, we see '31', no idea. I'm guessing '000000' indicates and RGB value of 0, since we aren't using RGB color. 'ff' is the brightness, from 0-255 in hex. '0f0f' are magic bytes. 'XX' is the checksum value.

#### \_sendmessage
I've included a method with WifiLight that will automatically add the checksum at the end of your message, and then will send it. It can be used for testing patterns easily, without dealing with checksum values.

```python
# sends that data, with checksum at the end
# I *think* this was for some pattern I haven't recognized yet
bulb._sendmessage("31ffc39200f00f")
```
