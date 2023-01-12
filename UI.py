import sys
from pyqtgraph.Qt import QtGui, QtWidgets
import pyqtgraph as pg
import socket
import threading
from graph_time import graph_time
from graph_temperature import graph_temperature
from graph_pressure import graph_pressure
from graph_strain import graph_strain
from communication import Communication

pg.setConfigOption("background", (33, 33, 33))
pg.setConfigOption("foreground", (197, 198, 199))
# Interface variables
app = QtWidgets.QApplication(sys.argv)
view = pg.GraphicsView()
Layout = pg.GraphicsLayout()
view.setCentralItem(Layout)
view.show()
view.setWindowTitle("Engine monitoring")
view.resize(900, 300)

# declare object for serial Communication
ser = Communication()
# Fonts for text items
font = QtGui.QFont()
font.setPixelSize(90)

# buttons style
style = "background-color:rgb(29, 185, 84);color:rgb(0,0,0);font-size:14px;"


HOST = "127.0.0.1"
PORT = 65432
conn = None


def connection():
    global conn
    global res
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        try:
            s.bind((HOST, PORT))
        except Exception:
            print("Exception Error: Unable to Open Specified Port: " + str(PORT))
            return
        s.listen()
        conn, addr = s.accept()
        with conn:
            print(f"Connected by {addr}")
            # connect_button.pack_forget()
            # connected()
            #            conn.sendall(b"Welcome to Borealis Mission Control")
            # s.recv()
            while True:
                rec = conn.recv(1024).decode("utf-8")
                pressure.update(int(res))
                if not rec:
                    conn.close()
                    sys.exit(1)


connection_thread = threading.Thread(target=connection, daemon=True)


def connect():
    connection_thread.start()


# Button
def button_action(self):
    connect()


button = QtWidgets.QGraphicsProxyWidget()
save_button = QtWidgets.QPushButton("Button 1")
save_button.setStyleSheet(style)
save_button.clicked.connect(button_action)
button.setWidget(save_button)

# Temperature graph
temperature = graph_temperature()
# Pressure Graph
pressure = graph_pressure()
# Strain Graph
strain = graph_strain()
# Time graph
time = graph_time(font=font)

text = """MACH"""
Layout.addLabel(text, col=1, colspan=21)
Layout.nextRow()

l1 = Layout.addLayout(colspan=100, rowspan=1).addLayout(rowspan=5, border=(83, 83, 83))

# Creating the modules
l1.addItem(button)
l1.addItem(strain)
l1.addItem(temperature)
l1.addItem(pressure)
l1.addItem(time)


def update():
    try:
        value_chain = []
        value_chain = ser.getData()
        strain.update(value_chain[1])
        temperature.update(value_chain[3])
        time.update()
    except IndexError:
        print("starting, please wait a moment")


if True:
    timer = pg.QtCore.QTimer()
    timer.timeout.connect(update)
    timer.start(1)
else:
    print("something is wrong with the update call")

if __name__ == "__main__":
    QtWidgets.QApplication.instance().exec()
