file = open("refractometer.txt", "r")

x = file.readline()
y = x.split(",")

Tanggal = y[0]
print(Tanggal)

Jam = y[1]
print(Jam)

IndexBias = y[2].replace("nD=","")
print(IndexBias)

Brix = y[3].split()
Brix = Brix[1]
print(Brix)
