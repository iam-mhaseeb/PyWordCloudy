import os
import random
import operator
from itertools import groupby
from words_extractor import WordsExtractor
from PIL import Image, ImageDraw, ImageFont


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
        font_path = os.path.join(os.path.dirname(__file__), "font.ttf")
        max_freq = sorted_words[0][1]

        for word_freq in sorted_words:
            if word_freq[1] < max_freq and font_size > 12:
                max_freq = word_freq[1]
                font_size = int(font_size/1.5)
            fnt = ImageFont.truetype(font_path, font_size)
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


wrod_cloud = WordCloudGenrator("""This article is about the academic discipline. For a general history of human beings, see History of the world. For other uses, see History (disambiguation).

Historia, 1892 painting by Nikolaos Gyzis
Those who cannot remember the past are condemned to repeat it.[1]
—George Santayana
History (from Greek ἱστορία, historia, meaning "inquiry, knowledge acquired by investigation")[2] is the study of the past as it is described in written documents.[3][4] Events occurring before written record are considered prehistory. It is an umbrella term that relates to past events as well as the memory, discovery, collection, organization, presentation, and interpretation of information about these events. Scholars who write about history are called historians.

History can also refer to the academic discipline which uses a narrative to examine and analyse a sequence of past events, and objectively determine the patterns of cause and effect that determine them.[5][6] Historians sometimes debate the nature of history and its usefulness by discussing the study of the discipline as an end in itself and as a way of providing "perspective" on the problems of the present.[5][7][8][9]

Stories common to a particular culture, but not supported by external sources (such as the tales surrounding King Arthur), are usually classified as cultural heritage or legends, because they do not show the "disinterested investigation" required of the discipline of history.[10][11] Herodotus, a 5th-century BC Greek historian is considered within the Western tradition to be the "father of history", and, along with his contemporary Thucydides, helped form the foundations for the modern study of human history. Their works continue to be read today, and the gap between the culture-focused Herodotus and the military-focused Thucydides remains a point of contention or approach in modern historical writing. In East Asia, a state chronicle, the Spring and Autumn Annals was known to be compiled from as early as 722 BC although only 2nd-century BC texts survived.

Ancient influences have helped spawn variant interpretations of the nature of history which have evolved over the centuries and continue to change today. The modern study of history is wide-ranging, and includes the study of specific regions and the study of certain topical or thematical elements of historical investigation. Often history is taught as part of primary and secondary education, and the academic study of history is a major discipline in university studies.""")