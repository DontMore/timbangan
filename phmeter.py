#!/usr/bin/env python3
import serial
import mysql.connector

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

def timbangan():

    ser = serial.Serial(
        port='/dev/ttyUSB1',
        baudrate = 9600,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        bytesize=serial.EIGHTBITS,
        timeout=None
    )

    buffer = ""
    data1= ""


    while True:
        x = ser.readline().decode(encoding='UTF-8',errors='replace')
        y = x.split()
        if y != ['--------------------']:
            if y == ['Name:']:
                data = data1.split()
                break
            else:
                data1 += x

    print(data)

    no = 20
    panjang = len(data)
    while no < panjang:
        if no == 21:
            sampel = str(data[13])
            batch = str(data[16])
            analis = str(data[18])
            value = str(data[21])
            satuan = str(data[22])
            print(sampel)
            print(batch)
            print(analis)
            print(value)
            print(satuan)
            sql = "INSERT INTO data_digital (sampel, batch, analis, value, satuan) VALUES (%s, %s, %s, %s, %s)"
            val = (sampel, batch, analis, value, satuan)
            mycursor.execute(sql, val)
            mydb.commit()
            print(mycursor.rowcount, "record inserted.")
        elif no > 21 and no < panjang:
            if (no-21) % 4 == 0:
               satuan = no + 1
               sampel = str(data[13])
               batch = str(data[16])
               analis = str(data[18])
               value = str(data[no])
               satuan = str(data[satuan])
               print(sampel)
               print(batch)
               print(analis)
               print(value)
               print(satuan)
               sql = "INSERT INTO data_digital (sampel, batch, analis, value, satuan) VALUES (%s, %s, %s, %s, %s)"
               val = (sampel, batch, analis, value, satuan)
               mycursor.execute(sql, val)
               mydb.commit()
               print(mycursor.rowcount, "record inserted.")
        elif no > panjang:
            no = panjang - 1
        no += 1
        
    timbangan()

timbangan()
