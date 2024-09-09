import unittest
from src.analyzer import preprocess_text, extract_strategies

class TestAnalyzer(unittest.TestCase):
    def test_preprocess_text(self):
        raw_text = "This is an example um of preprocessing uh text."
        cleaned_text = preprocess_text(raw_text)
        self.assertNotIn("um", cleaned_text)
        self.assertNotIn("uh", cleaned_text)
    
    def test_extract_strategies(self):
        cleaned_text = "Our trading strategy involves identifying key support levels."
        strategies = extract_strategies(cleaned_text)
        self.assertGreater(len(strategies), 0)
        self.assertIn("strategy", strategies[0]['strategy'].lower())

if __name__ == '__main__':
    unittest.main()
