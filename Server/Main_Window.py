# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\vinay\Desktop\untitled.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtWidgets
import sys
import settings
from Connection_Dialog import Ui_Connection
from Bindings import Ui_Binding


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(300, 210, 181, 81))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(lambda: self.Connect_dialog(MainWindow))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        self.menuConnection = QtWidgets.QMenu(self.menubar)
        self.menuConnection.setObjectName("menuConnection")
        self.menuOptions = QtWidgets.QMenu(self.menubar)
        self.menuOptions.setObjectName("menuOptions")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        self.statusbar.showMessage('Not Connected')
        MainWindow.setStatusBar(self.statusbar)
        self.actionConnect = QtWidgets.QAction(MainWindow)
        self.actionConnect.setObjectName("actionConnect")
        self.actionConnect.triggered.connect(lambda: self.Connect_dialog(MainWindow))
        self.actionDisconnect = QtWidgets.QAction(MainWindow)
        self.actionDisconnect.setEnabled(False)
        self.actionDisconnect.setObjectName("actionDisconnect")
        self.actionDisconnect.triggered.connect(lambda: self.Disconnect(MainWindow))
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionBinding = QtWidgets.QAction(MainWindow)
        self.actionBinding.setObjectName("actionBinding")
        self.actionBinding.triggered.connect(lambda: self.Binding_dialog(MainWindow))
        self.actionPort = QtWidgets.QAction(MainWindow)
        self.actionPort.setObjectName("actionPort")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionREADME = QtWidgets.QAction(MainWindow)
        self.actionREADME.setObjectName("actionREADME")
        self.menuConnection.addAction(self.actionConnect)
        self.menuConnection.addAction(self.actionDisconnect)
        self.menuConnection.addSeparator()
        self.menuConnection.addAction(self.actionExit)
        self.menuOptions.addAction(self.actionBinding)
        # self.menuOptions.addAction(self.actionPort)
        self.menuHelp.addAction(self.actionAbout)
        self.menuHelp.addAction(self.actionREADME)
        self.menubar.addAction(self.menuConnection.menuAction())
        self.menubar.addAction(self.menuOptions.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        settings._unpickling()

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Droid Stream Deck"))
        self.pushButton.setText(_translate("MainWindow", "Connect"))
        self.menuConnection.setTitle(_translate("MainWindow", "Connection"))
        self.menuOptions.setTitle(_translate("MainWindow", "Options"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionConnect.setText(_translate("MainWindow", "Connect"))
        self.actionConnect.setShortcut(_translate("MainWindow", "Ctrl+C"))
        self.actionDisconnect.setText(_translate("MainWindow", "Disconnect"))
        self.actionDisconnect.setShortcut(_translate("MainWindow", "Ctrl+D"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionExit.setShortcut(_translate("MainWindow", "Ctrl+W"))
        self.actionBinding.setText(_translate("MainWindow", "Binding"))
        self.actionBinding.setShortcut(_translate("MainWindow", "Ctrl+B"))
        # self.actionPort.setText(_translate("MainWindow", "Port"))
        # self.actionPort.setShortcut(_translate("MainWindow", "Ctrl+P"))
        self.actionAbout.setText(_translate("MainWindow", "About"))
        self.actionREADME.setText(_translate("MainWindow", "README"))

    def Connect_dialog(self, MainWindow):
        settings._unpickling()
        dialog = QtWidgets.QDialog()
        dialog.ui = Ui_Connection()
        dialog.ui.setupUi(dialog)
        dialog.exec_()
        settings._pickling()
        if(settings.socket_flag == 1):
            self.statusbar.showMessage('Connected')
            self.actionDisconnect.setEnabled(True)
            self.actionConnect.setEnabled(False)

    def Binding_dialog(self, MainWindow):
        settings._unpickling()
        dialog = QtWidgets.QDialog()
        dialog.ui = Ui_Binding()
        dialog.ui.setupUi(dialog)
        dialog.exec_()
        settings._pickling()

    def Disconnect(self, MainWindow):
        settings.conn_stat = False
        self.statusbar.showMessage('Not Connected')
        self.actionDisconnect.setEnabled(False)
        self.actionConnect.setEnabled(True)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
