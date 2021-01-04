from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


engine = create_engine("sqlite:///kelebek_db.db")
session = sessionmaker(bind=engine)()
Base = declarative_base()

# okul işlemleri için
class OkulBilgileri(Base):
    __tablename__ = "okul_bilgileri"

    kurum_kodu = Column(Integer, primary_key= True)
    kurum_adi = Column(String)
    sifre = Column(String)
    sinif_sayisi = Column(Integer)
    fsinif_sayisi = Column(Integer)

    def __init__(self,kurum_kodu,kurum_adi,sifre,sinif_sayisi,fsinif_sayisi):
        self.kurum_kodu = kurum_kodu
        self.kurum_adi = kurum_adi
        self.sifre = sifre
        self.sinif_sayisi = sinif_sayisi
        self.fsinif_sayisi = fsinif_sayisi

okul = OkulBilgileri(1245,"scevik","12",15,15)
session.add(okul)
session.commit()