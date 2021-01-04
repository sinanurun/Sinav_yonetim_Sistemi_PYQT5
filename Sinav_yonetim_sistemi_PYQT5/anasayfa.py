from anasayfa_ui import Ui_Anaekran
from kurum_bilgileri_guncelleme_ui import *
from kurum_bilgileri import *
from subebilgileriguncelleme import *
from fizikisinifguncelleme import *
from ydagitim import Yeni_Dagitim
import os
class Anapencere(QMainWindow,Ui_Anaekran):
    def __init__(self,parent=None):
        super(Anapencere,self).__init__(parent)
        self.baslat()

    def baslat(self):

        self.setupUi(self)
        self.EskiDagitimlar.triggered.connect(self.baslat)
        # self.show()
        self.OkulBilgileriGuncelle.triggered.connect(self.obg)
        self.SubeisimleriGuncelle.triggered.connect(self.sbg)
        # self.SubeListesi.triggered.connect(self.sl)

        # self.KapasiteGuncelle.triggered.connect(self.kg)
        self.YeniDagitim_2.triggered.connect(self.fyd)

        self.SinavyeriGuncelle.triggered.connect(self.syg)

        self.eskidagitimlar()

    def eskidagitimlar(self):
        self.tableWidget.setRowCount(0)
        self.label_2.setText(session.query(Kurum).value(Kurum.kurum_adi))
        dagitimlar = session.query(Dagitim).all()
        for dagitim in dagitimlar:
            self.tableWidget.insertRow(0)
            self.tableWidget.setItem(0,0,QTableWidgetItem(dagitim.dagitim_adi))
            self.tableWidget.setItem(0, 1, QTableWidgetItem(dagitim.dagitim_tarihi))
            sinif_listesi = QPushButton(self)
            sinif_listesi.setText("Sınıf Listesi")
            sinif_listesi.clicked.connect(lambda :os.startfile(dagitim.dsinif_listesi))
            self.tableWidget.setCellWidget(0, 2, sinif_listesi)

            fsinif_listesi = QPushButton(self)
            fsinif_listesi.setText("Salon Listesi")
            fsinif_listesi.clicked.connect(lambda :os.startfile(dagitim.dfsinif_listesi))
            self.tableWidget.setCellWidget(0, 3, fsinif_listesi)

            tsinif_listesi = QPushButton(self)
            tsinif_listesi.setText("Toplu Liste")
            tsinif_listesi.clicked.connect(lambda :os.startfile(dagitim.dtoplu_liste))
            self.tableWidget.setCellWidget(0, 4, tsinif_listesi)

            dagitim_sil = QPushButton(self)
            dagitim_sil.setText("Dağıtımı Sil")
            dagitim_sil.clicked.connect(lambda :self.fdagitim_sil(dagitim))
            self.tableWidget.setCellWidget(0, 5, dagitim_sil)


    def fdagitim_sil(self,dagitim):
        try:
            os.remove(dagitim.dsinif_listesi)
            os.remove(dagitim.dfsinif_listesi)
            os.remove(dagitim.dtoplu_liste)
            session.query(Dagitim).filter(Dagitim.dagitim_adi==dagitim.dagitim_adi).delete(synchronize_session='evaluate')
            session.commit()
            dialog = QMessageBox(self)
            islem = QLabel(dialog, text="İşlem Başarılı")
            dialog.show()
        except:
            dialog = QMessageBox(self)
            islem = QLabel(dialog, text="İşlem Başarısız")
            dialog.show()
        self.baslat()

     #okul bilgilerinin güncellenme sayfası ve işlemleri
    def obg(self):
        self.obgekrani = Kurumbg()
        self.setCentralWidget(self.obgekrani)
    def sbg(self):
        self.sbgekrani = Sube_bilgi_guncelle()
        self.setCentralWidget(self.sbgekrani)
    def sl(self):
        pass
    def syg(self):
        self.fbgekrani = Fiziki_bilgi_guncelle()
        self.setCentralWidget(self.fbgekrani)
    def kg(self):
        pass
    def fyd(self):
        self.yd = Yeni_Dagitim()
        self.setCentralWidget(self.yd)
