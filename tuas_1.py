# Buatlah program untuk melakukan pengecekan apakah semua anggota yang ada didalam tuple sama
def cek_isi_tuple (tuple):
    jum=len(tuple)
    tes=True
    if jum==1:
        print("True, karena hanya ada satu data dalam tuple")
    else:
        for i in range (1,jum):
            if tuple[0]==tuple[i]:
                tes=True
            else:
                tes=False
                return print(tes)
        return print (tes)
        
tA= (2,2,2,2,2,2,2)
cek_isi_tuple(tA)
