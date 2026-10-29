def baca_data(nama_file):
    """Membaca dan memvalidasi data nilai dari file teks."""
    data = []
    try:
        with open(nama_file, "r", encoding="utf-8") as file:
            for nomor, baris in enumerate(file, start=1):
                baris = baris.strip()
                if not baris:
                    continue  # Lewati baris kosong
                
                parts = baris.split(",")
                if len(parts) != 2:
                    print(f"Baris {nomor} dilewati (format tidak sesuai): {baris}")
                    continue
                
                nim, teks_nilai = parts
                try:
                    nilai = float(teks_nilai.strip())
                    data.append((nim.strip(), nilai))
                except ValueError:
                    print(f"Baris {nomor} dilewati (nilai bukan angka): {baris}")
                    
    except FileNotFoundError:
        print(f"Kesalahan: File '{nama_file}' tidak ditemukan.")
    
    return data

def tulis_rekap(nama_file, data):
    """Menulis ringkasan statistik rekap nilai ke file output."""
    if not data:
        print("Tidak ada data valid untuk direkap.")
        return
    
    nilai_list = [item[1] for item in data]
    jumlah_data = len(nilai_list)
    rata_rata = sum(nilai_list) / jumlah_data
    nilai_min = min(nilai_list)
    nilai_max = max(nilai_list)
    jumlah_lulus = sum(1 for x in nilai_list if x >= 60)
    
    with open(nama_file, "w", encoding="utf-8") as file:
        file.write(f"Jumlah data valid: {jumlah_data}\n")
        file.write(f"Rata-rata: {rata_rata:.2f}\n")
        file.write(f"Minimum: {nilai_min:.2f}\n")
        file.write(f"Maksimum: {nilai_max:.2f}\n")
        file.write(f"Jumlah lulus: {jumlah_lulus}\n")
        
    print(f"Rekap berhasil ditulis ke '{nama_file}'.")

if __name__ == "__main__":
    input_file = "data/nilai.txt"
    output_file = "data/hasil_rekap.txt"
    
    print("Memproses data nilai...")
    data_mahasiswa = baca_data(input_file)
    
    if data_mahasiswa:
        tulis_rekap(output_file, data_mahasiswa)
        print("Proses selesai.")