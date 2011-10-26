# -*- coding: utf-8 -*-

from droopy.factory import DroopyFactory
from droopy.lang.polish import Polish

import unittest


class PolishStatic(unittest.TestCase):

    def setUp(self):
        self.simple = DroopyFactory.create_full_droopy(u"Tylko prosty test", Polish())
        self.dots = DroopyFactory.create_full_droopy(u"To tylko test... wielokropka!", Polish())
        self.ogonki = DroopyFactory.create_full_droopy(u"Gżegżółka to gatunek kukułki, który na terenie Polski objęty jest ścisłą ochroną gatunkową.", Polish())
        self.syllables = DroopyFactory.create_full_droopy(u"Niebieskooki dwudziestiopięciolatek", Polish())

    def test_characters(self):
        self.assertEquals(17, self.simple.nof_characters)
        self.assertEquals(29, self.dots.nof_characters)
        self.assertEquals(91, self.ogonki.nof_characters)

    def test_letters(self):
        self.assertEquals(15, self.simple.nof_letters)
        self.assertEquals(22, self.dots.nof_letters)
        self.assertEquals(77, self.ogonki.nof_letters)

    def test_syllables(self):
        self.assertEquals(5, self.simple.nof_syllables)
        self.assertEquals(5, self.simple.count_syllables_in_word("dalekowzroczny"))
        self.assertEquals(8, self.dots.nof_syllables)
        self.assertEquals(12, self.syllables.nof_syllables)

    def test_words(self):
        self.assertEquals(3, self.simple.nof_words)
        self.assertEquals(4, self.dots.nof_words)

    def test_sentences(self):
        self.assertEquals(1, self.simple.nof_sentences)
        self.assertEquals(1, self.dots.nof_sentences)

    def test_foggy(self):
        self.assertEquals(0, self.simple.nof_foggy_words)
        self.assertEquals(1, self.dots.nof_foggy_words)


