import os


class TopicsExtractor:

    """This class is responsible for exctracting concepts
    from text file read by main module and return dictionary
    of topics extracted from file."""

    def __init__(self, text_input_file):

        """This is constructor for topics extractor class
        it takes text input file and expose it to whole class."""

        self.text_input_file = text_input_file
