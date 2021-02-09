#sqlite import etmek
#tablo ve database olusturma
import sqlite3
con = sqlite3.connect("dersler.db")
cursor=con.cursor()

def tabloolustur():
    cursor.execute("CREATE TABLE ogrenciler(ad TEXT,soyad TEXT,numara INT,ogrencino INT)")
def degerekle():
    cursor.execute("INSERT INTO ogrenciler VALUES('Emin','Dagdelen','123','1234')")
    con.commit()
    con.close()

tabloolustur()
degerekle()
def degerlerial():
    cursor.execute("SELECT ad,FROM ogrenciler")
    con.commit()
    con.close()
degerlerial()
