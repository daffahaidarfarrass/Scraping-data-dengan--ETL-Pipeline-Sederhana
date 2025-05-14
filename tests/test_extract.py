import unittest
from unittest.mock import patch, Mock
from utils.extract import extract_data, scrape_multiple_pages

# Contoh HTML dummy yang menyerupai struktur asli halaman
SAMPLE_HTML = """
<html>
  <body>
    <div class="product-details">
      <div class="product-title">Cool Shirt</div>
      <div class="price">$29.99</div>
      Rating: ⭐ 4.5 / 5
      Colors: 3
      Size: M
      Gender: Unisex
    </div>
  </body>
</html>
"""

class TestExtractData(unittest.TestCase):

    @patch("utils.extract.requests.get")
    def test_extract_data_single_page(self, mock_get):
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.text = SAMPLE_HTML
        mock_get.return_value = mock_response

        url = "https://fake-url.com"
        result = extract_data(url)

        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]["Title"], "Cool Shirt")
        self.assertEqual(result[0]["Price"], "29.99")
        self.assertEqual(result[0]["Rating"], "4.5")
        self.assertEqual(result[0]["Colors"], "5")
        self.assertEqual(result[0]["Size"], "M")
        self.assertEqual(result[0]["Gender"], "Unisex")
        self.assertIn("timestamp", result[0])

    @patch("utils.extract.extract_data")
    def test_scrape_multiple_pages(self, mock_extract_data):
        mock_extract_data.side_effect = [
            [{"Title": "Page1", "Price": "10", "Rating": "5", "Colors": "3", "Size": "L", "Gender": "Unisex", "timestamp": "dummy"}],
            [{"Title": "Page2", "Price": "20", "Rating": "4", "Colors": "3", "Size": "M", "Gender": "Male", "timestamp": "dummy"}]
        ]

        base_url = "https://fake-url.com"
        result = scrape_multiple_pages(base_url, 2)

        self.assertEqual(len(result), 2)
        self.assertEqual(result[0]["Title"], "Page1")
        self.assertEqual(result[1]["Title"], "Page2")
    