from ModulKulit import konfigurasi_elektron
from ModulKulit import nomor_atom

def bilangan_kuantum_azimut(kulit):
    nilai_kulit = {
        's': 0,
        'p': 1,
        'd': 2,
        'f': 3
    }
    konfigurasi_terakhir = ''
    for i in kulit:
        if i.isalpha():
            konfigurasi_terakhir = i
    return nilai_kulit.get(konfigurasi_terakhir)

konfigurasi = konfigurasi_elektron(nomor_atom) 
bilangan_kuantum = bilangan_kuantum_azimut(konfigurasi)
print(f'l =', bilangan_kuantum)