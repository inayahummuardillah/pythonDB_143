import tkinter as tk
import sqlite3


# Fungsi untuk membuat tabel jika belum ada
def create_table():
    connection = sqlite3.connec('Tkinter2.db')
    cursor = connection.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS nilai (
                   id INTEGER PRIMARY KEY ,
                   siswa TEXT ,
                   biologi INTEGER ,
                   fisika INTEGER ,
                   inggris INTEGER
                )''')
    connection.commit()
    connection.close()

# Fungsi untuk memasukkan data ke dalam database
def insert_data():
    siswa = entry_nama.get()
    biologi = int(entry_biologi.get())
    fisika = int(entry_fisika.get())
    inggris = int(entry_inggris.get())

    # Mencari nilai tertinggi dan menentukan prediksi fakultas"
    max_nilai = max(entry_biologi, entry_fisika, entry_inggris)
    prediksi = ""
    if max_nilai == entry_biologi:
        prediksi = "kedokteran"
    elif max_nilai == entry_fisika:
        prediksi = "Teknik"
    elif max_nilai == entry_inggris:
        prediksi = "Bahasa"

    hasil.config(text=f"Hasil Prediksi: {prediksi}")

    connection = sqlite3.connect('Tkinter2.db')
    cursor = connection.cursor()
    cursor.execute('''INSERT INTO nilai (siswa, biologi, fisika, inggris)
                       VALUES (?, ?, ?, ?) ''', (siswa, biologi, fisika, inggris))
    connection.commit()
    connection.close()

# fungsi untuk menyimpan data setelah tombol "simpan" ditekan
def simpan_data():
    insert_data()
    entry_nama.delete(0, tk.END)
    entry_biologi.delete(0, tk.END)
    entry_fisika.delete(0, tk.END)
    entry_inggris.delete(0, tk.END)

# Membuat tabel jika belum ada
create_table()

# Membuat GUI menggunakan Tkinter
root =tk.Tk()
root.title("Input nilai siswa")

label_nama = tk.Label(root, text="Nama Siswa:")
label_nama.pack()
entry_nama = tk.Entry(root)
entry_nama.pack()

label_biologi = tk.Label(root, text="Nilai Biologi:")
label_biologi.pack()
entry_biologi = tk.Entry(root)
entry_biologi.pack()

label_fisika = tk.Label(root, text="Nilai Fisika:")
label_fisika.pack()
entry_fisika = tk.Entry(root)
entry_fisika.pack()

label_inggris = tk.Label(root, text="Nilai Inggris:")
label_inggris.pack()
entry_inggris = tk.Entry(root)
entry_inggris.pack()

button_simpan = tk.Button(root, text="Simpan", command=simpan_data)
button_simpan.pack()

hasil = tk.Label(root, text="Hasil Prediksi: Bahasa")
hasil.pack()

root.mainloop()
