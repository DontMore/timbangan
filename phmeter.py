
file = open("phmeter.txt", "r")

no = 1
data = ""

while no < 38:
    response = file.readline()
    data += response
    no += 1

data = data.split()

print(data)
print("-------------------------------------")
print(len(data))
if len(data) == 19:
    print("nama sampel belum")
elif len(data) == 20:
    print("tanggal :")
    print(data[2])
    print("jam :")
    print(data[3])
    print("sampel :")
    print(data[7])
    print("user :")
    print(data[9])
    print("pH :")
    print(data[14])
    print("Suhu :")
    print(data[17])
elif len(data) > 20:
    lebihdata = len(data) - 20
    print("tanggal :")
    print(data[2])
    print("jam :")
    print(data[3])
    print("sampel :")
    i = 0
    datasampel1 = ""
    while i <= lebihdata:
        num = i + 5
        datasampel = data[num]
        datasampel1 += " " + datasampel
        i += 1
    print(datasampel1)
    print("user :")
    print(data[(7 + lebihdata)])
    print("pH :")
    print(data[(14 + lebihdata)])
    print("Suhu :")
    print(data[(17 + lebihdata)])

