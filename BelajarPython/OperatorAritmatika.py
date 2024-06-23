# Operasi matematika yg berkaitan dengan data float, hasilnya akan float
# tipe data variabel bil8 adalah float maka tidak bisa dijumlah karena tipe data float tidak bisa untuk operasi aritmatika
#bil7 = 12
#bil8 = "5"
#jumlahNilai = bil7 + bil8 
#print (jumlahNilai)
#print (type(jumlahNilai))


#PENJUMLAHAN
bil1 = 7
bil2 = 3
hasil = bil1 + bil2
print(hasil)
print(type(hasil))

bil3 = 5.5
bil4 = 1
jumlah = bil3 + bil4
print(jumlah)
print(type(jumlah))

bil5 = "1"
bil6 = "7"
nilaiString = bil5 + bil6
print(nilaiString)
print(type(nilaiString))

bil7 = 12
bil8 = "5"
jumlahNilai = bil7 + int(bil8)
print (jumlahNilai)
print (type(jumlahNilai))

bilC = "Fantyka"
bilD = "Bintang"
bilE = "Karisma"
gabung = bilC + " " + bilD + " " + bilE
print(gabung)
print(type(gabung))

#PENGURANGAN
bilA = 10
bilB = 5
kurang = bilA - bilB
print(kurang)
print(type(kurang))


#PERKALIAN
#tipe data string hanya bisa dikalikan dengan tipe data integer 
#tipe data string tidak bisa dikalikan dengan sesama tipe data string dan juga tipe data float
#bilH = 5.1
#bilJ = "3"
#nilaiPerkalian = bilH * bilJ
#print(nilaiPerkalian)
#print(type(nilaiPerkalian))

bilF = 5
bilG = 2
jmlPerkalian = bilF * bilG
print(jmlPerkalian)
print(type(jmlPerkalian))

bilH = 5
bilJ = "3"
nilaiPerkalian = bilH * bilJ
print(nilaiPerkalian)
print(type(nilaiPerkalian))

#PEMBAGIAN 
# nilainya akan selalu menjadi float
# jadi untuk pembagian jika tipe data-nya float ataupun integer akan menghasilkan nilai float
bilK = 10
bilL = 2
pembagian = bilK / bilL
print(pembagian)
print(type(pembagian))

bilM =10.0
bilN = 5.0
pembagianPecahan = bilM / bilN
print(pembagianPecahan)
print(type(pembagianPecahan))

# (%) modula adalah sisa hasil bagi 
bilZ = 5
bilQ = 2
nilaiModula = bilZ % bilQ
print(nilaiModula)
print(type(nilaiModula))

# (//) floor Division adalah hasil pembagian tetapi yg diambil angka bulat
bilZ = 5
bilQ = 2
nilaiModula = bilZ // bilQ
print(nilaiModula)
print(type(nilaiModula))

bilZ = 5.0
bilQ = 2.0
nilaiModula = bilZ // bilQ
print(nilaiModula)
print(type(nilaiModula))

# (**) eksponensial adalah pangkat 
bilI = 5
bilU = 2
nilaiModula = bilI ** bilU
print(nilaiModula)
print(type(nilaiModula))