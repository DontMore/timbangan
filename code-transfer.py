# Mengimpor library pyserial
import serial

# Membuat objek serial dengan parameter sesuai perangkat yang terhubung
ser = serial.Serial(
        port= '/dev/ttyUSB1',
        baudrate='1200',
        parity=serial.PARITY_ODD,
        stopbits=serial.STOPBITS_ONE,
        bytesize=serial.SEVENBITS,
        timeout=None
    )

# Membuka port serial jika belum terbuka
if not ser.is_open:
    ser.open()

# Membaca data dari port serial secara terus menerus
while True:
    # Membaca sebanyak 100 byte dari port serial
    data = ser.readline()
    dataPrint = data.decode('utf-8')
    # Jika ada data yang diterima, cetak data tersebut
    if dataPrint:
        print(dataPrint)
