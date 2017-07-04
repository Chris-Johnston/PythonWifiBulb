import socket
import sys
import binascii

def getChecksumValue(byteArray):
        """ returns the checksum value as a byte from an array of bytes """
        #sum all the values
        sumOfValues = 0
        for x in range(len(byteArray)):
            sumOfValues += byteArray[x]
        # return
        return sumOfValues % pow(2, len(byteArray) + 1)

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
        self.s.detach()

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

# allow CLI for setting colors
#python3 WifiBulb.py <IP> <R> <G> <B>
# this should be expanded, could include warmwhite
if __name__ == "__main__":
    # create a bulb
    bulb = WifiBulb(sys.argv[1])
    # connect
    bulb.connect()
    # setColor
    color = (int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]))
    bulb.setColor(color)
    # disconnect
    bulb.disconnect()
