import pyqtgraph as pg

# import numpy as np
from collections import deque


class graph_pressure(pg.PlotItem):
    def __init__(
        self,
        parent=None,
        name=None,
        labels=None,
        title="Pressure (KPa)",
        viewBox=None,
        axisItems=None,
        enableMenu=True,
        **kargs
    ):
        super().__init__(
            parent, name, labels, title, viewBox, axisItems, enableMenu, **kargs
        )

        self.presssure_plot = self.plot(pen=(0, 185, 84))
        self.presssure_data = deque(maxlen=30)
        self.ptr = 0

    def update(self, value):
        self.presssure_data.append(int(value))
        self.ptr += 1
        self.presssure_plot.setData(list(self.presssure_data))
        self.presssure_plot.setPos(self.ptr, 0)
