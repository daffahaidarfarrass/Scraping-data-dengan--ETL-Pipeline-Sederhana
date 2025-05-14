import unittest
import os
import pandas as pd
from sqlalchemy import create_engine, text
from utils.load import load_to_postgresql, load_to_csv, load_to_google_sheets

class TestLoadData(unittest.TestCase):
    def setUp(self):
        self.test_db_url = "postgresql://daffa:#Deuverh12@localhost:5432/fashiondb"
        self.table_name = "test_table"
        self.df = pd.DataFrame([{
            "Title": "Cool Shirt",
            "Price": 150000,
            "Rating": 4.8,
            "Colors": "3",
            "Size": "L",
            "Gender": "Unisex",
            "timestamp": "2025-05-07T10:00:00"
        }])

        self.csv_filename = "fashion_data.csv"
        self.sheet_url = "https://docs.google.com/spreadsheets/d/1lKN8mEXUdjQN_Ivbculxds7z9sEBgaBCtVuAM-ua2xk/edit?usp=sharing"

    def test_load_to_postgresql(self):
        try:
            load_to_postgresql(self.df, self.test_db_url, self.table_name)

            engine = create_engine(self.test_db_url)
            with engine.connect() as conn:
                result = conn.execute(text(f"SELECT COUNT(*) FROM {self.table_name}"))
                count = result.scalar()
                self.assertEqual(count, 1)
        except Exception as e:
            self.fail(f"Failed to load data to PostgreSQL: {e}")

    def test_load_to_csv(self):
        try:
            load_to_csv(self.df, self.csv_filename)

            # Pastikan file CSV telah dibuat dan data sudah ada di dalamnya
            self.assertTrue(os.path.exists(self.csv_filename))

            # Membaca kembali file CSV untuk memastikan data yang tepat
            df_loaded = pd.read_csv(self.csv_filename)
            self.assertEqual(len(df_loaded), 1)  # Pastikan ada 1 baris data
            self.assertEqual(df_loaded["Title"][0], "Cool Shirt")
        except Exception as e:
            self.fail(f"Failed to load data to CSV: {e}")
        finally:
            # Hapus file CSV setelah pengujian, jika ada
            if os.path.exists(self.csv_filename):
                os.remove(self.csv_filename)

    def test_load_to_google_sheets(self):
        try:
            # Asumsi: credentials.json telah disiapkan untuk akses ke Google Sheets
            load_to_google_sheets(self.df, self.sheet_url, "../google-sheets-api.json")

            self.assertTrue(True)
        except Exception as e:
            self.fail(f"Failed to load data to Google Sheets: {e}")

    def tearDown(self):
        # Bersihkan tabel setelah test PostgreSQL
        try:
            engine = create_engine(self.test_db_url)
            with engine.connect() as conn:
                conn.execute(text(f"DROP TABLE IF EXISTS {self.table_name}"))
        except Exception as e:
            self.fail(f"Failed to clean up database: {e}")
