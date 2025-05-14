# google sheet link = https://docs.google.com/spreadsheets/d/1lKN8mEXUdjQN_Ivbculxds7z9sEBgaBCtVuAM-ua2xk/edit?usp=sharing

# Database PostgreSQL = 
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
