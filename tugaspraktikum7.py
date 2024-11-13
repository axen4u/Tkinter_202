import tkinter as tk


# Fungsi untuk menangani prediksi
def hasil_prediksi():
    try:
        # Dapatkan nilai-nilai dari entri input dan konversikan ke angka
        nilai = []
        for entry in entries:
            val = entry.get().strip()  # Menghapus spasi ekstra
            if val == "":  # Cek apakah input kosong
                raise ValueError("Semua nilai harus diisi!")
            if not val.isdigit():  # Cek apakah input adalah angka
                raise ValueError("Masukkan hanya angka untuk nilai!")
            nilai.append(float(val))
        
        # Menghitung rata-rata nilai
        rata_rata = sum(nilai) / len(nilai)

        # Prediksi prodi berdasarkan rata-rata nilai
        if rata_rata >= 75:
            prodi = "Teknologi Informasi"
        else:
            prodi = "Manajemen"

        # Menampilkan hasil prediksi
        result_label.config(text=f"Hasil Prediksi: {prodi}")

    except ValueError as e:
        # Menampilkan pesan error jika ada input yang salah
        messagebox.showerror("Error", str(e))

# Membuat jendela utama
root = tk.Tk()
root.title("Aplikasi Prediksi Prodi Pilihan")

# Mengatur ukuran window
root.geometry("400x500")

# Judul Aplikasi
judul_label = tk.Label(root, text="Aplikasi Prediksi Prodi Pilihan", font=("Arial", 14, "bold"))
judul_label.pack(pady=10)

# Membuat 10 input untuk nilai mata pelajaran
entries = []
for i in range(1, 11):
    frame = tk.Frame(root)  # Membuat frame untuk label dan entry agar rapi
    frame.pack(pady=5)
    
    label = tk.Label(frame, text=f"Nilai Mata Pelajaran {i}:")
    label.pack(side=tk.LEFT, padx=5)  # Menempatkan label di kiri
    
    entry = tk.Entry(frame)
    entry.pack(side=tk.LEFT, padx=5)# Menempatkan label di kiri
    
    entry = tk.Entry(frame)
    entry.pack(side=tk.LEFT, padx=5)  # Menempatkan entry di sebelah label
    entries.append(entry)

# Button untuk memprediksi prodi pilihan
predict_button = tk.Button(root, text="Hasil Prediksi", command=hasil_prediksi)
predict_button.pack(pady=20)

# Label untuk menampilkan hasil prediksi
result_label = tk.Label(root, text="Hasil Prediksi: ", font=("Arial", 12))
result_label.pack(pady=10)

# Menjalankan aplikasi
root.mainloop()
