'''Membuat Program Menghitung berat badan ideal di semua usia'''

def show() :
    print("\nProgram Cek Stunting")
    print("Silahkan Pilih Jenis Kelamin Anda")
    print("[1] Laki Laki")
    print("[2] Perempuan")
    print("[0] Keluar")
    
    pilih = int(input("Masukan Pilihan Anda : "))
    if pilih == 1 :
        laki()
    elif pilih == 2 :
        perempuan()
    elif pilih == 3 :
        keluar()
    else :
        print("Pilihan Tidak Tersedia")

def laki() :
    tinggi = int(input("Masukan Tinggi Badan Anda : "))
    berat  = int(input("Masukan Berat Badan Anda : "))
    ideal  = (tinggi - 100) - ((tinggi - 100) * 0.10)

    if berat < ideal+2 :
        print("Kamu Kurus, Makan Yang Banyak Ya!")
    elif berat > ideal+2 :
        print("Kamu Gemuk, Olahraga Yang Banyak Ya!")
    else :
        print("Kamu Keren!")
    print("Berat Badan Ideal Mu Adalah ",ideal)

def perempuan() :
    tinggi = int(input("Masukan Tinggi Badan Anda : "))
    berat  = int(input("Masukan Berat Badan Anda : "))
    ideal  = (tinggi - 100) - ((tinggi - 100) * 0.15)

    if berat < ideal+2 :
        print("Kamu Kurus, Makan Yang Banyak Ya!")
    elif berat > ideal+2 :
        print("Kamu Gemuk, Olahraga Yang Banyak Ya!")
    else :
        print("Kamu Keren!")
    print("Berat Badan Ideal Mu Adalah ",ideal)

def keluar() :
    print("Terimakasi Telah Menggunakan Program Ini ")

def lagi() :
    return show

show()