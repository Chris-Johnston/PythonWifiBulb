import socket
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
        print ("Connecting to : " + self.IP + " : " + str(WifiBulb.PORT) )
        try:
            self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.s.connect((self.IP, WifiBulb.PORT))
            print ("Connected to " + self.IP + ":" + str(WifiBulb.PORT))
        except:
            print ("failed to connect")

    def disconnect(self):
        """ disconnects the socket """
        self.s.detach()

    def setColor(self, color):
        """sets the color the given tuple in the format (R, G, B)"""
        print("Sending color: " + str(color))
        # the structure of the packets sent to the light are
        # pattern, red, green, blue, "00f00f", some 1 byte checksum?
        # this is a work in progress. planned to use the different patterns
        # I have yet to establish a pattern between the colors and the checksum
        # but since it's only 255 bytes, I don't think it's too big of a deal to just go with it for now

        # attempting to generate checksums
        for x in range(255):
            # mode + red + green + blue + magicBytes + checksum
            message = WifiBulb.mode + format(color[0], "02x") + format(color[1], "02x") + format(color[2], "02x") + WifiBulb.magicBytes 
            messageBytes = bytearray.fromhex(message)
            checksum = getChecksumValue(messageBytes)
            messageBytes.append(checksum)
            try:
                self.s.send(messageBytes)
            except:
                print("Failed to set color")
