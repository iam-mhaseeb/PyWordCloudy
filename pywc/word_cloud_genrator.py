from __future__ import absolute_import

import os
import random
import operator
from itertools import groupby
from PIL import Image, ImageDraw, ImageFont
from .words_extractor import WordsExtractor

FONT_PATH = os.environ.get("FONT_PATH", os.path.dirname(__file__), "font.ttf")


class WordCloudGenrator:

    """This class is responsible for generating image & writing
        words on image sent by Words Extractor module and
        store it on disk."""

    def __init__(self, input_txt):

        """This is constructor for word cloud generator class
            it takes text string and act as controller to
            expose text string to whole class."""

        if input_txt:
            words_extractor = WordsExtractor(input_txt)
            extracted_words = words_extractor.extracted_words
            words_freq = self.generate_frequencies(extracted_words)
            cloud_styles = self.generate_cloud_styles(words_freq)
            img = self.generate_image()
            self.word_cloud = self.generate_word_cloud(img, cloud_styles)
        else:
            raise ValueError(
                "Please pass the correct string containing your text.")

    def generate_frequencies(self, words):

        """This function generates frequencies for words
            based on number of occurences and return dictionary
            containing each word as key & frequency as value.

        Parameters
        ----------
        words: A list of cleaned words sent by Words Extractor module.
        -------
        words_frequencies: A dictionary of words & frequencies,
            word as key & frequency as value."""

        return {key: len(list(group)) for key, group in groupby(words)}

    def generate_cloud_styles(self, words_freq):

        """This function generates font size for words
            based on frequncies and return dictionary
            containing each word as key & style of text as value.

        Parameters
        ----------
        words: A dictionary of words & frequencies.
        -------
        cloud_styles: A dictionary of words & font size,
            text position, color of text, word as key & size as value."""

        sorted_words = sorted(
            words_freq.items(), key=operator.itemgetter(1), reverse=True)
        cloud_styles = {}
        font_size = 20
        max_freq = sorted_words[0][1]

        for word_freq in sorted_words:
            if word_freq[1] < max_freq and font_size > 12:
                max_freq = word_freq[1]
                font_size = int(font_size/1.5)
            fnt = ImageFont.truetype(FONT_PATH, font_size)
            width = random.randint(100, 400)
            height = random.randint(100, 300)
            r = random.randint(1, 200)
            g = random.randint(1, 200)
            b = random.randint(1, 200)
            cloud_styles[word_freq[0]] = {
                "font": fnt,
                "width": width,
                "height": height,
                "r": r, "g": g, "b": b
                }

        return cloud_styles

    def generate_image(self):

        """This function generates new blank image
            and return image object.

        Parameters
        ----------
        None
        -------
        generated_img: Newly created blank image with white background
            for further processing."""

        generated_img = Image.new("RGB", (600, 400), color=(255, 255, 255))
        return generated_img

    def generate_word_cloud(self, img, cloud_styles):

        """This function generates word cloud, save it on disk
            and return image object.

        Parameters
        ----------
        img: A blank image ready for writing.
        cloud_styles: A dictionary of words & font size,
            text position, color of text, word as key & size as value.
        -------
        word_cloud: Newly created word cloud image with words on it
            font weight representing the frequency of word."""

        img_d = ImageDraw.Draw(img)

        for word, style in cloud_styles.items():
            img_d.text((style.get("width"), style.get("height")), word,
                       font=style.get("font"),
                       fill=(style.get("r"), style.get("g"), style.get("b")))

        path_to_save = os.path.join(
            os.path.dirname(__file__), "word_cloud.png")
        img.save(path_to_save)
        return img

    def get_word_cloud(self):

        """This function return genrated word cloud
            to caller.

        Parameters
        ----------
        None
        -------
        word_cloud: Newly created word cloud image with words on it
            font weight representing the frequency of word."""

        return self.word_cloud
