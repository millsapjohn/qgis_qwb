from .qwb import QWBPlugin

def classFactory(iface):
    return QWBPlugin(iface)
