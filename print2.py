import serial
from datetime import datetime
import tkinter as tk
from tkinter import ttk
import serial.tools.list_ports

def update_ports():
    ports = [p.device for p in serial.tools.list_ports.comports()]
    scale_port_combobox['values'] = ports
    printer_port_combobox['values'] = ports

def submit_form():
    scale_port = scale_port_combobox.get()
    scale_baudrate = scale_baudrate_combobox.get()

    printer_port = printer_port_combobox.get()
    printer_baudrate = printer_baudrate_combobox.get()

    ser = serial.Serial(
        port=scale_port,
        baudrate=scale_baudrate,
        parity=serial.PARITY_ODD,
        stopbits=serial.STOPBITS_ONE,
        bytesize=serial.SEVENBITS,
        timeout=None
    )

    ser2 = serial.Serial(
        port=printer_port,
        baudrate=printer_baudrate,
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

    sampel = sampel_entry.get()
    sampel = "Nama sampel :       \n" + sampel + "\n"
    print(sampel)
    ser2.write(sampel.encode('utf-8'))

    noQC = noQC_entry.get()
    noQC = "Nomor QC :       \n" + noQC + "\n"
    print(noQC)
    ser2.write(noQC.encode('utf-8'))

    batch = batch_entry.get()
    batch = "Nomor Batch :       \n" + batch + "\n"
    print(batch)
    ser2.write(batch.encode('utf-8'))

    analis = analis_entry.get()
    analis = "Nama Analis :       \n" + analis + "\n \n--------------------\n"
    print(analis)
    ser2.write(analis.encode('utf-8'))

    # Display submitted data in the text box
    submitted_data_text.insert(tk.END, formatted_now + "\n" + noTimbangan + sampel + noQC + batch + analis)

# Serial setup
ser2 = serial.Serial(
    port='/dev/ttyUSB1',
    baudrate=1200,
    parity=serial.PARITY_ODD,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.SEVENBITS,
    timeout=None
)

# GUI setup
root = tk.Tk()
root.title("Measurement Form")

frame = ttk.Frame(root, padding="10")
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

# Scale Settings
scale_label = ttk.Label(frame, text="Scale Settings")
scale_label.grid(row=0, column=0, columnspan=2, pady=(0, 10))

scale_port_label = ttk.Label(frame, text="Port:")
scale_port_label.grid(row=1, column=0, sticky=tk.E)

scale_port_combobox = ttk.Combobox(frame, state="readonly")
scale_port_combobox.grid(row=1, column=1, pady=(0, 10))

scale_baudrate_label = ttk.Label(frame, text="Baudrate:")
scale_baudrate_label.grid(row=2, column=0, sticky=tk.E)

scale_baudrate_combobox = ttk.Combobox(frame, values=["1200", "2400", "4800"], state="readonly")
scale_baudrate_combobox.grid(row=2, column=1, pady=(0, 10))

# Printer Settings
printer_label = ttk.Label(frame, text="Printer Settings")
printer_label.grid(row=3, column=0, columnspan=2, pady=(10, 10))

printer_port_label = ttk.Label(frame, text="Port:")
printer_port_label.grid(row=4, column=0, sticky=tk.E)

printer_port_combobox = ttk.Combobox(frame, state="readonly")
printer_port_combobox.grid(row=4, column=1, pady=(0, 10))

printer_baudrate_label = ttk.Label(frame, text="Baudrate:")
printer_baudrate_label.grid(row=5, column=0, sticky=tk.E)

printer_baudrate_combobox = ttk.Combobox(frame, values=["1200", "2400", "4800"], state="readonly")
printer_baudrate_combobox.grid(row=5, column=1, pady=(0, 10))

# Update ports button
update_ports_button = ttk.Button(frame, text="Update Ports", command=update_ports)
update_ports_button.grid(row=6, column=0, columnspan=2, pady=(10, 0))

# Measurement Form
sampel_label = ttk.Label(frame, text="Nama Sampel:")
sampel_label.grid(row=7, column=0, sticky=tk.E, pady=(10, 10))

sampel_entry = ttk.Entry(frame)
sampel_entry.grid(row=7, column=1, pady=(10, 10))

noQC_label = ttk.Label(frame, text="Nomor QC:")
noQC_label.grid(row=8, column=0, sticky=tk.E, pady=(0, 10))

noQC_entry = ttk.Entry(frame)
noQC_entry.grid(row=8, column=1, pady=(0, 10))

batch_label = ttk.Label(frame, text="Nomor Batch:")
batch_label.grid(row=9, column=0, sticky=tk.E, pady=(0, 10))

batch_entry = ttk.Entry(frame)
batch_entry.grid(row=9, column=1, pady=(0, 10))

analis_label = ttk.Label(frame, text="Nama Analis:")
analis_label.grid(row=10, column=0, sticky=tk.E, pady=(0, 10))

analis_entry = ttk.Entry(frame)
analis_entry.grid(row=10, column=1, pady=(0, 10))

# Submit button
submit_button = ttk.Button(frame, text="Submit", command=submit_form)
submit_button.grid(row=11, column=0, columnspan=2, pady=(10, 0))

# Label to display submitted data
submitted_data_label = ttk.Label(frame, text="Submitted Data:")
submitted_data_label.grid(row=12, column=0, columnspan=2, pady=(10, 0))

# Text widget to display submitted data
submitted_data_text = tk.Text(frame, height=10, width=40)
submitted_data_text.grid(row=13, column=0, columnspan=2, pady=(10, 0))

root.mainloop()

