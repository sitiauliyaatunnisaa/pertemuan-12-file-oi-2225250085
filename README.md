# Pertemuan 12 - File I/O dan Error Handling

* **Nama:** Siti Auliyaatunnisaa
* **NIM:** 2225250085
* **Kelas:** 3A

## Tujuan
Membaca, memvalidasi, mengolah, dan menulis data file dengan Python secara modular di VS Code.

## Format File Input
A001,85
A002,78
A003,92
A004,abc
A005,74

## Cara Menjalankan
python tugas/rekap_nilai_file.py

## Error yang Ditangani
- FileNotFoundError: Ditangani ketika file input utama (data/nilai.txt) tidak ditemukan di dalam direktori.
- ValueError: Ditangani per baris ketika program mendapati data nilai berupa teks non-angka (misalnya abc), sehingga baris tersebut dilewati tanpa membuat program crash.

## Test Case
| Kondisi / Kasus Uji | Hasil yang Diharapkan | Hasil Aktual | Status |
| :--- | :--- | :--- | :--- |
| **File input (`nilai.txt`) ada dan valid** | Program membaca seluruh baris, menghitung statistik, dan menulis rekap ke file output. | Statistik berhasil dihitung dan file `hasil_rekap.txt` terisi dengan benar. | **Berhasil** |
| **File input (`nilai.txt`) tidak ditemukan** | Program menangkap `FileNotFoundError` dan menampilkan pesan kesalahan tanpa *crash*. | Muncul pesan peringatan file tidak ditemukan dengan aman. | **Berhasil** |
| **Terdapat data nilai berupa huruf (`abc`)** | Program mendeteksi `ValueError`, melewati baris tersebut, dan tetap memproses data valid lainnya. | Baris invalid dilewati tanpa menghentikan program. | **Berhasil** |

## Refleksi
Salah satu error yang ditemukan selama pembuatan program adalah `ValueError`, yang terjadi saat fungsi `float()` mencoba mengubah teks non-angka (seperti huruf `abc`) menjadi format numerik. Program menanganinya dengan menggunakan blok `try-except` di dalam perulangan baris file, sehingga baris yang bermasalah dapat dilewati dengan aman tanpa menghentikan proses rekapitulasi data mahasiswa secara keseluruhan.