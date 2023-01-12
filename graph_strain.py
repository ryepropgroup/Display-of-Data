import pyqtgraph as pg
from collections import deque


class graph_strain(pg.PlotItem):
    def __init__(
        self,
        parent=None,
        name=None,
        labels=None,
        title="Strain (meter/meter)",
        viewBox=None,
        axisItems=None,
        enableMenu=True,
        **kargs
    ):
        super().__init__(
            parent, name, labels, title, viewBox, axisItems, enableMenu, **kargs
        )

        self.strain_plot = self.plot(pen=(0, 185, 84))
        self.strain_data = deque(maxlen=30)
        self.ptr = 0

    def update(self, value):
        self.strain_data.append(value)
        self.ptr += 1
        self.strain_plot.setData(self.strain_data)
        self.strain_plot.setPos(self.ptr, 0)
