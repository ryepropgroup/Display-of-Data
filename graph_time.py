import pyqtgraph as pg
import time


class graph_time(pg.PlotItem):

    def __init__(self, parent=None, name=None, labels=None, title='Time (sec)', viewBox=None, axisItems=None, enableMenu=True, font=None, **kargs):
        super().__init__(parent, name, labels, title, viewBox, axisItems, enableMenu, **kargs)

        self.hideAxis('bottom')
        self.hideAxis('left')
        self.time_text = pg.TextItem("test", anchor=(0.5, 0.5), color="r")
        if font != None:
            self.time_text.setFont(font)
        self.addItem(self.time_text)
        self.count = 0

    def update(self):
        self.count += 1
        time.sleep(0.1)
        text = str(self.count/10)
        self.time_text.setText(text)




