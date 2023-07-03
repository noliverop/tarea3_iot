from iot import Ui_Dialog
from PyQt5 import QtCore, QtGui, QtWidgets
import numpy as np
import pyqtgraph as pg

class Controller:

    def __init__(self, parent):
        self.ui = Ui_Dialog()
        self.parent = parent

        self.plot_vars = ["temperatura", "humedad","Acc_x","Acc_y","Acc_z","RMS"]

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
    Dialog = QtWidgets.QDialog()
    cont = Controller(parent=Dialog)
    ui = cont.ui
    ui.setupUi(Dialog)
    Dialog.show()
    cont.setSignals()
    sys.exit(app.exec_())

