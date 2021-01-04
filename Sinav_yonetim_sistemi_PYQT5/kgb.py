# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'kurum_bilgileri_guncelleme.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Kgb_form(QtWidgets.QWidget):
    def __init__(self):
        super(Kgb_form,self).__init__()
        self.setObjectName("Form")
        self.setEnabled(True)
        self.resize(523, 357)
        self.setStyleSheet("fg:rgb(85, 255, 0)")
        self.formLayoutWidget = QtWidgets.QWidget(self)
        self.formLayoutWidget.setGeometry(QtCore.QRect(50, 30, 281, 141))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.kurumKoduLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.kurumKoduLabel.setObjectName("kurumKoduLabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.kurumKoduLabel)
        self.kurum_kodu = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.kurum_kodu.setObjectName("kurum_kodu")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.kurum_kodu)
        self.kurumIfresiLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.kurumIfresiLabel.setObjectName("kurumIfresiLabel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.kurumIfresiLabel)
        self.kurum_sifresi = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.kurum_sifresi.setObjectName("kurum_sifresi")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.kurum_sifresi)
        self.okulAdLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.okulAdLabel.setObjectName("okulAdLabel")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.okulAdLabel)
        self.kurum_adi = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.kurum_adi.setObjectName("kurum_adi")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.kurum_adi)
        self.ubeSaySLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.ubeSaySLabel.setObjectName("ubeSaySLabel")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.ubeSaySLabel)
        self.sube_sayisi = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.sube_sayisi.setObjectName("sube_sayisi")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.sube_sayisi)
        self.sNavYeriSaySLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.sNavYeriSaySLabel.setObjectName("sNavYeriSaySLabel")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.sNavYeriSaySLabel)
        self.sinav_yeri_sayisi = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.sinav_yeri_sayisi.setObjectName("sinav_yeri_sayisi")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.sinav_yeri_sayisi)
        self.kurumGuncelle = QtWidgets.QPushButton(self)
        self.kurumGuncelle.setGeometry(QtCore.QRect(370, 190, 75, 23))
        self.kurumGuncelle.setObjectName("kurumGuncelle")
        self.label = QtWidgets.QLabel(self)
        self.label.setEnabled(True)
        self.label.setGeometry(QtCore.QRect(40, 250, 321, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setStatusTip("")
        self.label.setStyleSheet("background-color: rgb(0, 255, 127);")
        self.label.setObjectName("label")

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Form", "Okul Bilgilerini Güncelle"))
        self.kurumKoduLabel.setText(_translate("Form", "Kurum Kodu"))
        self.kurumIfresiLabel.setText(_translate("Form", "Kurum Şifresi"))
        self.okulAdLabel.setText(_translate("Form", "Okul Adı"))
        self.ubeSaySLabel.setText(_translate("Form", "Şube Sayısı"))
        self.sNavYeriSaySLabel.setText(_translate("Form", "Sınav Yeri Sayısı"))
        self.kurumGuncelle.setText(_translate("Form", "Güncelle"))
        self.label.setText(_translate("Form", "Bilgileriniz güncellenmiştir"))


# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     Form = QtWidgets.QWidget()
#     ui = Ui_Form()
#     ui.setupUi(Form)
#     Form.show()
#     sys.exit(app.exec_())

