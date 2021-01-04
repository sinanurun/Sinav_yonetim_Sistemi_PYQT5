from orm_db import *


Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()


def kurum_girisi(kkodu,sifre):
    # print(kkodu,sifre)
    kgirisi = session.query(Kurum).filter(Kurum.kurum_kodu == kkodu, Kurum.kurum_sifre == sifre).first()
    try:
        if (kgirisi.kurum_adi) :
            # print(kgirisi.kurum_adi)
            return True
    except:
        return False
    # if (kadi == kurum.kurum_kodu and kurum.kurum_sifre == sifre):
    #     print("doğru")
    # else:
    #     print("hatalı")

        #print(["{} öğretmeni {} Hoca".format(ders.isim+str(ders.ogretmen.yas), ogretmen.isim) for ogretmen in ogretmenler for ders in ogretmen.ders])

def kurumbilgileri():
    return session.query(Kurum).first()


def kgb_guncelle(**bilgiler):
    eski = bilgiler["eski"]
    del bilgiler["eski"]
    try:
        session.query(Kurum).filter(Kurum.kurum_kodu==eski).update(bilgiler, synchronize_session=False)
        session.commit()
        session.query(SubeBilgileri).delete(synchronize_session='evaluate')
        session.commit()
        session.query(FizikiSinif).delete(synchronize_session='evaluate')
        session.commit()
        subeler=[]
        for dd in range (bilgiler["sube_sayisi"]):
            sube = SubeBilgileri(sube_adi="şube adı "+str(dd+1))
            subeler.append(sube)
        session.add_all(subeler)
        session.commit()
        fsiniflar=[]
        for dd in range (bilgiler["fsinif_sayisi"]):
            fsinif = FizikiSinif(fsinif_adi="fiziki sınıf "+str(dd+1))
            fsiniflar.append(fsinif)
        session.add_all(fsiniflar)
        session.commit()
    except:
        print("hata")

