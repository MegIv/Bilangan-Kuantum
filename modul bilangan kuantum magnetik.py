def Kuantum_Magnetik(subkulit, jumlah_elektron):
    if subkulit == 's':
        l = 0  
        jumlah_orbital = 1
    elif subkulit == 'p':
        l = 1
        jumlah_orbital = 3
    elif subkulit == 'd':
        l = 2 
        jumlah_orbital = 5
    elif subkulit == 'f':
        l = 3  
        jumlah_orbital = 7
        return
    orbital = [[0, 0] for _ in range(jumlah_orbital)]  
    bilangan_kuantum_magnetik = list(range(-l, l + 1))
    posisi_terakhir = None
    for i in range(jumlah_elektron):
        for pengisian in range(jumlah_orbital):
            if orbital[pengisian][0] == 0:  
                orbital[pengisian][0] = 1  
                posisi_terakhir = pengisian  
                break
        else:
            for pengisian in range(jumlah_orbital):
                if orbital[pengisian][1] == 0:  
                    orbital[pengisian][1] = 1   
                    posisi_terakhir = pengisian  
                    break
    print(f"Nilai Kuantum Magnetik = {bilangan_kuantum_magnetik[posisi_terakhir]}")
    __init__ == '__main__'
subkulit = input("Masukkan subkulit (s, p, d, f): ")
jumlah_elektron = int(input("Masukkan jumlah elektron: "))
Kuantum_Magnetik(subkulit, jumlah_elektron)
