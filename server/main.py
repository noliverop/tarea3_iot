from iot import Ui_Dialog
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QThreadPool
import numpy as np
import pyqtgraph as pg
from bt_scanner import BtScanWorker
from bleak import BLEDevice
import DatabaseWorker as db
import pygatt

adapter = pygatt.GATTToolBackend()

CHARACTERISTIC_UUID_DATA = "0000ee01-0000-1000-8000-00805f9b34fb"
CHARACTERISTIC_UUID_CONFIG = "0000ff01-0000-1000-8000-00805f9b34fb" # ID de la caracteristica del servicio
status = 10
subscribed = False
device = None



import struct

def create_byte_array(data_list):
    byte_array = bytearray()

    for item in data_list:
        if isinstance(item, int):
            # Pack the integer as a 4-byte signed integer (int32)
            byte_array.extend(struct.pack('>i', item))
        elif isinstance(item, str):
            # Convert the string to bytes and append
            byte_array.extend(item.encode('utf-8'))
        elif isinstance(item, float):
            # Pack the float as a 8-byte float (float64)
            byte_array.extend(struct.pack('>d', item))
        else:
            raise ValueError(f"Unsupported type: {type(item)}")

    return byte_array


class Controller(QtWidgets.QDialog):

    def __init__(self):
        super(Controller,self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.status = [0, 20, 21, 22, 23, 30, 31]
        self.protocol = [1, 2, 3, 4, 5]
        
        self.bt_devices = []

        self.plot_vars = ["temperatura", "humedad","Acc_x","Acc_y","Acc_z","RMS"]

        #buscar señales
        self.thread_pool = QThreadPool()
        self.ui.search_esp32.clicked.connect(self.on_bt_search_start)
        self.ui.boton_detener.clicked.connect(self.on_device_stop)

        self.ui.boton_graficar.clicked.connect(self.graficar)
        self.ui.detener.clicked.connect(self.detener_graficos)

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

        elif disp.name is not None and type(disp) == BLEDevice and disp.name == "ESP_GATTS_DEMO":
            #global status
            print("es dispositivo y es BLE")          
            global adapter
            adapter.start()  
            global device
            device = adapter.connect(MAC, timeout=2.0)
            self.ui.search_esp32.setText("Conectado")
            self.ui.search_esp32.setEnabled(False) 
            id_device,status,id_protocol,acc_sam,acc_sens,gyro,bme688,dis,tcp,udp,host,ssid,passw = db.getConfig()
            self.ui.text_acc_sampling.setText(str(acc_sam))
            self.ui.text_acc_sensibity.setText(str(acc_sens))
            self.ui.text_gyro_sensibility.setText(str(gyro))
            self.ui.textEdit_18.setText(str(bme688))
            self.ui.text_disc_time.setText(str(dis))
            self.ui.text_tcp_port.setText(str(tcp))
            self.ui.text_udp_port.setText(str(udp))
            self.ui.text_host_ip.setText(str(host))
            self.ui.text_ssid.setText(str(ssid))
            self.ui.text_pass.setText(str(passw))

            #self.ui.selec_10.setCurrentIndex(self.status.index(status))
            #self.ui.selec_11.setCurrentIndex(self.protocol.index(id_protocol))


            payload = create_byte_array([status,id_protocol,acc_sam,acc_sens,gyro,bme688,dis,tcp,udp,host,ssid,passw])
            print(f"Writing config")
            device.char_write(CHARACTERISTIC_UUID_CONFIG, payload, wait_for_response=True)



            #config = bt.bt_read_caracts(device.address)
            #print(config)

    def on_device_stop(self):
        global adapter
        adapter.stop()
        global device 
        device = None
        self.ui.search_esp32.setEnabled(True) 
        self.ui.search_esp32.setText("Buscar ESP-32")
        self.ui.text_acc_sampling.setText("")
        self.ui.text_acc_sensibity.setText("")
        self.ui.text_gyro_sensibility.setText("")
        self.ui.textEdit_18.setText("")
        self.ui.text_disc_time.setText("")
        self.ui.text_tcp_port.setText("")
        self.ui.text_udp_port.setText("")
        self.ui.text_host_ip.setText("")
        self.ui.text_ssid.setText("")
        self.ui.text_pass.setText("")
    
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
        x1 = [50,100,150,200,250,300,350,400,450,500]

        #data = np.array([x,y1])

        print("Plot 1 grafica " + var_select1)

        plot1.getItem(0,0).plot(x=x1,y=y1)

        # grafico 2

        plot2 = self.ui.plot2 
        
        var_select2 = self.plot_vars[self.ui.selec_plot2.currentIndex()]
        y2 = np.random.randint(30,size=10)
        x2 = [50,100,150,200,250,300,350,400,450,500]

        p = plot2.addPlot()
        p.showGrid(x=True,y=True)
        p.setAxisItems({"bottom":pg.DateAxisItem()})


        print("Plot 2 grafica " + var_select2)
        plot2.getItem(0,0).plot(x=x2,y=y2)

        # grafico 3

        plot3 = self.ui.plot3 

        var_select3 = self.plot_vars[self.ui.selec_plot3.currentIndex()]
        y3 = np.random.randint(30,size=10)
        x3 = [50,100,150,200,250,300,350,400,450,500]

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

