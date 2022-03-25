import unittest
from translator import english_to_french 
from translator import french_to_english
class TestMyModule(unittest.TestCase):
    def test_e2f1(self):
        self.assertEqual(french_to_english('Bonjour'), 'Hello')
    def test_e2f2(self):
        self.assertEqual(french_to_english('Au revoir'), 'Goodbye')
    def test_e2f3(self):
        self.assertNotEqual(french_to_english('None'), '')
    def test_e2f4(self):
        self.assertNotEqual(french_to_english(0),0)

class TestMyModule1(unittest.TestCase):
    def test_f2e1(self):
        self.assertEqual(english_to_french('Hello'), 'Bonjour')
    def test_f2e2(self):
        self.assertEqual(english_to_french('Goodbye'), 'Au revoir')
    def test_f2e3(self):
        self.assertNotEqual(english_to_french('None'), '')
    def test_f2e4(self):
        self.assertNotEqual(english_to_french(0),0)
unittest.main()