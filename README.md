# 🧪 Scraping Data dengan ETL Pipeline Sederhana

Proyek ini merupakan implementasi sederhana dari proses ETL (Extract, Transform, Load) untuk pengambilan data dari web (web scraping), transformasi data, dan penyimpanannya ke dalam format CSV, Database PostgreSQL, dan Google Sheet untuk dianalisis lebih lanjut.

## 📌 Tujuan Proyek

- Mengambil data dari sebuah website menggunakan `requests` dan `BeautifulSoup`
- Membersihkan dan mentransformasi data mentah
- Menyimpan data hasil scraping ke dalam file `.csv`
- Menerapkan prinsip sederhana ETL dalam konteks scraping data

## 🧰 Tools & Teknologi

- Python
- Requests
- BeautifulSoup (bs4)
- Pandas
- Jupyter Notebook

## 🔄 Alur ETL Pipeline

1. **Extract**  
   Mengambil data dari website target menggunakan `requests.get()` dan mem-parsing HTML dengan `BeautifulSoup`.

2. **Transform**  
   Membersihkan data (misal: menghapus tag HTML, memformat teks), memfilter informasi yang relevan, dan menyusunnya ke dalam DataFrame menggunakan `pandas`.

3. **Load**  
   Menyimpan data hasil transformasi ke dalam file CSV, Database PostgreSQL, dan Google Sheet untuk dianalisis lebih lanjut.

## 📊 Hasil

- Data berhasil diekstrak dan disimpan ke dalam `data/hasil_scraping.csv`.
- Pipeline ETL bekerja secara berurutan dan modular.
- Cocok sebagai pondasi awal untuk proses data pipeline skala lebih besar.

## 🚀 Penggunaan

Clone repositori ini dan jalankan file notebook:

```bash
git clone https://github.com/daffahaidarfarrass/Scraping-data-dengan--ETL-Pipeline-Sederhana.git
cd Scraping-data-dengan--ETL-Pipeline-Sederhana
jupyter notebook etl_pipeline_scraping.ipynb
```


# google sheet link
    - https://docs.google.com/spreadsheets/d/1lKN8mEXUdjQN_Ivbculxds7z9sEBgaBCtVuAM-ua2xk/edit?usp=sharing

# Database PostgreSQL
    - database = fashiondb
    - username = daffa
    - password = #Deuverh12
    - port = 5432

# Sebelum menjalankan program utama kita membuat database PostgreSQL terlebih dahulu
    - buka CMD/powershell
    - Ketik psql --username postgres
    - Lalu, CREATE USER daffa WITH ENCRYPTED PASSWORD '#Deuverh12';
    - Lalu, CREATE DATABASE fashiondb;
    - Berisi akses ke username daffa
    - Ketik GRANT ALL ON DATABASE fashiondb TO daffa;
    - Lalu, ALTER DATABASE fashiondb OWNER TO daffa;
    - Lalu, exit

# Setelah membuat username dan database fashiondb. Lalu, install semua library yang dibutuhkan
    - Masuk ke folder submission-pemda
    - ketik pip install -r requirements.txt

# Cara menjalankan program utama
    - ketik py main.py

# Cara Menjalankan unit test pada folder tests
    - python3 -m pytest tests

# Cara Menjalankan test coverage pada folder tests
    - ketik coverage run -m pytest tests

# Cara melakukan testing dengan hasil yang lebih detail terhadap file program pada folder tests
    - ketik pip install pytest pytest-cov
    - testing extract.py
        - Ketik py -m pytest tests/test_extract.py -v --cov --cov-report=html
        - Lalu, akan muncul folder baru htmlcov
        - Klik, index.html untuk melihat hasil
        - Coverage report terakhir 95%
    - testing load.py 
        - Ketik py -m pytest tests/test_load.py -v --cov --cov-report=html
        - Lalu, akan muncul folder baru htmlcov
        - Klik, index.html untuk melihat hasil
        - Coverage report terakhir 76%
    - testing transform.py
        - Ketik py -m pytest tests/test_transform.py -v --cov --cov-report=html
        - Lalu, akan muncul folder baru htmlcov
        - Klik, index.html untuk melihat hasil
        - Coverage report terakhir 89%
# Untuk file google-sheets-api.json silahkan bikin sendiri. Melalui google service
# Laman website: https://fashion-studio.dicoding.dev.  
