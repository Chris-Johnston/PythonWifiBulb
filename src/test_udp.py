import sys
import socket
from threading import Thread
import time

#IP_ADDR = '10.42.0.232'
IP_ADDR = '10.10.123.3'
UDP_PORT = 48899

# msg = 'HF-A11ASSISTHREAD'
messages = [
    'HF-A11ASSISTHREAD',
    # '+ok',
    'AT+WMODE=STA\r',
    'AT+H\r',
    'AT+ENTM',
    'AT+TCPLK\r'
    # 'AT+Z\r',
    #'+okAT+WMODE',
    #'AT+WSLK',
    # 'AT+WSSSID',
    # 'ATE',
    # 'AT+RST',
    # 'AT+WSKEY'
    # 'AT+WMODE=STA',
    # 'AT+Z',
    # 'AT+Z',
    # 'AT+Z',
    # 'AT+Q',
    # 'AT+Q',
]

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect((IP_ADDR, UDP_PORT))

def recv():
    while True:
        data = s.recv(1024 * 2)
        if not data: sys.exit(0)
        #print('got', data)
        print(data.decode('utf-8'))

Thread(target=recv).start()

for m in messages:
    print('Sent:', m)
    b = m.encode()
    s.send(b)
    #time.sleep(0.4)


# msg = ''
#
# for m in messages: msg += m
#
# b = msg.encode()
#
# s.send(b)

