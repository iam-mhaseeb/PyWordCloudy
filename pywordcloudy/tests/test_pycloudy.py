from unittest import TestCase
from pywordcloudy import WordCloudGenrator

class TestPyWordCloudy(TestCase):
    def test_is_genrate_word_cloud(self):
        wordcloud = WordCloudGenrator("A simpel text  to test word cloud.")
        self.assertTrue(isinstance(wordcloud, WordCloudGenrator))
