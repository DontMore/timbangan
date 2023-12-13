# Mengimpor library pyserial
import serial

# Membuat objek serial dengan parameter sesuai perangkat yang terhubung
ser = serial.Serial(
    port='COM8', # Ganti dengan nomor port yang sesuai
    baudrate=9600, # Ganti dengan kecepatan baud yang sesuai
    timeout=1 # Ganti dengan waktu tunggu yang sesuai
)

# Membuka port serial jika belum terbuka
if not ser.is_open:
    ser.open()

# Membaca data dari port serial secara terus menerus
while True:
    # Membaca sebanyak 100 byte dari port serial
    data = ser.read(100)
    # Jika ada data yang diterima, cetak data tersebut
    if data:
        print(data)
