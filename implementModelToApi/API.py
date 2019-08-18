#! /home/naufal/Playground/belajarAPI/env/bin/python

 # IMPORT library, diperlukan untuk menjalankan flask. ibarat iostream di c++ (untuk cout & cin)
from flask import Flask, jsonify, request

 # Penjelasan
# Flask, jsonify & requests berasalah dari satu sumber yaitu flask <-- framework flask.
# artinya kita mengambil 3 fitur dari framework flask. ada banyak fitur lainnya

AplikasiAPI = Flask(__name__)
# mendefinisikan applikasi

 # mengatur rute atau url aplikasi
@AplikasiAPI.route('/API', methods=["GET"]) # isinya () dengan url yang diinginkan misal /datauser atau lainnya
def indexAplikasi(): # fungsi dari rute diatas
  # disini kita bisa menuliskan kode2 kita untuk nantinya di return ke halaman API

   # Mendefinisikan Query
  query = request.args.get('query') # query adalah parameter dari url, misal localhost/index.php?query=contoh <--- contoh adalah query,
  # query bisa diubah sesuai kebutuhan, namanya gk harus query 

   # CONTOH DATABASE DIBAWAH DIGANTI DENGAN SOURCE CODE UNTUK MENGAMBIL DATA DARI DB, 
  # CODE DIBAWAH INI HANYA CONTOH
  contohDataDariDatabase = [{
    "judul":"Javascript",
    "rekomendasi-1":"buku001", # Penjelasan, buku001 adalahh kode buku. buku001 bisa diubah menjadi judul atau yang lain sesuai kebutuhan
    "rekomendasi-2":"buku002",
    "rekomendasi-3":"buku003",
    "rekomendasi-4":"buku004",
  },{
    "judul":"PHP",
    "rekomendasi-1":"buku006", # Penjelasan, buku001 adalahh kode buku. buku001 bisa diubah menjadi judul atau yang lain sesuai kebutuhan
    "rekomendasi-2":"buku007",
    "rekomendasi-3":"buku004",
    "rekomendasi-4":"buku0010",
  }]

   # Perulangan Untuk Mengecek apakah query ada didalam databasee
  for data in contohDataDariDatabase:
    if data["judul"].lower() == query.lower(): # Jika ketemu langsung tampilkan ke web. # lower digunakan agar semua huruf jadi kecil
      return jsonify({
        "Pesan":"Berhasil",
        "Rekomendasi-1":data["rekomendasi-1"],
        "Rekomendasi-2":data["rekomendasi-2"],
        "Rekomendasi-3":data["rekomendasi-3"],
        "Rekomendasi-4":data["rekomendasi-4"],
      })

   # Jika tidak ketemu
  return jsonify({
    "Pesan":"Tidak Ditemukan"
  })

 # fungsi main, untuk menjalankan aplikasi
if __name__ == '__main__':
  AplikasiAPI.run() 