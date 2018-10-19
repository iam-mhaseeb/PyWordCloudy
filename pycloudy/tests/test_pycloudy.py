from unittest import TestCase
from pycloudy import WordCloudGenrator

class TestPyCloudy(TestCase):
    def test_is_genrate_word_cloud(self):
        wordcloud = WordCloudGenrator("A simpel text  to test word cloud.")
        self.assertTrue(isinstance(wordcloud, WordCloudGenrator))
