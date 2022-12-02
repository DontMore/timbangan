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
        port='/dev/ttyUSB0',
        baudrate = 1200,
        parity=serial.PARITY_ODD,
        stopbits=serial.STOPBITS_ONE,
        bytesize=serial.SEVENBITS,
        timeout=None
    )

    data1= ""
    data2=""
    data3=""


    while True:
        x = ser.readline().decode(encoding='UTF-8',errors='replace')
        y = x.split()
        if y != ['--------------------']:
            if y == ['Name:']:
                data = data1.split()
                break
            else:
                data1 += x
                z = data1.split()
                print(z)
                panjang_z = len(z)
                print(panjang_z)
                if panjang_z == 61:
                    if z[60] != "Start":
                        data1 = ""
                         
    print(data)
    
    if(data != "Cancel"):
        no_kontrol_alat = "3QC-MAN-001"
        sample = str(data[15])
        temperature = str(data[20])
        startWeight = str(data[66])
        finalWeight = str(data[78])
        result = str(data[73])
        measurement = str(data[81])
        print(sample)
        print(temperature)
        print(no_kontrol_alat)
        print(startWeight)
        print(finalWeight)
        print(result)
        print(measurement)
        sql = "INSERT INTO moisture (sample, temperature, no_kontrol_alat, startWeight, finalWeight, result, measurement) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        val = (sample, temperature, no_kontrol_alat, startWeight, finalWeight, result, measurement)
        mycursor.execute(sql, val)
        mydb.commit()
        print(mycursor.rowcount, "record inserted.")
        
    timbangan()

timbangan()