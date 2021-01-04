# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'giris_ekrani.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_giris_ekrani(object):
    def setupUi(self, giris_ekrani):
        giris_ekrani.setObjectName("giris_ekrani")
        giris_ekrani.resize(424, 310)
        self.label = QtWidgets.QLabel(giris_ekrani)
        self.label.setGeometry(QtCore.QRect(70, 70, 61, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(giris_ekrani)
        self.label_2.setGeometry(QtCore.QRect(70, 120, 47, 13))
        self.label_2.setObjectName("label_2")
        self.k_adi = QtWidgets.QLineEdit(giris_ekrani)
        self.k_adi.setGeometry(QtCore.QRect(150, 70, 113, 20))
        self.k_adi.setObjectName("k_adi")
        self.sifre = QtWidgets.QLineEdit(giris_ekrani)
        self.sifre.setGeometry(QtCore.QRect(150, 120, 113, 20))
        self.sifre.setEchoMode(QtWidgets.QLineEdit.Password)
        self.sifre.setObjectName("sifre")
        self.g_butonu = QtWidgets.QPushButton(giris_ekrani)
        self.g_butonu.setGeometry(QtCore.QRect(160, 160, 75, 23))
        self.g_butonu.setObjectName("g_butonu")
        self.hatali_giris = QtWidgets.QLabel(giris_ekrani)
        self.hatali_giris.setGeometry(QtCore.QRect(76, 200, 251, 51))
        self.hatali_giris.setObjectName("hatali_giris")
        self.hatali_giris.setVisible(0)

        self.retranslateUi(giris_ekrani)
        # self.g_butonu.clicked.connect(self.giris_kontrol)
        QtCore.QMetaObject.connectSlotsByName(giris_ekrani)
    #
    # def giris_kontrol(self):
    #     pass

    def retranslateUi(self, giris_ekrani):
        _translate = QtCore.QCoreApplication.translate
        giris_ekrani.setWindowTitle(_translate("giris_ekrani", "Giriş Ekranı"))
        self.label.setText(_translate("giris_ekrani", "Kullanıcı Adı"))
        self.label_2.setText(_translate("giris_ekrani", "Şifre"))
        self.g_butonu.setText(_translate("giris_ekrani", "Giriş"))
        self.hatali_giris.setText(_translate("giris_ekrani", "Giriş Hatalı Tekrar Deneyiniz"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    giris_ekrani = QtWidgets.QWidget()
    ui = Ui_giris_ekrani()
    ui.setupUi(giris_ekrani)
    giris_ekrani.show()
    sys.exit(app.exec_())

