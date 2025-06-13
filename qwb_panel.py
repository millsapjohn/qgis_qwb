from qgis.PyQt.QtWidgets import (
    QWidget,
    QTextEdit,
    QDockWidget,
    QHBoxLayout,
    QVBoxLayout,
    QLineEdit,
    QLabel,
    QPushButton,
    QTabWidget,
)
from qgis.PyQt.QtCore import Qt
from qgis.utils import iface
from qgis.PyQt.QtWebEngineWidgets import QWebEngineView, QWebEnginePage
from qgis.PyQt.QtNetwork import QNetworkProxyFactory


class QWBPanel(QDockWidget):
    def __init__(self, iface):
        super().__init__()
        self.setWindowTitle('QWB Browser')
        self.iface = iface
        self.widget = QWidget()
        self.main_layout = QVBoxLayout()
