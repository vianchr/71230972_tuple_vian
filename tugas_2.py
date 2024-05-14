def nama_nim_tempat(tuple):
    NIM={}
    Nama={}
    alamat={}
    
    for item in tuple:
        if item == tuple[0]:
            Nama=item
        elif item == tuple[1]:
            NIM=item
        else:
            alamat=item
    print (f"NIM    : {NIM}")
    print (f"Nama   : {Nama}")
    print (f"alamat : {alamat}\n")
    print (f"NIM           : {convert(NIM)}")
    #nama depan :
    nama_depan = Nama.split()[0]
    print (f"nama depan    : {convert(nama_depan)[1::]}")
    #nama terbalik :
    nama_terbalik = reversed(Nama.split())
    print (f"nama terbalik : {convert(nama_terbalik)}")
    
            
def convert(list):
    return tuple(list)
    
   



Data=('Matahari Bhakti Nendya', '22064091', 'Bantul, DI Yogyakarta')
nama_nim_tempat(Data)