file = open("refraktometer.txt", "r")
import mysql.connector
from datetime import datetime

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1",
    database="digitalisasi",
    allow_local_infile = "True"
)
    
if mydb.is_connected():
    print("Berhasil terhubung ke database")
    
mycursor = mydb.cursor()

x = file.readline()
y = x.split(",")

no_kontrol_alat = "3QC-RFK-001"

tanggal = str(y[0])
thn = tanggal[:2]
bln = tanggal[2:4]
tgl = tanggal[4:]
tanggal = tgl + "-" + bln + "-" + thn
tanggal = datetime.strptime(tanggal, "%d-%m-%y")
print(tanggal)

waktu = str(y[1])
jam = waktu[0:2]
menit = waktu[2:]
jam = jam + ":" + menit
print(jam)

IndexBias = str(y[2].replace("nD=",""))
print(IndexBias)

Brix = y[3].split()
Brix = str(Brix[1])
print(Brix)

sql = "INSERT INTO refractometer (no_kontrol_alat, tanggal, jam, IndexBias, Brix) VALUES (%s, %s, %s, %s, %s)"
val = (no_kontrol_alat, tanggal, jam, IndexBias, Brix)
mycursor.execute(sql, val)
mydb.commit()
print(mycursor.rowcount, "record inserted.")