import pandas as pd

def transform_data(data):
    try:
        df = pd.DataFrame(data)
        df.dropna(inplace=True)
        df.drop_duplicates(inplace=True)

        # Buang produk tidak valid
        df = df[df["Title"] != "Unknown Product"]
        df = df[df["Rating"].str.replace('.', '', 1).str.isnumeric()]  # validasi rating

        # Konversi harga ke rupiah
        df["Price"] = df["Price"].astype(float) * 16000
        df["Price"] = df["Price"].astype(int)

        return df

    except Exception as e:
        print(f"Error in transform_data: {e}")
        return pd.DataFrame()
