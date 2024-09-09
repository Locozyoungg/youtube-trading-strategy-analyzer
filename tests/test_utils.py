import unittest
from src.utils import clean_text

class TestUtils(unittest.TestCase):
    def test_clean_text(self):
        text = "Sample text to be cleaned."
        cleaned_text = clean_text(text)
        self.assertEqual(cleaned_text, text)

if __name__ == '__main__':
    unittest.main()
