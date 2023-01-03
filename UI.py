import sys
from pyqtgraph.Qt import QtGui, QtCore, QtWidgets
import pyqtgraph as pg
from PyQt5.QtWidgets import QPushButton
from graph_time import graph_time
from graph_temperature import graph_temperature
from graph_pressure import graph_pressure
from graph_strain import graph_strain
from communication import Communication

pg.setConfigOption('background', (33, 33, 33))
pg.setConfigOption('foreground', (197, 198, 199))
# Interface variables
app = QtWidgets.QApplication(sys.argv)
view = pg.GraphicsView()
Layout = pg.GraphicsLayout()
view.setCentralItem(Layout)
view.show()
view.setWindowTitle('Engine monitoring')
view.resize(900, 300)

# declare object for serial Communication
ser = Communication()
# Fonts for text items
font = QtGui.QFont()
font.setPixelSize(90)

# buttons style
style = "background-color:rgb(29, 185, 84);color:rgb(0,0,0);font-size:14px;"

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

l1 = Layout.addLayout(colspan=100, rowspan=1)
l11 = l1.addLayout(rowspan=5, border=(83, 83, 83))

#Creating the modules
l11.addItem(strain)
l11.addItem(temperature)
l11.addItem(pressure)
l11.addItem(time)




def update():
    try:
        value_chain = []
        value_chain = ser.getData()
        strain.update(value_chain[1])
        pressure.update(value_chain[4])
        temperature.update(value_chain[3])
        time.update()
    except IndexError:
        print('starting, please wait a moment')


if True:
    timer = pg.QtCore.QTimer()
    timer.timeout.connect(update)
    timer.start(1)
else:
    print("something is wrong with the update call")

if __name__ == '__main__':
        QtWidgets.QApplication.instance().exec()


