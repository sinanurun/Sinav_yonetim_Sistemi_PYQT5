# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'subebilgileriguncelleme.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from openpyxl import load_workbook, Workbook
from random import *

import sys
from db_islemleri import * #db işlemleri sayfasını aldık


class Fiziki_bilgi_guncelle(QtWidgets.QWidget):
    def __init__(self):
        super(Fiziki_bilgi_guncelle,self).__init__()

        self.setObjectName("Form")
        self.resize(623, 355)

        self.query = session.query(FizikiSinif)

        self.tablo = QtWidgets.QTableWidget(self)
        self.tablo.setGeometry(QtCore.QRect(20,30,600,250))
        self.tablo.setRowCount(self.query.count())
        self.tablo.setColumnCount(2)
        self.tablo.setHorizontalHeaderLabels(["Fiziki Sınıf Adı","Fiziki Sınıf Mevcutları"])
        self.tablo.setColumnWidth(0, 100)
        self.tablo.setColumnWidth(1, 100)

        for dd in range(self.query.count()):
            icerik = self.query.filter(FizikiSinif.fsinif_id == dd + 1).first()
            self.tablo.setItem(dd,0,QtWidgets.QTableWidgetItem(icerik.fsinif_adi))
            self.tablo.setItem(dd, 1, QtWidgets.QTableWidgetItem(str(icerik.fsinif__mevcut)))

        self.guncelle = QtWidgets.QPushButton(self)
        self.guncelle.setGeometry(QtCore.QRect(530, 320, 75, 23))
        self.guncelle.setObjectName("guncelle")
        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)
        self.guncelle.clicked.connect(self.guncellefonk)
    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Form", "Fiziki bilgileri Güncelleme"))
        self.guncelle.setText(_translate("Form", "Güncelle"))



    def guncellefonk(self):

        session.query(FizikiSinif).delete(synchronize_session='evaluate')
        session.commit()


        for satir in range(self.tablo.rowCount()):
            if self.tablo.item(satir,1).text() != 'None':

                ogren = FizikiSinif(fsinif_adi=self.tablo.item(satir,0).text(),fsinif__mevcut=int(self.tablo.item(satir,1).text()))
            else:
                ogren = FizikiSinif(fsinif_adi=self.tablo.item(satir, 0).text(),
                                    fsinif__mevcut=0)
            session.add(ogren)
            session.commit()
        return self.__init__()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Fiziki_bilgi_guncelle()
    ui.show()
    sys.exit(app.exec_())

