#Dictionary

pins = {"Anu":1234, "Grah":1111, "Iman":2222}
print(pins["Anu"])
print(type(pins["Grah"]))
print(pins.keys())
print(pins.values())
pins["Nugi"]= 5555
pins.pop("Grah")
pins["elok"] = "AB123"
print(pins)

#Input

masuk = input("Masukkan nama : ")
bilangan = int(input("Masukkan angka : "))
print(bilangan)
print(masuk)
print(bilangan**2)
bilanganpecahan = float(input("Masukkan bilangan : "))
hasil = bilanganpecahan/2
print(hasil)

#Condition

if 1<5:
    print("yes")
else:
    print("no")

if 1 == 5:
    print("yes")
else:
    print("no")

#Multiple Condition

user_input = float(input("Masukkan angka : "))
if user_input > 100:
    print("Mantul")
elif user_input == 70:
    print("Pas")
else:
    print("Kasian deh lu")

# Function

def printing():
    print("Hai")
    print("Bambang")

printing()

def luas_persegi(sisi):
    luas = sisi * sisi
    return luas

print(luas_persegi(6))

#print_return.py

def returning():
    return 10

def printing():
    print(100)

print(returning()+20)
printing()+20

def luas_segitiga(alas, tinggi):
    luas = (alas*tinggi)/2
    print("Luas Segitiga : %d" %luas)
luas_segitiga(4,5)

def hitung_umur(tahun):
    umur = 2019 - tahun
    print("Umur anda : %d" %umur)
hitung_umur(2000)