import unittest
import pandas as pd
from utils.transform import transform_data

class TestTransformData(unittest.TestCase):
    def test_transform_valid_data(self):
        raw_data = [
            {
                "Title": "Cool Shirt",
                "Price": "10.0",
                "Rating": "4.5",
                "Colors": "Red",
                "Size": "M",
                "Gender": "Unisex",
                "timestamp": "2025-05-07T10:00:00"
            }
        ]
        df = transform_data(raw_data)

        self.assertEqual(len(df), 1)
        self.assertEqual(df.iloc[0]["Title"], "Cool Shirt")
        self.assertEqual(df.iloc[0]["Price"], 160000)  # 10 * 16000

    def test_transform_invalid_data(self):
        raw_data = [
            {
                "Title": "Unknown Product",  # Akan dibuang
                "Price": "abc",              # Tidak valid
                "Rating": "NaN",             # Tidak valid
                "Colors": "Blue",
                "Size": "L",
                "Gender": "Male",
                "timestamp": "2025-05-07T10:00:00"
            }
        ]
        df = transform_data(raw_data)
        self.assertEqual(len(df), 0)
