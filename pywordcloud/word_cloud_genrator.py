from __future__ import absolute_import

import os
import random
import inspect
import operator
from itertools import groupby
from PIL import Image, ImageDraw, ImageFont
from words_extractor import WordsExtractor  # TODO: Make it .words_extractor

FONT_PATH = os.path.join(os.path.dirname(__file__), "font.ttf")


class WordCloudGenrator:

    """This class is responsible for generating image & writing
        words on image sent by Words Extractor module and
        store it on disk."""

    def __init__(self, input_txt):

        """This is constructor for word cloud generator class
            it takes text string and act as controller to
            expose text string to whole class."""

        if input_txt:
            self.img_path = os.path.dirname(
                os.path.abspath((inspect.stack()[1])[1]))
            words_extractor = WordsExtractor(input_txt)
            extracted_words = words_extractor.extracted_words
            words_freq = self.generate_frequencies(extracted_words)
            img = self.generate_image()
            cloud_styles = self.generate_cloud_styles(words_freq, img)
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

    def generate_cloud_styles(self, words_freq, img):

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
        font_size = 30
        max_freq = sorted_words[0][1]
        dimens = []

        for word_freq in sorted_words:
            if word_freq[1] < max_freq and font_size > 12:
                max_freq = word_freq[1]
                font_size = int(font_size/1.5)
            fnt = ImageFont.truetype(FONT_PATH, font_size)
            # TODO: Write text on new img paste new image on word cloud
            dimens_set = False
            while not dimens_set:
                width = random.randint(50, 400)
                height = random.randint(10, 350)

                for dimen in dimens:
                    if dimen[0]-5 <= width <= dimen[0]+10:
                        break
                    if dimen[1]-30 <= height <= dimen[1]+30:
                        break

                else:
                    dimens_set = True

            dimens.append([width, height])
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

        img.save(self.img_path+"/word_cloud.png")
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


test_txt = """Pakistan[b] (Urdu: پاکِستان‬‎), officially the Islamic Republic of Pakistan (Urdu: اِسلامی جمہوریہ پاکِستان‬‎), is a country in South Asia. It is the fifth-most populous country with a population exceeding 212,742,631 people.[19] In area, it is the 33rd-largest country, spanning 881,913 square kilometres (340,509 square miles). Pakistan has a 1,046-kilometre (650-mile) coastline along the Arabian Sea and Gulf of Oman in the south and is bordered by India to the east, Afghanistan to the west, Iran to the southwest, and China in the far northeast. It is separated narrowly from Tajikistan by Afghanistan's Wakhan Corridor in the northwest, and also shares a maritime border with Oman.

The territory that now constitutes Pakistan was the site of several ancient cultures, including the Mehrgarh of the Neolithic and the Bronze Age Indus Valley Civilisation, and was later home to kingdoms ruled by people of different faiths and cultures, including Hindus, Indo-Greeks, Muslims, Turco-Mongols, Afghans, and Sikhs. The area has been ruled by numerous empires and dynasties, including the Persian Achaemenid Empire, Alexander III of Macedon, the Seleucid Empire, the Indian Maurya Empire, the Gupta Empire,[26] the Arab Umayyad Caliphate, the Delhi Sultanate, the Mongol Empire, the Mughal Empire, the Afghan Durrani Empire, the Sikh Empire (partially), and, most recently, the British Empire.

Pakistan is the only country to have been created in the name of Islam.[27][28] As a result of the Pakistan Movement led by Muhammad Ali Jinnah and the Indian subcontinent's struggle for independence, the sovereign state of Pakistan was created in 1947 as an independent homeland for Indian Muslims.[29] It is an ethnically and linguistically diverse country, with a similarly diverse geography and wildlife. Initially a dominion, Pakistan adopted a constitution in 1956, becoming an Islamic republic. An ethnic civil war in 1971 resulted in the secession of East Pakistan as the new country of Bangladesh.[30] In 1973 Pakistan adopted a new constitution establishing, alongside its pre-existing parliamentary republic status, a federal government based in Islamabad consisting of four provinces and three federal territories. The new constitution also stipulated that all laws are to conform to the injunctions of Islam as laid down in the Quran and Sunnah.[31]

A regional[32][33][34] and middle power,[35][36][37] Pakistan has the sixth-largest standing armed forces in the world and is also a nuclear power as well as a declared nuclear-weapons state, the second in South Asia and the only nation in the Muslim world to have that status. Pakistan has a semi-industrialised economy with a well-integrated agriculture sector and a growing services sector.[38][39] The Pakistani economy is the 24th-largest in the world in terms of purchasing power and the 41st-largest in terms of nominal GDP (World Bank). It is ranked among the emerging and growth-leading economies of the world,[40][41] and is backed by one of the world's largest and fastest-growing middle class.[42][43]

Pakistan's political history since independence has been characterized by periods of military rule, political instability and conflicts with India. The country continues to face challenging problems, including overpopulation, terrorism, poverty, illiteracy, and corruption.[44][45][46][47] Pakistan is a member of the United Nations, the Shanghai Cooperation Organisation, the Non-Aligned Movement, the Organisation of Islamic Cooperation, the Commonwealth of Nations, the Economic Cooperation Organisation, the South Asian Association for Regional Cooperation, the Developing Eight, and the G20 developing nations, Group of 24, Group of 77, and ECOSOC. It is also an associate member of CERN. Pakistan is a signatory to the Kyoto Protocol, the Paris Agreement, and the International Covenant on Civil and Political Rights."""

word_cloud = WordCloudGenrator(input_txt=test_txt)