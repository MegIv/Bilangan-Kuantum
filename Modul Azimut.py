from ModulKulit import nomor_atom

def bilangan_kuantum_azimut(nilai_kulit):
    nilai_kulit = {
        's': 0,
        'p': 1,
        'd': 2,
        'f': 3
    }
    konfigurasi_terakhir = ''
    for i in nilai_kulit:
        if i.isalpha():
            konfigurasi_terakhir = i
    return nilai_kulit.get(konfigurasi_terakhir)

__init__ = '__main__' 
bilangan_kuantum = bilangan_kuantum_azimut(nomor_atom)
print(f'l =', bilangan_kuantum)
