import unittest
import textprocessor

"""
 Module to run unit test cases on TextProcessor.py

"""

class ProcessorTestCase(unittest.TestCase):

    def test_count_alpha(self):
        text = "testing123"
        p = textprocessor.Processor(text)
        self.assertEqual(p.count_alpha(), 7, "alpha count of 'text' does not match input")

    def test_count_numeric(self):
        text = "testing123"
        p = textprocessor.Processor(text)
        self.assertEqual(p.count_numeric(), 4, "numeric count of 'text' does not match input") 

    def test_count_vowels(self):
        text = "testing123"
        p = textprocessor.Processor(text)
        self.assertEqual(p.count_vowels(), 2, " vowel count of'text' does not match input")  


# Main: Run Test Cases
if __name__ == '__main__':
    unittest.main()