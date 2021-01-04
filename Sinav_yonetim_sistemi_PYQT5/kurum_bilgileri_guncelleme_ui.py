from PyQt5.QtWidgets import *
from PyQt5.uic import *
import sys
from db_islemleri import * #db işlemleri sayfasını aldık
from kgb import *

class Kurumbg(Kgb_form):
    def __init__(self):
        super(Kurumbg,self).__init__()
        self.label.setVisible(0)
        self.kurumGuncelle.clicked.connect(self.guncelle)
        self.bilgileri_getir()

    def bilgileri_getir(self):
        self.kgirisi = kurumbilgileri()

        self.kurum_kodu.setText(str(self.kgirisi.kurum_kodu))
        self.kurum_sifresi.setText(str(self.kgirisi.kurum_sifre))
        self.kurum_adi.setText(str(self.kgirisi.kurum_adi))
        self.sube_sayisi.setText(str(self.kgirisi.sube_sayisi))
        self.sinav_yeri_sayisi.setText(str(self.kgirisi.fsinif_sayisi))
        self.eskikod = str(self.kgirisi.kurum_kodu)


    def guncelle(self):
        keys = self.kgirisi.__table__.columns.keys()
        values = [int(self.kurum_kodu.text()),
             self.kurum_adi.text(),
             self.kurum_sifresi.text(),
             int(self.sube_sayisi.text()),
             int(self.sinav_yeri_sayisi.text())]
        d = dict(zip(keys,values))
        d["eski"]=self.eskikod
        kgb_guncelle(**d)

        # kgb_guncelle(self.kurum_kodu.text(),
        #             self.kurum_sifresi.text(),
        #             self.kurum_adi.text(),
        #             self.sube_sayisi.text(),
        #             self.sinav_yeri_sayisi.text())

        # print(self.ekran.kurum_kodu.)

        self.label.setVisible(1)
        return self.bilgileri_getir()



# app = QApplication(sys.argv)
# giris = Kurumbg()
# giris.show()
# sys.exit(app.exec_())