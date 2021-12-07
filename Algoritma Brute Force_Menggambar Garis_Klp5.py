# Menginisialisasikan kordinat (x1,y1) dan kordinat (x2,y2)
x1 = int(input('Masukan x1  : '))
y1 = int(input('Masukan y1  : '))
x2 = int(input('Masukan x2  : '))
y2 = int(input('Masukan y2  : '))
print('------------------------------------------------')

# Menghitung variabel N (banyaknya iterasi yang dilakukan apabila x1 tidak sama dengan x2 atau y1 tidak sama dengan y2)
nilaiY = y2 - y1
nilaiX = x2 - x1
N = x2 - x1 + 1

# Menjadikan x dan y sebagai titik awal
x = x1
y = y1
i = 1

# membuat kondisi dengan beberapa syarat :

# 1) Jika x1 = x2 (garis vertikal), maka :
#    a. y = y + 1 dan x tetap
#    b. gambar titik kordinat (x,y)
#    c. tampilkan grafik (selesai)

if x1 == x2:
    titikA = []
    titikB = []
    while i < y2:
        i+=1

# 2) Jika y1 = y2 (garis horizontal), maka :
#    a. x = x + 1 dan y tetap
#    b. gambar titik kordinat (x,y)
#    c. tampilkan grafik (selesai)

elif y1 == y2:
    titikA = []
    titikB = []
    while i < y2:
        i+=1

# 3) Jika 2 kondisi di atas salah, maka :
#    a. hitung kemiringan garis dengan m = (y2 - y1) / (x2 - x1) 
#    b. iterasi diulang sebanyak N
#    c. y = m ( x - x1 ) + y1
#    d. lakukan pembulatan pada y
#    e. gambar titik (x, y(pembulatan))
#    f. x = x + 1
