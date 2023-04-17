import serial.tools.list_ports
import tkinter as tk
from tkinter import ttk
import sqlite3

# Mencari semua port serial yang tersedia
available_ports = list(serial.tools.list_ports.comports())

# Membuat koneksi ke database SQLite
conn = sqlite3.connect('serial.db')
c = conn.cursor()

# Membuat tabel jika belum ada
c.execute('''CREATE TABLE IF NOT EXISTS ports
             (id INTEGER PRIMARY KEY AUTOINCREMENT, port TEXT)''')
conn.commit()

# Membuat tampilan GUI
root = tk.Tk()
root.title("Pilih Port Serial")
root.geometry("300x250")

# Membuat label untuk menampilkan hasil
result_label = tk.Label(root, text="Pilih Port Serial:")
result_label.pack(pady=10)

# Membuat daftar dropdown untuk port serial yang sedang digunakan
port_var = tk.StringVar()
port_dropdown = ttk.Combobox(root, textvariable=port_var)
port_dropdown['values'] = [port.device for port in available_ports]
port_dropdown.pack(pady=5)

# Memilih port serial yang sedang digunakan
selected_port = ""

def select_port():
    global selected_port
    selected_port = port_var.get()
    # Menyimpan port serial yang dipilih ke dalam database
    c.execute("INSERT INTO ports (port) VALUES (?)", (selected_port,))
    conn.commit()
    root.destroy()

select_button = tk.Button(root, text="Pilih", command=select_port)
select_button.pack(pady=10)

save_button = tk.Button(root, text="Save", command=root.destroy)
save_button.pack(pady=5)

root.mainloop()

# Menampilkan port serial yang dipilih
if selected_port:
    print("Port Serial yang Dipilih:", selected_port)
else:
    print("Tidak Ada Port Serial yang Dipilih")

# Menampilkan daftar port serial yang tersimpan di dalam database
c.execute("SELECT * FROM ports")
print("Daftar Port Serial yang Tersimpan:")
for row in c.fetchall():
    print(row[1])

# Menutup koneksi ke database SQLite
conn.close()

