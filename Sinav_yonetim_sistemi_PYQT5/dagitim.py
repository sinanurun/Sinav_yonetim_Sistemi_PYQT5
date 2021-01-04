# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dagitimlar.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(722, 299)
        self.tableWidget = QtWidgets.QTableWidget(Form)
        self.tableWidget.setGeometry(QtCore.QRect(70, 40, 511, 192))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(6)
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
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Eski Dağıtımlar"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Dağıtım Adı"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Şube Listeleri"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Sınıf Listeleri"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Form", "Toplu Liste Excel"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Form", "Toplu Liste PDF"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

