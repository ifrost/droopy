# -*- coding: utf-8 -*-

from droopy.factory import DroopyFactory
from droopy.lang.english import English

import unittest


class FiltersTest(unittest.TestCase):

    def setUp(self):
        self.emots = DroopyFactory.create_full_droopy(u"Some emots :) Each emot is treated like end of sentence :P", English())
        self.non_letters = DroopyFactory.create_full_droopy(u"Text *formatted* _with_ -special chars- 123", English())

    def test_clear_emoticons(self):
        self.assertEqual(u"Some emots . Each emot is treated like end of sentence .", self.emots.without_emoticons)

    def test_clear_non_letters(self):
        self.assertEqual(u"Text  formatted   with   special chars  123", self.non_letters.without_non_alphanumeric)
