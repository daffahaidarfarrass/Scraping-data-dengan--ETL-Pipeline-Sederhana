from bs4 import BeautifulSoup
from datetime import datetime
import requests

def extract_data(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')

        products = []
        for div in soup.select(".product-details"):
            title = div.select_one(".product-title").text.strip()
            price = div.select_one(".price").text.strip().replace("$", "")
            rating = div.text.split("Rating: ⭐ ")[-1].split(" /")[0].strip()
            colors = div.text.split("Colors")[0].strip().split()[-1]
            size = div.text.split("Size: ")[-1].split("\n")[0].strip()
            gender = div.text.split("Gender: ")[-1].split("\n")[0].strip()

            products.append({
                "Title": title,
                "Price": price,
                "Rating": rating,
                "Colors": colors,
                "Size": size,
                "Gender": gender,
                "timestamp": datetime.now().isoformat()
            })

        return products

    except Exception as e:
        print(f"Error in extract_data: {e}")
        return []

# Fungsi untuk mengambil data dari beberapa halaman
def scrape_multiple_pages(base_url, num_pages):
    all_data = []
    
    # Ambil data dari halaman pertama
    print(f"Berhasil Scraping data produk dari {base_url}")
    raw_data = extract_data(base_url)
    all_data.extend(raw_data)

    # Ambil data dari halaman berikutnya
    for page in range(2, num_pages + 1):
        url = f"{base_url}/page{page}"
        print(f"Berhasil Scraping data produk dari {url}")
        raw_data = extract_data(url)
        all_data.extend(raw_data)  # Gabungkan data dari setiap halaman

    return all_data
