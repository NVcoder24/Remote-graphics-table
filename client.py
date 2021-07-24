import socket
from pynput.mouse import Button, Controller

mouse = Controller()

port = 6000
ip = "192.168.1.107"
multiplier = 1

def networking():
    sock = socket.socket()
    sock.connect((ip, port))

    while True:
        data = sock.recv(1024)
        data = data.decode("utf-8")
        data = data.split("|")

        try:
            x = data[0]
            y = data[1]
            x = -int(x)
            y = -int(y)
            x *= multiplier
            y *= multiplier
        except:
            x = 0
            y = 0

        mouse.move(x, y)

def mouse_btn_handling():
    pass

networking()
