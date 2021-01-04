"""
bu bölümde orm yapısı kullanılarak db iş ve işlemleri gerçekleştirilmektedir.
tablo tanımları vb işlmler

"""
# from sqlalchemy import Column, ForeignKey, Integer, String # yerine * da olabilirdi
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import *  #tablolar arası ilişki kurmak için
from sqlalchemy import *

Base = declarative_base()

# okul işlemleri için db orm yapısı
class Kurum(Base):
    #tablo adı
    __tablename__ = 'okul_bilgileri'
    #tablo sutunları ve özellikleri varsa da ilişkileri
    kurum_kodu = Column(Integer, unique= True, primary_key=True)
    kurum_adi = Column(String(250), nullable=False)
    kurum_sifre = Column(String(250), nullable=False)
    sube_sayisi = Column(Integer,nullable=False)
    fsinif_sayisi = Column(Integer,nullable=False)


class SubeBilgileri(Base):
    __tablename__ = 'sube_bilgileri'

    sube_id = Column(Integer,unique=True, primary_key=True, autoincrement= True)
    sube_adi = Column(String(250), unique=True)
    sube_mevcut = Column(Integer)
    sube_ogrenci = Column(String)

class FizikiSinif(Base):
    __tablename__ = 'fiziki_sinif'

    fsinif_id = Column(Integer,unique=True, primary_key=True, autoincrement= True)
    fsinif_adi = Column(String(250),unique=True)
    fsinif__mevcut = Column(Integer)

class OgrenciListeleri(Base):
    __tablename__ = 'ogrenci_listeleri'

    ogrenci_id = Column(Integer,unique=True, primary_key=True, autoincrement= True)
    ogrenci_no = Column(Integer,unique=True)
    ogrenci_adi = Column(String(100))
    sube_id = Column(Integer,ForeignKey('sube_bilgileri.sube_id')) #referans alınacak tablo birebir yazılmalı
    sube_bilgileri = relationship(SubeBilgileri, backref ='ogrenci_listeleri')

class Dagitim(Base):
    __tablename__ = 'dagitim_listeleri'

    dagitim_id = Column(Integer,unique=True, primary_key=True, autoincrement= True)
    dagitim_adi = Column(String(100))
    dagitim_tarihi = Column(String(100))
    dsinif_listesi = Column(String(100))
    dfsinif_listesi = Column(String(100))
    dtoplu_liste = Column(String(100))

# sqlite olarak kayıtedilecek dosyayı gösteriyoruz
engine = create_engine('sqlite:///kelebek.db')

# Tanımladığımız Base üzerindeki tabloları oluşturuyoruz
Base.metadata.create_all(engine)