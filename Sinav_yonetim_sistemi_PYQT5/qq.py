# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qq.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(623, 355)
        self.formLayoutWidget = QtWidgets.QWidget(Form)
        self.formLayoutWidget.setGeometry(QtCore.QRect(0, 10, 173, 231))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.subeadie1 = QtWidgets.QLabel(self.formLayoutWidget)
        self.subeadie1.setObjectName("subeadie1")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.subeadie1)
        self.subeadi1 = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.subeadi1.setObjectName("subeadi1")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.subeadi1)
        self.sdfLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.sdfLabel.setObjectName("sdfLabel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.sdfLabel)
        self.sdfLineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.sdfLineEdit.setObjectName("sdfLineEdit")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.sdfLineEdit)
        self.guncelle = QtWidgets.QPushButton(Form)
        self.guncelle.setGeometry(QtCore.QRect(530, 320, 75, 23))
        self.guncelle.setObjectName("guncelle")
        self.renciListesiEkLabel = QtWidgets.QLabel(Form)
        self.renciListesiEkLabel.setGeometry(QtCore.QRect(400, 280, 90, 22))
        self.renciListesiEkLabel.setObjectName("renciListesiEkLabel")
        self.listeal = QtWidgets.QPushButton(Form)
        self.listeal.setGeometry(QtCore.QRect(500, 280, 110, 23))
        self.listeal.setObjectName("listeal")
        self.formLayoutWidget_2 = QtWidgets.QWidget(Form)
        self.formLayoutWidget_2.setGeometry(QtCore.QRect(180, 90, 431, 141))
        self.formLayoutWidget_2.setObjectName("formLayoutWidget_2")
        self.formLayout_2 = QtWidgets.QFormLayout(self.formLayoutWidget_2)
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.formLayout_2.setObjectName("formLayout_2")
        self.tableWidget = QtWidgets.QTableWidget(self.formLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.tableWidget)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Şube bilgileri Güncelleme"))
        self.subeadie1.setText(_translate("Form", "Şube Adı Giriniz"))
        self.sdfLabel.setText(_translate("Form", "sdf"))
        self.guncelle.setText(_translate("Form", "Güncelle"))
        self.renciListesiEkLabel.setText(_translate("Form", "Öğrenci Listesi Çek"))
        self.listeal.setText(_translate("Form", "Listeyi Al"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "New Column"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "New Column"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Form", "New Column"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Form", "New Column"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Form", "New Column"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

