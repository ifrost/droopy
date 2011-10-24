# -*- coding: utf-8 -*-

from droopy.factory import DroopyFactory
from droopy.lang.english import English

import unittest


class EnglishStatic(unittest.TestCase):

    def setUp(self):
        self.simple = DroopyFactory.create_full_droopy(u"Just a simple test.", English())

    def test_syllables(self):
        self.assertEquals(5, self.simple.nof_syllables)

    def test_words(self):
        self.assertEquals(4, self.simple.nof_words)

    def test_sentences(self):
        self.assertEquals(1, self.simple.nof_sentences)

    def test_foggy(self):
        self.assertEquals(0, self.simple.nof_foggy_words)


