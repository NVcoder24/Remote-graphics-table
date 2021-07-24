import sys
from PyQt5 import QtWidgets
import socket

port = 5000
ip = "localhost"

print(f"port: {port}")
print(f"ip: {ip}")

class WebCanvas(QtWidgets.QLabel):

    def __init__(self):
        super().__init__()
        self.point = [0, 0]
        self.setText(f"port: {port}\nip: {ip}")

        self.sock = socket.socket()
        self.sock.bind((ip, port))
        self.sock.listen(1)

        self.conn, self.addr = self.sock.accept()

    def mousePressEvent(self, e):
        self.point[0] = e.x()
        self.point[1] = e.y()

    def mouseMoveEvent(self, e):
        x = self.point[0] - e.x()
        y = self.point[1] - e.y()

        self.point[0] = e.x()
        self.point[1] = e.y()

        self.conn.send(bytes(f"{x}|{y}", "utf-8"))

        print(x, y)

class MainWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()

        self.canvas = WebCanvas()

        w = QtWidgets.QWidget()
        l = QtWidgets.QVBoxLayout()
        w.setLayout(l)
        l.addWidget(self.canvas)

        self.setCentralWidget(w)


app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()
