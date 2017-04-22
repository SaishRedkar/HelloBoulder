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
