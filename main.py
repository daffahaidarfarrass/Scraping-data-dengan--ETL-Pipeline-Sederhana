from utils.extract import extract_data, scrape_multiple_pages
from utils.transform import transform_data
from utils.load import load_to_csv, load_to_google_sheets, load_to_postgresql

# URL dasar tanpa nomor halaman
base_url = "https://fashion-studio.dicoding.dev"

# Ambil data dari 50 halaman
raw_data = scrape_multiple_pages(base_url, 50)

# Transformasi data
clean_data = transform_data(raw_data)

# Simpan data ke CSV
load_to_csv(clean_data, filename='products.csv')

# Simpan data ke Google Sheet
sheet_url = "https://docs.google.com/spreadsheets/d/1lKN8mEXUdjQN_Ivbculxds7z9sEBgaBCtVuAM-ua2xk/edit?usp=edit"

load_to_google_sheets(clean_data, sheet_url=sheet_url, credentials_file="google-sheets-api.json")


# Simpan data ke PostgreSQL
db_url = "postgresql://daffa:#Deuverh12@localhost:5432/fashiondb"

load_to_postgresql(clean_data, db_url=db_url, table_name="fashion_data")
