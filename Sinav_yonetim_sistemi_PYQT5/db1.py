import sqlalchemy as db #kütüphane dahil etme işlemi

engine = db.create_engine("sqlite:///kelebekcik.sqlite")
# connection = engine.connect()
# # bilgi = db.MetaData()
# # kelebekcik = db.Table("okul_bilgileri",bilgi,autoload=True, autoload_with=engine)
# # # print(kelebekcik.columns.keys())
# # # print(repr(bilgi.tables['okul_bilgileri']))
# # sorgu = db.select([kelebekcik])
# #
# # ResultProxy = connection.execute(sorgu)
# # ResultSet = ResultProxy.fetchall()
# # print(ResultSet[0])