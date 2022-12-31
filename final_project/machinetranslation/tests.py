import sys
import unittest
from translator import english_to_french, french_to_english

class TestTranslator(unittest.TestCase):
    def test_english_to_french(self):
        self.assertIsNone(english_to_french(None))
        self.assertEqual(english_to_french('Hello'), 'Bonjour')
        self.assertNotEqual(english_to_french('Hello'), 'Au revoir')

    def test_french_to_english(self):
        self.assertIsNone(french_to_english(None))
        self.assertEqual(french_to_english('Bonjour'), 'Hello')
        self.assertNotEqual(english_to_french('Au revoir'), 'Hello')

if __name__=='__main__':
    unittest.main()
