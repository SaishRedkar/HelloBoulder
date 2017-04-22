import re

"""
A simple module with various Text Processing Capabilities

"""


class Processor:
    """
    Class for Processing Strings
    """

    def __init__(self, text):
        self.text = text

    def count_alpha(self):
        """
        Count number of alphabetic characters in text
        :return: Number of alphabetic characters
        """
        alpha = re.compile(r'[a-zA-Z]')
        return len(alpha.findall(self.text))

    def count_numeric(self):
        """
        Count number of numeric characters in text
        :return: Number of numeric characters
        """

        alpha = re.compile(r'[0-9]')
        return len(alpha.findall(self.text))

    def count_vowels(self):
        """
        Count number of vowels in text
        :return: Number of vowels
        """

        vowels = re.compile(r'[aeiou]', re.IGNORECASE)
        return len(vowels.findall(self.text))