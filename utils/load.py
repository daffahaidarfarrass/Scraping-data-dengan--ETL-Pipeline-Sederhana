import pandas as pd
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from sqlalchemy import create_engine

def load_to_csv(df, filename="products.csv"):
    try:
        df.to_csv(filename, index=False)
        print(f"Data berhasil disimpan ke {filename}")
    except Exception as e:
        print(f"Gagal menyimpan data ke CSV: {e}")


def load_to_google_sheets(df, sheet_url, credentials_file="google-sheets-api.json"):
    try:
        # Menyiapkan scope akses Google Sheets dan Drive
        scope = [
            "https://spreadsheets.google.com/feeds",
            "https://www.googleapis.com/auth/spreadsheets",
            "https://www.googleapis.com/auth/drive.file",
            "https://www.googleapis.com/auth/drive"
        ]

        # Autentikasi dengan Service Account
        creds = ServiceAccountCredentials.from_json_keyfile_name(credentials_file, scope)
        client = gspread.authorize(creds)

        # Membuka spreadsheet berdasarkan URL
        spreadsheet = client.open_by_url(sheet_url)
        sheet = spreadsheet.sheet1

        # Gabungkan header + data
        values = [df.columns.tolist()] + df.values.tolist()

        # Tulis semua ke sheet sekaligus
        sheet.update(values)

        print(f"Data berhasil disimpan ke Google Sheets: {spreadsheet.title}")
    
    except Exception as e:
        print(f"Gagal menyimpan data ke Google Sheets: {e}")


def load_to_postgresql(df, db_url, table_name="fashion_data"):
    try:
        # Membuat koneksi engine PostgreSQL
        engine = create_engine(db_url)

        # Menyimpan data ke tabel PostgreSQL (jika tabel belum ada, akan dibuat)
        df.to_sql(table_name, engine, if_exists='replace', index=False)

        print(f"Data berhasil disimpan ke PostgreSQL: tabel '{table_name}'")

    except Exception as e:
        print(f"Gagal menyimpan ke PostgreSQL: {e}")


