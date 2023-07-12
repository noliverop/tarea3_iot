import asyncio
from bleak import BleakScanner
from PyQt5.QtCore import QObject, QRunnable, pyqtSlot, pyqtSignal

class BtScanSignals(QObject):
    # Señal que se activa cuando termina la búsqueda de dispositivos
    search_done = pyqtSignal(object)

class BtScanWorker(QRunnable):
    """
    Worker para escanear dispositivos Bluetooth cercanos
    """

    def __init__(self):
        super(BtScanWorker, self).__init__()
        self.signals = BtScanSignals()


    @pyqtSlot()
    def run(self):
        async def search():
            devices = await BleakScanner.discover(timeout=10.0)
            return devices

        devices = asyncio.run(search())
        self.signals.search_done.emit(devices)