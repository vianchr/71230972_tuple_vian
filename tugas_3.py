def cek_email():
    nama_file = input("Masukkan nama file: ")
    # Membuka file
    try:
        file = open(nama_file)
    except:
        print("File tidak ditemukan.")
        cek_email()

    # Membuat kamus untuk menghitung distribusi jam
    jam_email = dict()
    for line in file:
        if line.startswith("From "):
            words = line.split()
            jam = words[5].split(":")[0]
            jam_email[jam] = jam_email.get(jam, 0) + 1

    # Menampilkan hasil
    for jam, jumlah in sorted(jam_email.items()):
       print(f"{jam} {jumlah}")
       
cek_email()