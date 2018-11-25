# -*- coding: utf-8 -*-
#
# Form implementation generated from reading ui file '.\Connection_Dialog.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog
import settings
import socket
import Sock_Conn


class Ui_Connection(QDialog):
    def setupUi(self, Connection):
        Connection.setObjectName("Connection")
        Connection.setFixedSize(533, 386)
        self.gridLayout = QtWidgets.QGridLayout(Connection)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_2 = QtWidgets.QLabel(Connection)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("Port")
        self.horizontalLayout_3.addWidget(self.label_2)
        spacerItem = QtWidgets.QSpacerItem(55, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.plainTextEdit_2 = QtWidgets.QPlainTextEdit(Connection)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.plainTextEdit_2.setFont(font)
        self.plainTextEdit_2.setReadOnly(False)
        self.plainTextEdit_2.setObjectName("Port_input")
        self.horizontalLayout_3.addWidget(self.plainTextEdit_2)
        self.gridLayout.addLayout(self.horizontalLayout_3, 4, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 500, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 6, 0, 1, 1)
        self.buttonBox = QtWidgets.QDialogButtonBox(Connection)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Ok | QtWidgets.QDialogButtonBox.Close)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 7, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(Connection)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("IP")
        self.horizontalLayout_2.addWidget(self.label)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.plainTextEdit = QtWidgets.QPlainTextEdit(Connection)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.plainTextEdit.setFont(font)
        self.plainTextEdit.setReadOnly(True)
        self.plainTextEdit.setObjectName("IP_input")
        self.horizontalLayout_2.addWidget(self.plainTextEdit)
        self.gridLayout.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 500, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem3, 0, 0, 1, 1)

        hostname = socket.gethostname()
        IP = socket.gethostbyname(hostname)
        self.plainTextEdit.insertPlainText(IP)
        self.plainTextEdit_2.insertPlainText('12345')

        self.retranslateUi(Connection)
        self.buttonBox.accepted.connect(lambda: self.apply(Connection))
        self.buttonBox.rejected.connect(Connection.reject)
        QtCore.QMetaObject.connectSlotsByName(Connection)

    def retranslateUi(self, Connection):
        _translate = QtCore.QCoreApplication.translate
        Connection.setWindowTitle(_translate("Connection", "Dialog"))
        self.label_2.setText(_translate("Connection", "Port"))
        self.label.setText(_translate("Connection", "IP Address"))

    def apply(self, Connection):
        settings.ip = str(self.plainTextEdit.toPlainText())
        settings.port = int(self.plainTextEdit_2.toPlainText())
        settings._pickling()
        self.myThread = Sock_Conn.Sock_Conn()
        self.myThread.closeDiag.connect(lambda: Connection.accept())
        self.myThread.start()
