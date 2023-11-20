import serial
from datetime import datetime, timedelta 


ser = serial.Serial(
        port='/dev/ttyUSB0',
        baudrate=1200,
        parity=serial.PARITY_ODD,
        stopbits=serial.STOPBITS_ONE,
        bytesize=serial.SEVENBITS,
        timeout=None
    )

ser2 = serial.Serial(
        port='/dev/ttyUSB1',
        baudrate=1200,
        parity=serial.PARITY_ODD,
        stopbits=serial.STOPBITS_ONE,
        bytesize=serial.SEVENBITS,
        timeout=None
    )

now = datetime.now()
formatted_now = now.strftime("%d-%m-%Y  %H:%M:%S")
print(formatted_now)
ser2.write(formatted_now.encode('utf-8'))

noTimbangan = "\nNomor Timbangan :   \n 3QC-TMB-007\n"
ser2.write(noTimbangan.encode('utf-8'))

sampel = input("Nama sampel :")
sampel = "Nama sampel :       \n" + sampel + "\n"
print(sampel)
ser2.write(sampel.encode('utf-8'))

batch = input("Nomor Batch :")
batch = "Nomor Batch :       \n" + batch + "\n"
print(batch)
ser2.write(batch.encode('utf-8'))

analis = input("Nama Analis :")
analis = "Nama Analis :       \n" + analis + "\n \n--------------------\n"
print(analis)
ser2.write(analis.encode('utf-8'))

while True:
    data = ser.readline()
    dataPrint = data.decode('utf-8') 
    print(dataPrint)
    ser2.write(dataPrint.encode('utf-8'))

ser.close()
