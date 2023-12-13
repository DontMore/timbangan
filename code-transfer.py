# Mengimpor library Tkinter
import tkinter as tk

# Membuat objek window sebagai root window
window = tk.Tk()

# Memberi judul window
window.title("Serial Communication")

# Membuat frame untuk menampung widget
frame = tk.Frame(window)

# Membuat label untuk menampilkan data dari port serial
label = tk.Label(frame, text="Data from serial port:")

# Membuat text widget untuk menampilkan data dari port serial
text = tk.Text(frame, height=10, width=40)

# Membuat scrollbar untuk text widget
scrollbar = tk.Scrollbar(frame, command=text.yview)

# Menghubungkan scrollbar dengan text widget
text.config(yscrollcommand=scrollbar.set)

# Menempatkan widget pada frame dengan grid layout manager
label.grid(row=0, column=0, sticky="w")
text.grid(row=1, column=0, sticky="nsew")
scrollbar.grid(row=1, column=1, sticky="ns")

# Menyesuaikan ukuran frame sesuai dengan ukuran window
frame.pack(fill=tk.BOTH, expand=True)

# Membuat fungsi untuk membaca data dari port serial dan menampilkannya pada text widget
def read_serial():
    # Menggunakan kode yang Anda berikan untuk membaca data dari port serial
    data = ser.readline()
    dataPrint = data.decode('utf-8')
    # Jika ada data yang diterima, tambahkan data tersebut ke text widget
    if dataPrint:
        text.insert(tk.END, dataPrint)
        # Scroll text widget ke bawah agar data terbaru terlihat
        text.see(tk.END)
    # Memanggil fungsi ini lagi setelah 100 milidetik
    window.after(100, read_serial)

# Memanggil fungsi read_serial untuk pertama kali
read_serial()

# Menjalankan main loop dari window
window.mainloop()
