from iot import Ui_Dialog
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QThreadPool
import numpy as np
import pyqtgraph as pg
from bt_scanner import BtScanWorker
from bleak import BLEDevice
import bt
import DatabaseWork as db
import pygatt

adapter = pygatt.GATTToolBackend()

CHARACTERISTIC_UUID_DATA = "0000ee01-0000-1000-8000-00805f9b34fb"
CHARACTERISTIC_UUID_CONFIG = "0000ff01-0000-1000-8000-00805f9b34fb" # ID de la caracteristica del servicio
status = 10
subscribed = False


class Controller(QtWidgets.QDialog):

    def __init__(self):
        super(Controller,self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        
        self.bt_devices = []

        self.plot_vars = ["temperatura", "humedad","Acc_x","Acc_y","Acc_z","RMS"]

        #buscar señales
        self.thread_pool = QThreadPool()
        self.ui.search_esp32.clicked.connect(self.on_bt_search_start)

        #seleccion de dispositivo
        self.ui.selec_esp.currentIndexChanged.connect(self.on_device_select)

    def on_bt_search_start(self):
        worker = BtScanWorker()
        worker.signals.search_done.connect(self.on_bt_search_done)
        self.ui.search_esp32.setText("Buscando ...")
        self.ui.search_esp32.setEnabled(False)

        #Iniciar busqueda
        self.thread_pool.start(worker)

    def on_bt_search_done(self,devices):
        self.ui.search_esp32.setText("Buscar ESP-32")
        self.ui.search_esp32.setEnabled(True)
        self.bt_devices = devices
        self.update_device_select()

    def update_device_select(self):
        self.ui.selec_esp.clear()

        #for device_id in self.db_devices:
        #    item = (f"ESP32: ID: {device_id}",device_id)
        #    self.ui.selec_esp.addItem(*item)

        #self.ui.selec_esp.insertSeparator(self.ui.selec_esp.count())

        for device in self.bt_devices:
            self.ui.selec_esp.addItem(f"Bluetooth: {device.name}", device)


    def on_device_select(self):

        print("se cambio dispositivo")
        disp = self.ui.selec_esp.currentData()

        MAC = disp.address

        if disp.name is None:
            print("no es dispositivo")

        elif device.name is not None and type(disp) == BLEDevice and disp.name == "ESP_GATTS_DEMO":
            print("es dispositivo y es BLE")
            if status == 10:
                device = adapter.connect(MAC, timeout=2.0)
                protocol,status = db.getConfig()
                print(f"protocol es {protocol} y status es {status}")


            payload = bytes([status, protocol])
            print(f"Writing config: status={status}, protocol={protocol}")
            device.char_write(CHARACTERISTIC_UUID_CONFIG, payload, wait_for_response=False)



            #config = bt.bt_read_caracts(device.address)
            #print(config)

        
    def setSignals(self):
        self.ui.selec_10.currentIndexChanged.connect(self.leerModoOperacion)
        self.ui.boton_detener.clicked.connect(self.criticalError)
        self.ui.boton_configuracion.clicked.connect(self.leerConfiguracion)
        self.ui.boton_graficar.clicked.connect(self.graficar)
        self.ui.detener.clicked.connect(self.detener_graficos)

    def leerConfiguracion(self):
        conf = dict()
        conf['AccSamp'] = self.ui.text_acc_sampling.toPlainText()
        conf['AccSen'] = self.ui.text_acc_sensibity.toPlainText()
        print (conf)
        return conf

    def leerModoOperacion(self):
        index = self.ui.selec_10.currentIndex()
        texto = self.ui.selec_10.itemText(index)
        print(texto)
        return texto

    def graficar(self):

        # grafico 1

        plot1 = self.ui.plot1 

        p = plot1.addPlot()
        p.showGrid(x=True,y=True)
        p.setAxisItems({"bottom":pg.DateAxisItem()})
        var_select1 = self.plot_vars[self.ui.selec_plot1.currentIndex()]
        y1 = np.random.randint(30,size=10)
        x1 = [1,2,3,4,5,6,7,8,9,10]

        #data = np.array([x,y1])

        print("Plot 1 grafica " + var_select1)

        plot1.getItem(0,0).plot(x=x1,y=y1)

        # grafico 2

        plot2 = self.ui.plot2 
        
        var_select2 = self.plot_vars[self.ui.selec_plot2.currentIndex()]
        y2 = np.random.randint(30,size=10)
        x2 = [1,2,3,4,5,6,7,8,9,10]

        p = plot2.addPlot()
        p.showGrid(x=True,y=True)
        p.setAxisItems({"bottom":pg.DateAxisItem()})


        print("Plot 2 grafica " + var_select2)
        plot2.getItem(0,0).plot(x=x2,y=y2)

        # grafico 3

        plot3 = self.ui.plot3 

        var_select3 = self.plot_vars[self.ui.selec_plot3.currentIndex()]
        y3 = np.random.randint(30,size=10)
        x3 = [1,2,3,4,5,6,7,8,9,10]

        p = plot3.addPlot()
        p.showGrid(x=True,y=True)
        p.setAxisItems({"bottom":pg.DateAxisItem()})

        print("Plot 3 grafica " + var_select3)

        plot3.getItem(0,0).plot(x=x3,y=y3)

    def detener_graficos(self):
        
        plot1 = self.ui.plot1
        plot1.clear()

        plot2 = self.ui.plot2
        plot2.clear()

        plot3 = self.ui.plot3
        plot3.clear()

    def criticalError(self):
        popup = QtWidgets.QMessageBox(parent= self.parent)
        popup.setWindowTitle('ERROR MASIVO')
        popup.setText('QUE HAS APRETADO, NOS HAS CONDENADO A TODOS')
        popup.setIcon(QtWidgets.QMessageBox.Icon.Critical)
        popup.exec()
        return

    def stop(self):
        print('Mori')
        return

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = Controller()
    Dialog.show()
    
    sys.exit(app.exec_())

