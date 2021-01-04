import sys
from PyQt5.QtWidgets import QApplication,QWidget
from giris import GirisPenceresi
from anasayfa import Anapencere
from db_islemleri import * #db işlemleri sayfasını aldık


# giriş kontrolü yapılıp ana ekrana geçişi sağlayan fonskiyon kontrol fonksiyonu
def kontrol():
    kkodu = giris.k_adi.text()
    ksifre = giris.sifre.text()
    onay = kurum_girisi(kkodu,ksifre)
    if onay == True:
        giris.destroy()
        global anapencere
        anapencere = Anapencere()
        anapencere.show()
        # return print("giriş yapıldı")
    else:
        giris.hatali_giris.setVisible(1)
         # giriş penceresi kapatılıyor
     # ana ekran penceresine yöneldirme yapılıyor

# giriş ile ilgili iş ve işlemler





app = QApplication(sys.argv)
giris = GirisPenceresi()
a = giris.g_butonu.clicked.connect(kontrol)
giris.show()
sys.exit(app.exec_())



if __name__ == "__main__":
    girisui()