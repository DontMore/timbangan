import serial
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1",
    database="data_digital",
    allow_local_infile="True"
)

if mydb.is_connected():
    print("Berhasil terhubung ke database")

mycursor = mydb.cursor()

def collectData():
    ser = serial.Serial(
        port='/dev/ttyUSB0',
        baudrate=1200,
        parity=serial.PARITY_ODD,
        stopbits=serial.STOPBITS_ONE,
        bytesize=serial.SEVENBITS,
        timeout=None
    )

    buffer = ""
    data1 = ""

    while True:
        x = ser.readline().decode(encoding='UTF-8', errors='replace')
        y = x.split()
        if y != ['--------------------']:
            if y == ['Name:']:
                data1 = data1
                break
            else:
                data1 += x

    print(data1)

    timbangan = "3QC-TMB-003"

    sql = "INSERT INTO data_timbang (timbangan, data) VALUES (%s, %s)"
    val = (timbangan, data1)
    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "record inserted.")
    
    collectData()

collectData()
