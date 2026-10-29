with open("data/nilai.txt", "r", encoding="utf-8") as file:
    for baris in file:
        baris = baris.strip()
        if not baris:
            continue
        parts = baris.split(",")
        if len(parts) == 2:
            nim, teks_nilai = parts
            try:
                print(nim.strip(), float(teks_nilai))
            except ValueError:
                pass