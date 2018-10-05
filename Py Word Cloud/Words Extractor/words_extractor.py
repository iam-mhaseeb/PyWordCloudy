import os


class WordsExtractor:

    """This class is responsible for exctracting & cleaning
        words from text string sent by main module and store
        dictionary of words extracted from string in
        extracted_words variable."""

    def __init__(self, input_txt):

        """This is constructor for words extractor class
            it takes text string and act as controller to
            expose text string to whole class."""

        self.extracted_words = None
        tokenized_words = self.get_tokenized_text(input_txt)
        cleaned_words = self.remove_stop_words(tokenized_words)

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
        file_path = r"Py Word Cloud/Topics Extractor/stop_words_list.txt"
        with open(file_path, "r") as stop_words_file:
            stop_words = stop_words_file.read()
            return set([word for word in tokenized_txt if word not in stop_words])
