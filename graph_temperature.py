import pyqtgraph as pg
from collections import deque


class graph_temperature(pg.PlotItem):
    def __init__(
        self,
        parent=None,
        name=None,
        labels=None,
        title="Temperature (ºc)",
        viewBox=None,
        axisItems=None,
        enableMenu=True,
        **kargs
    ):
        super().__init__(
            parent, name, labels, title, viewBox, axisItems, enableMenu, **kargs
        )

        self.temp_plot = self.plot(pen=(29, 185, 84))
        self.temp_data = deque(maxlen=30)
        self.ptr = 0

    def update(self, value):
        self.temp_data.append(value)
        self.ptr += 1
        self.temp_plot.setData(self.temp_data)
        self.temp_plot.setPos(self.ptr, 0)
