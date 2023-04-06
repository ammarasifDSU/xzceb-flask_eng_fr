import unittest
from translator import englishToFrench, frenchToEnglish

class TestLanguageTranslator(unittest.TestCase):
    
    def test_englishToFrench(self):
        self.assertEqual(englishToFrench('Hello'), 'Bonjour')
        self.assertEqual(englishToFrench('How are you?'), 'Comment allez-vous?')
    
    def test_frenchToEnglish(self):
        self.assertEqual(frenchToEnglish('Bonjour'), 'Hello')
        self.assertEqual(frenchToEnglish('Comment allez-vous?'), 'How are you?')
    
    def test_translation_hello_bonjour(self):
        self.assertEqual(englishToFrench('Hello'), 'Bonjour')
        self.assertEqual(frenchToEnglish('Bonjour'), 'Hello')
    
    def test_translation_bonjour_hello(self):        
        self.assertEqual(frenchToEnglish('Bonjour'), 'Hello')
        self.assertEqual(englishToFrench('Hello'), 'Bonjour')

if __name__ == '__main__':
    unittest.main()