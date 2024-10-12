# Pacakage Bilangan Kuantum

Paket ini membantu menghitung berbagai bilangan kuantum berdasarkan nomor atom. Terdiri dari modul untuk menghitung konfigurasi elektron, bilangan kuantum utama, bilangan kuantum azimut, bilangan kuantum magnetik, dan bilangan kuantum spin.

## Instalasi

Pastikan Python sudah terpasang di sistem Anda. 
### pip:
```bash
pip install quantum-101==0.2
```

### Contoh Penggunaan

Berikut adalah contoh sederhana cara menggunakan package ini setelah diinstal:

```python
import konfig_elektron
import kuantum_utama
import kuantum_azimut
import kuantum_magnetik
import kuantum_spin
import nomor_atom

# Contoh: Menghitung properti kuantum untuk unsur Besi (Fe) dengan nomor atom 26.
nomor_atom = 26

# Konfigurasi elektron
konfigurasi_elektron = konfig_elektron.konfigurasi_elektron(nomor_atom)
print(f"Konfigurasi Elektron: {konfigurasi_elektron}")

# Bilangan kuantum utama (n)
n = kuantum_utama.kuantumUtama(nomor_atom)
print(f"Bilangan Kuantum Utama: n = {n}")

# Bilangan kuantum azimut (l)
l = kuantum_azimut.bilangan_kuantum_azimut(konfigurasi_elektron)
print(f"Bilangan Kuantum Azimut: l = {l}")

# Bilangan kuantum magnetik (ml)
kuantum_magnetik.Kuantum_Magnetik(nomor_atom)

# Bilangan kuantum spin (ms)
kuantum_spin.Bilangan_Spin(nomor_atom)

# Nama unsur dan golongan
nama_unsur = nomor_atom.cari_nama_unsur(nomor_atom)
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
konfigurasi = konfig_elektron.konfigurasi_elektron(26)
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
n = kuantum_utama.kuantumUtama(26)
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
l = kuantum_azimut.bilangan_kuantum_azimut(konfigurasi_elektron)
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
kuantum_magnetik.Kuantum_Magnetik(26)  
# Output: Bilangan kuantum magnetik untuk Besi
```

---

### 5. **Modul Spin (Bilangan Kuantum Spin)**

Modul ini menghitung bilangan kuantum spin (ms) untuk elektron terakhir.

#### Fungsi:
```python
Bilangan_Spin(nomor_atom)
```

#### Penggunaan:
```python
kuantum_spin.Bilangan_Spin(26)  
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
nama_unsur = nomor_atom.cari_nama_unsur(26)
print(nama_unsur)  # Output: Nama unsur dan golongan untuk Besi
```

---
#### Contact :
ivanramadhan4818@gmail.com
