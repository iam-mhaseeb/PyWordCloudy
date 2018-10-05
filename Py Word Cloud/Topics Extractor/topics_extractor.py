import os


class TopicsExtractor:

    """This class is responsible for exctracting concepts
        from text string sent by main module and return
        dictionary of topics extracted from string."""

    def __init__(self, input_txt):

        """This is constructor for topics extractor class
            it takes text string and act as controller to
            expose text string to whole class."""

        input_txt = input_txt
        tokenized_txt = self.get_tokenized_text(self.input_text)

    def get_tokenized_text(self, input_text):

        """This function does tokenization of text string
            and return tokenized words as list.

        Parameters
        ----------
        text string : iterable of characters(string).
        Returns
        -------
        tokenized text : list of strings each string
            representing a word.
        """

        return input_txt.split()
