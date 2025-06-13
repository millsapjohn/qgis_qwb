from qgis.PyQt.QtWidgets import QDockWidget, QMainWindow
from qgis.PyQt.QtCore import Qt
from qgis.utils import iface
from .qwb_panel import QWBPanel


class QWBPlugin:
    def __init__(self, iface):
        self.iface = iface

    def initGui(self):
        self.dock = QWBPanel(self.iface)
        self.iface.addDockWidget(Qt.DockWidgetArea.RightDockWidgetArea, self.dock)

    def unload(self):
        self.iface.removeDockWidget(self.dock)
        self.dock.deleteLater()
