from PyQt5.QtWidgets import *
from ui_giris import Ui_giris_ekrani

class GirisPenceresi(QMainWindow,Ui_giris_ekrani):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
    def kontrol(self):
        self.hatali_giris.setVisible(1)
        return 1