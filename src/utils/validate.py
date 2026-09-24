def validasi_nama ():
    nama = input("Masukkan nama Anda: ")
    if len(nama) < 3:
        print("Nama harus memiliki setidaknya 3 karakter.")
        return False
    elif not nama.isalpha():
        print("Nama hanya boleh mengandung huruf.")
        return False
    else:
        print("Nama valid.")
        return True