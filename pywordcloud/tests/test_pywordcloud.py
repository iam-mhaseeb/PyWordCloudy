from unittest import TestCase
from pywordcloud import WordCloudGenrator

class TestPyWordCloud(TestCase):
    def test_is_genrate_word_cloud(self):
        wordcloud = WordCloudGenrator("A simpel text  to test word cloud.")
        self.assertTrue(isinstance(wordcloud, WordCloudGenrator))
