# Pacakage Bilangan Kuantum

Paket ini membantu menghitung berbagai bilangan kuantum berdasarkan nomor atom. Terdiri dari modul untuk menghitung konfigurasi elektron, bilangan kuantum utama, bilangan kuantum azimut, bilangan kuantum magnetik, dan bilangan kuantum spin.

## Instalasi

Pastikan Python sudah terpasang di sistem Anda. 
### pip:
```bash
pip install quantum-101==0.3
```

### Contoh Penggunaan

Berikut adalah contoh sederhana cara menggunakan package ini setelah diinstal:

```python
from quantum_101 import konfigurasi_elektron
from quantum_101 import kuantumUtama
from quantum_101 import bilangan_kuantum_azimut
from quantum_101 import mengambil_konfigurasi_terakhir
from quantum_101.kuantum_magnetik import Kuantum_Magnetik
from quantum_101.kuantum_spin import Kuantum_Magnetik as kuantum_spin

# Contoh: Menghitung properti kuantum untuk unsur Besi (Fe) dengan nomor atom 26.
nomor_atom = 26

# Konfigurasi elektron
konfigurasi_elektron = konfigurasi_elektron(nomor_atom)
print(f"Konfigurasi Elektron: {konfigurasi_elektron}")

# Bilangan kuantum utama (n)
n = kuantumUtama(nomor_atom)
print(f"Bilangan Kuantum Utama: n = {n}")

# Bilangan kuantum azimut (l)
l = bilangan_kuantum_azimut(konfigurasi_elektron)
print(f"Bilangan Kuantum Azimut: l = {l}")

# Bilangan kuantum magnetik (ml)
Kuantum_Magnetik(nomor_atom)

# Bilangan kuantum spin (ms)
kuantum_spin(nomor_atom)

# Nama unsur dan golongan
cari_nama_unsur(nomor_atom)
print(f"Unsur: {nama_unsur}")
```

---

## Penjelasan Modul

### 1. **Modul Kulit (Konfigurasi Elektron)**

Modul ini menghitung konfigurasi elektron untuk sebuah nomor atom.

#### Fungsi:
```python
konfigurasi_elektron(nomor_atom)
```

#### Penggunaan:
```python
konfigurasi = konfigurasi_elektron(26)
print(konfigurasi)  # Output: Konfigurasi elektron untuk unsur Besi (Fe)
```

---

### 2. **Modul Kuantum Utama (Bilangan Kuantum Utama)**

Modul ini mengekstrak bilangan kuantum utama (n) dari konfigurasi elektron.

#### Fungsi:
```python
kuantumUtama(nomor_atom)
```

#### Penggunaan:
```python
n = kuantumUtama(26)
print(n)  # Output: Bilangan kuantum utama
```

---

### 3. **Modul Kuantum Azimut (Bilangan Kuantum Azimut)**

Modul ini menghitung bilangan kuantum azimut (l) berdasarkan subkulit terakhir dari konfigurasi elektron.

#### Fungsi:
```python
bilangan_kuantum_azimut(konfigurasi)
```

#### Penggunaan:
```python
l = bilangan_kuantum_azimut(26)
print(l)  # Output: Bilangan kuantum azimut
```

---

### 4. **Modul Kuantum Magnetik (Bilangan Kuantum Magnetik)**

Modul ini menghitung bilangan kuantum magnetik (ml) untuk subkulit terakhir.

#### Fungsi:
```python
Kuantum_Magnetik(nomor_atom)
```

#### Penggunaan:
```python
Kuantum_Magnetik(26)  
# Output: Bilangan kuantum magnetik untuk Besi
```

---

### 5. **Modul Spin (Bilangan Kuantum Spin)**

Modul ini menghitung bilangan kuantum spin (ms) untuk elektron terakhir.

#### Fungsi:
```python
kuantum_spin(nomor_atom)
```

#### Penggunaan:
```python
kuantum_spin(26)  
# Output: Bilangan kuantum spin untuk Besi
```

---

### 6. **Modul Nomor Atom (Nama dan Golongan Unsur)**

Modul ini mengembalikan nama dan golongan unsur berdasarkan nomor atom.

#### Fungsi:
```python
cari_nama_unsur(nomor_atom)
```

#### Penggunaan:
```python
nama_unsur = cari_nama_unsur(26)
print(nama_unsur)  # Output: Nama unsur dan golongan untuk Besi
```

---
#### Contact :
ivanramadhan4818@gmail.com
