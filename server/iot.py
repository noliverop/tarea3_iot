# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Iot_tarea2.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(772, 775)
        self.Pestana_principal = QtWidgets.QTabWidget(Dialog)
        self.Pestana_principal.setGeometry(QtCore.QRect(0, 10, 761, 811))
        self.Pestana_principal.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Pestana_principal.setObjectName("Pestana_principal")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.selec_esp = QtWidgets.QComboBox(self.tab)
        self.selec_esp.setGeometry(QtCore.QRect(300, 50, 81, 31))
        self.selec_esp.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.selec_esp.setObjectName("selec_esp")
        self.search_esp32 = QtWidgets.QPushButton(self.tab)
        self.search_esp32.setGeometry(QtCore.QRect(400, 50, 121, 31))
        self.search_esp32.setStyleSheet("background-color: rgb(5, 5, 203);\n"
"color: rgb(255, 255, 255);")
        self.search_esp32.setObjectName("search_esp32")
        self.boton_configuracion = QtWidgets.QPushButton(self.tab)
        self.boton_configuracion.setGeometry(QtCore.QRect(350, 440, 93, 28))
        self.boton_configuracion.setStyleSheet("background-color: rgb(5, 5, 203);\n"
"color: rgb(255, 255, 255);")
        self.boton_configuracion.setObjectName("boton_configuracion")
        self.label_7 = QtWidgets.QLabel(self.tab)
        self.label_7.setGeometry(QtCore.QRect(150, 180, 81, 31))
        self.label_7.setObjectName("label_7")
        self.text_acc_sampling = QtWidgets.QTextEdit(self.tab)
        self.text_acc_sampling.setGeometry(QtCore.QRect(240, 180, 104, 31))
        self.text_acc_sampling.setObjectName("text_acc_sampling")
        self.text_acc_sensibity = QtWidgets.QTextEdit(self.tab)
        self.text_acc_sensibity.setGeometry(QtCore.QRect(240, 230, 104, 31))
        self.text_acc_sensibity.setObjectName("text_acc_sensibity")
        self.label_1 = QtWidgets.QLabel(self.tab)
        self.label_1.setGeometry(QtCore.QRect(80, 60, 181, 16))
        self.label_1.setStyleSheet("color: rgb(0, 0, 0);\n"
"\n"
"")
        self.label_1.setObjectName("label_1")
        self.label_9 = QtWidgets.QLabel(self.tab)
        self.label_9.setGeometry(QtCore.QRect(150, 230, 81, 31))
        self.label_9.setObjectName("label_9")
        self.text_gyro_sensibility = QtWidgets.QTextEdit(self.tab)
        self.text_gyro_sensibility.setGeometry(QtCore.QRect(240, 280, 104, 31))
        self.text_gyro_sensibility.setObjectName("text_gyro_sensibility")
        self.label_11 = QtWidgets.QLabel(self.tab)
        self.label_11.setGeometry(QtCore.QRect(150, 280, 81, 31))
        self.label_11.setObjectName("label_11")
        self.label_20 = QtWidgets.QLabel(self.tab)
        self.label_20.setGeometry(QtCore.QRect(130, 320, 91, 31))
        self.label_20.setObjectName("label_20")
        self.textEdit_18 = QtWidgets.QTextEdit(self.tab)
        self.textEdit_18.setGeometry(QtCore.QRect(240, 320, 104, 31))
        self.textEdit_18.setObjectName("textEdit_18")
        self.label_27 = QtWidgets.QLabel(self.tab)
        self.label_27.setGeometry(QtCore.QRect(130, 370, 91, 31))
        self.label_27.setObjectName("label_27")
        self.text_disc_time = QtWidgets.QTextEdit(self.tab)
        self.text_disc_time.setGeometry(QtCore.QRect(240, 370, 104, 31))
        self.text_disc_time.setObjectName("text_disc_time")
        self.text_tcp_port = QtWidgets.QTextEdit(self.tab)
        self.text_tcp_port.setGeometry(QtCore.QRect(500, 180, 104, 31))
        self.text_tcp_port.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.text_tcp_port.setObjectName("text_tcp_port")
        self.label_8 = QtWidgets.QLabel(self.tab)
        self.label_8.setGeometry(QtCore.QRect(430, 180, 51, 31))
        self.label_8.setObjectName("label_8")
        self.text_udp_port = QtWidgets.QTextEdit(self.tab)
        self.text_udp_port.setGeometry(QtCore.QRect(500, 230, 104, 31))
        self.text_udp_port.setObjectName("text_udp_port")
        self.label_10 = QtWidgets.QLabel(self.tab)
        self.label_10.setGeometry(QtCore.QRect(430, 230, 61, 31))
        self.label_10.setObjectName("label_10")
        self.text_host_ip = QtWidgets.QTextEdit(self.tab)
        self.text_host_ip.setGeometry(QtCore.QRect(500, 280, 104, 31))
        self.text_host_ip.setObjectName("text_host_ip")
        self.label_12 = QtWidgets.QLabel(self.tab)
        self.label_12.setGeometry(QtCore.QRect(430, 280, 61, 31))
        self.label_12.setObjectName("label_12")
        self.text_ssid = QtWidgets.QTextEdit(self.tab)
        self.text_ssid.setGeometry(QtCore.QRect(500, 330, 104, 31))
        self.text_ssid.setObjectName("text_ssid")
        self.label_26 = QtWidgets.QLabel(self.tab)
        self.label_26.setGeometry(QtCore.QRect(430, 330, 61, 31))
        self.label_26.setObjectName("label_26")
        self.text_pass = QtWidgets.QTextEdit(self.tab)
        self.text_pass.setGeometry(QtCore.QRect(500, 380, 104, 31))
        self.text_pass.setObjectName("text_pass")
        self.label_28 = QtWidgets.QLabel(self.tab)
        self.label_28.setGeometry(QtCore.QRect(430, 380, 61, 31))
        self.label_28.setObjectName("label_28")
        self.label_3 = QtWidgets.QLabel(self.tab)
        self.label_3.setGeometry(QtCore.QRect(530, 120, 51, 31))
        self.label_3.setObjectName("label_3")
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(260, 120, 71, 31))
        self.label_2.setObjectName("label_2")
        self.consola_1 = QtWidgets.QTextEdit(self.tab)
        self.consola_1.setGeometry(QtCore.QRect(60, 690, 681, 81))
        self.consola_1.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.consola_1.setObjectName("consola_1")
        self.label_31 = QtWidgets.QLabel(self.tab)
        self.label_31.setGeometry(QtCore.QRect(60, 660, 141, 21))
        self.label_31.setStyleSheet("color: rgb(0, 0, 0);\n"
"\n"
"")
        self.label_31.setObjectName("label_31")
        self.boton_inicio = QtWidgets.QPushButton(self.tab)
        self.boton_inicio.setGeometry(QtCore.QRect(240, 610, 121, 31))
        self.boton_inicio.setStyleSheet("background-color: rgb(34, 111, 22);\n"
"color: rgb(255, 255, 255);")
        self.boton_inicio.setObjectName("boton_inicio")
        self.selec_10 = QtWidgets.QComboBox(self.tab)
        self.selec_10.setGeometry(QtCore.QRect(100, 530, 181, 31))
        self.selec_10.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.selec_10.setObjectName("selec_10")
        self.selec_10.addItem("")
        self.selec_10.addItem("")
        self.selec_10.addItem("")
        self.selec_10.addItem("")
        self.selec_10.addItem("")
        self.selec_10.addItem("")
        self.selec_10.addItem("")
        self.label_29 = QtWidgets.QLabel(self.tab)
        self.label_29.setGeometry(QtCore.QRect(130, 500, 101, 21))
        self.label_29.setStyleSheet("color: rgb(0, 0, 0);\n"
"\n"
"")
        self.label_29.setObjectName("label_29")
        self.boton_detener = QtWidgets.QPushButton(self.tab)
        self.boton_detener.setGeometry(QtCore.QRect(420, 610, 121, 31))
        self.boton_detener.setStyleSheet("background-color: rgb(103, 8, 8);\n"
"color: rgb(255, 255, 255);")
        self.boton_detener.setObjectName("boton_detener")
        self.selec_11 = QtWidgets.QComboBox(self.tab)
        self.selec_11.setGeometry(QtCore.QRect(420, 520, 181, 31))
        self.selec_11.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.selec_11.setObjectName("selec_11")
        self.selec_11.addItem("")
        self.selec_11.addItem("")
        self.selec_11.addItem("")
        self.selec_11.addItem("")
        self.selec_11.addItem("")
        self.label_30 = QtWidgets.QLabel(self.tab)
        self.label_30.setGeometry(QtCore.QRect(450, 490, 101, 21))
        self.label_30.setStyleSheet("color: rgb(0, 0, 0);\n"
"\n"
"")
        self.label_30.setObjectName("label_30")
        self.Pestana_principal.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.plot1 = GraphicsLayoutWidget(self.tab_2)
        self.plot1.setGeometry(QtCore.QRect(30, 50, 691, 141))
        self.plot1.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.plot1.setObjectName("plot1")
        self.plot2 = GraphicsLayoutWidget(self.tab_2)
        self.plot2.setGeometry(QtCore.QRect(30, 240, 691, 141))
        self.plot2.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.plot2.setObjectName("plot2")
        self.label_21 = QtWidgets.QLabel(self.tab_2)
        self.label_21.setGeometry(QtCore.QRect(40, 610, 141, 21))
        self.label_21.setStyleSheet("color: rgb(0, 0, 0);\n"
"\n"
"")
        self.label_21.setObjectName("label_21")
        self.barra = QtWidgets.QProgressBar(self.tab_2)
        self.barra.setGeometry(QtCore.QRect(510, 700, 111, 16))
        self.barra.setProperty("value", 24)
        self.barra.setObjectName("barra")
        self.consola_4 = QtWidgets.QTextEdit(self.tab_2)
        self.consola_4.setGeometry(QtCore.QRect(40, 640, 681, 81))
        self.consola_4.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.consola_4.setObjectName("consola_4")
        self.selec_plot1 = QtWidgets.QComboBox(self.tab_2)
        self.selec_plot1.setGeometry(QtCore.QRect(370, 10, 141, 31))
        self.selec_plot1.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.selec_plot1.setObjectName("selec_plot1")
        self.selec_plot1.addItem("")
        self.selec_plot1.addItem("")
        self.selec_plot1.addItem("")
        self.selec_plot1.addItem("")
        self.selec_plot1.addItem("")
        self.selec_plot1.addItem("")
        self.label_23 = QtWidgets.QLabel(self.tab_2)
        self.label_23.setGeometry(QtCore.QRect(160, 10, 201, 31))
        self.label_23.setObjectName("label_23")
        self.label_24 = QtWidgets.QLabel(self.tab_2)
        self.label_24.setGeometry(QtCore.QRect(160, 200, 201, 31))
        self.label_24.setObjectName("label_24")
        self.selec_plot2 = QtWidgets.QComboBox(self.tab_2)
        self.selec_plot2.setGeometry(QtCore.QRect(370, 200, 141, 31))
        self.selec_plot2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.selec_plot2.setObjectName("selec_plot2")
        self.selec_plot2.addItem("")
        self.selec_plot2.addItem("")
        self.selec_plot2.addItem("")
        self.selec_plot2.addItem("")
        self.selec_plot2.addItem("")
        self.selec_plot2.addItem("")
        self.selec_plot3 = QtWidgets.QComboBox(self.tab_2)
        self.selec_plot3.setGeometry(QtCore.QRect(370, 390, 141, 31))
        self.selec_plot3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.selec_plot3.setObjectName("selec_plot3")
        self.selec_plot3.addItem("")
        self.selec_plot3.addItem("")
        self.selec_plot3.addItem("")
        self.selec_plot3.addItem("")
        self.selec_plot3.addItem("")
        self.selec_plot3.addItem("")
        self.plot3 = GraphicsLayoutWidget(self.tab_2)
        self.plot3.setGeometry(QtCore.QRect(30, 430, 691, 141))
        self.plot3.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.plot3.setObjectName("plot3")
        self.label_25 = QtWidgets.QLabel(self.tab_2)
        self.label_25.setGeometry(QtCore.QRect(150, 390, 201, 31))
        self.label_25.setObjectName("label_25")
        self.boton_graficar = QtWidgets.QPushButton(self.tab_2)
        self.boton_graficar.setGeometry(QtCore.QRect(270, 580, 93, 28))
        self.boton_graficar.setStyleSheet("background-color: rgb(12, 85, 8);\n"
"color: rgb(255, 255, 255);")
        self.boton_graficar.setObjectName("boton_graficar")
        self.detener = QtWidgets.QPushButton(self.tab_2)
        self.detener.setGeometry(QtCore.QRect(420, 580, 93, 28))
        self.detener.setStyleSheet("background-color: rgb(204,0,0);\n"
"color: rgb(255, 255, 255);")
        self.detener.setObjectName("detener")
        self.Pestana_principal.addTab(self.tab_2, "")

        self.retranslateUi(Dialog)
        self.Pestana_principal.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.search_esp32.setText(_translate("Dialog", "Buscar ESP-32"))
        self.boton_configuracion.setText(_translate("Dialog", "Configurar"))
        self.label_7.setText(_translate("Dialog", "Acc Sampling"))
        self.label_1.setText(_translate("Dialog", "Esp32 disponibles por bluetooth"))
        self.label_9.setText(_translate("Dialog", "Acc Sensibility"))
        self.label_11.setText(_translate("Dialog", "Gyro Sensibility"))
        self.label_20.setText(_translate("Dialog", "BME688 Sampling"))
        self.label_27.setText(_translate("Dialog", "Discontinuos time"))
        self.label_8.setText(_translate("Dialog", " TCP Port"))
        self.label_10.setText(_translate("Dialog", "UDP Port"))
        self.label_12.setText(_translate("Dialog", "Host IP Addr"))
        self.label_26.setText(_translate("Dialog", "Ssid"))
        self.label_28.setText(_translate("Dialog", "Pass"))
        self.label_3.setText(_translate("Dialog", "Net Config"))
        self.label_2.setText(_translate("Dialog", "Sensor config"))
        self.label_31.setText(_translate("Dialog", "Consola"))
        self.boton_inicio.setText(_translate("Dialog", "Iniciar Monitoreo"))
        self.selec_10.setItemText(0, _translate("Dialog", "Configuración por Bluetooth "))
        self.selec_10.setItemText(1, _translate("Dialog", "Configuración vía TCP en BD "))
        self.selec_10.setItemText(2, _translate("Dialog", "Conexión TCP continua"))
        self.selec_10.setItemText(3, _translate("Dialog", "Conexión TCP discontinua"))
        self.selec_10.setItemText(4, _translate("Dialog", "Conexión UDP"))
        self.selec_10.setItemText(5, _translate("Dialog", "BLE continua "))
        self.selec_10.setItemText(6, _translate("Dialog", "BLE discontinua"))
        self.label_29.setText(_translate("Dialog", "Modo de operacion"))
        self.boton_detener.setText(_translate("Dialog", "Detener monitoreo"))
        self.selec_11.setItemText(0, _translate("Dialog", "1"))
        self.selec_11.setItemText(1, _translate("Dialog", "2"))
        self.selec_11.setItemText(2, _translate("Dialog", "3"))
        self.selec_11.setItemText(3, _translate("Dialog", "4"))
        self.selec_11.setItemText(4, _translate("Dialog", "5"))
        self.label_30.setText(_translate("Dialog", "Id protocols"))
        self.Pestana_principal.setTabText(self.Pestana_principal.indexOf(self.tab), _translate("Dialog", "Pestaña de configuracion"))
        self.label_21.setText(_translate("Dialog", "Consola"))
        self.selec_plot1.setItemText(0, _translate("Dialog", "Temperatura"))
        self.selec_plot1.setItemText(1, _translate("Dialog", "humedad"))
        self.selec_plot1.setItemText(2, _translate("Dialog", "Acc_x"))
        self.selec_plot1.setItemText(3, _translate("Dialog", "Acc_y"))
        self.selec_plot1.setItemText(4, _translate("Dialog", "Acc_z"))
        self.selec_plot1.setItemText(5, _translate("Dialog", "RMS"))
        self.label_23.setText(_translate("Dialog", "Seleccionar variable a graficar en plot 1"))
        self.label_24.setText(_translate("Dialog", "Seleccionar variable a graficar en plot 2"))
        self.selec_plot2.setItemText(0, _translate("Dialog", "Temperatura"))
        self.selec_plot2.setItemText(1, _translate("Dialog", "humedad"))
        self.selec_plot2.setItemText(2, _translate("Dialog", "Acc_x"))
        self.selec_plot2.setItemText(3, _translate("Dialog", "Acc_y"))
        self.selec_plot2.setItemText(4, _translate("Dialog", "Acc_z"))
        self.selec_plot2.setItemText(5, _translate("Dialog", "RMS"))
        self.selec_plot3.setItemText(0, _translate("Dialog", "Temperatura"))
        self.selec_plot3.setItemText(1, _translate("Dialog", "humedad"))
        self.selec_plot3.setItemText(2, _translate("Dialog", "Acc_x"))
        self.selec_plot3.setItemText(3, _translate("Dialog", "Acc_y"))
        self.selec_plot3.setItemText(4, _translate("Dialog", "Acc_z"))
        self.selec_plot3.setItemText(5, _translate("Dialog", "RMS"))
        self.label_25.setText(_translate("Dialog", "Seleccionar variable a graficar en plot 3"))
        self.boton_graficar.setText(_translate("Dialog", "Graficar"))
        self.detener.setText(_translate("Dialog", "Detener"))
        self.Pestana_principal.setTabText(self.Pestana_principal.indexOf(self.tab_2), _translate("Dialog", "Pestaña de monitoreo"))
from pyqtgraph import GraphicsLayoutWidget
