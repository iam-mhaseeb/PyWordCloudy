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
        tokenized_txt = self.get_tokenized_text(self.input_txt)

    def get_tokenized_text(self, input_txt):

        """This function does tokenization of text string
            and return tokenized words as list.

        Parameters
        ----------
        input_txt : iterable of characters(string).
        Returns
        -------
        tokenized text : list of strings each string
            representing a word.
        """

        return input_txt.split()

    def remove_stop_words(self, tokenized_txt):

        """This function removes stop words from tokenized
            words list and return remaining words as list.

        Parameters
        ----------
        tokenized_txt : iterable of tokenized string.
        Returns
        -------
        cleaned text : list of cleaned non stop words strings
             each string representing a word.
        """

        with open(("stop_words_list.txt"), "r") as stop_words_file:
            stop_words = stop_words_file.read()
            return [word for word in tokenized_txt if word not in stop_words]
