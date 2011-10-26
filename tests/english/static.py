# -*- coding: utf-8 -*-

from droopy.factory import DroopyFactory
from droopy.lang.english import English

import unittest


class EnglishStatic(unittest.TestCase):

    def setUp(self):
        self.simple = DroopyFactory.create_full_droopy(u"Just a simple test.", English())
        self.complex = DroopyFactory.create_full_droopy(u"""Moses supposes his toeses are roses
            but Moses supposes erroneously
            for nobody's toeses are posies of roses
            as Moses supposes his toeses to be...
            """, English())

    def test_characters(self):
        self.assertEquals(19, self.simple.nof_characters)
        self.assertEquals(193, self.complex.nof_characters)

    def test_letters(self):
        self.assertEquals(15, self.simple.nof_letters)
        self.assertEquals(117, self.complex.nof_letters)

    def test_syllables(self):
        self.assertEquals(5, self.simple.nof_syllables)
        self.assertEquals(44, self.complex.nof_syllables)

    def test_words(self):
        self.assertEquals(4, self.simple.nof_words)
        self.assertEquals(24, self.complex.nof_words)

    def test_sentences(self):
        self.assertEquals(1, self.simple.nof_sentences)
        self.assertEquals(1, self.complex.nof_sentences)

    def test_foggy(self):
        self.assertEquals(0, self.simple.nof_foggy_words)


