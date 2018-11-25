from PyQt5.QtCore import QThread, pyqtSignal
import settings
import socket
import Hotkey_Press


class Sock_Conn(QThread):
    closeDiag = pyqtSignal()

    def __init__(self):
        QThread.__init__(self)

    def __del__(self):
        self.wait()

    def run(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind((settings.ip, settings.port))
        s.listen(5)
        while settings.conn_stat:
            c, addr = s.accept()
            code_encoded = c.recv(1024)
            code_decoded = code_encoded.decode('utf-8')
            if (code_decoded == "Conn"):
                settings.socket_flag = 1
                self.closeDiag.emit()
            else:
                Hotkey_Press.Hotkey(code_decoded)
            c.close()
        s.close()
