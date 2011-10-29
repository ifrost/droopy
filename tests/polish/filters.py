# -*- coding: utf-8 -*-

from droopy.factory import DroopyFactory
from droopy.lang.polish import Polish

import unittest


class FilersTest(unittest.TestCase):

    def setUp(self):
        self.emots = DroopyFactory.create_full_droopy(u"Kilka emotek :) Każda emotka jest trakowana jak koniec zdania :P", Polish())
        self.non_letters = DroopyFactory.create_full_droopy(u"Tekst *formatowany* _specjalnymi_ -znakami- $ąę$", Polish())

    def test_clear_emoticons(self):
        self.assertEqual(u"Kilka emotek . Każda emotka jest trakowana jak koniec zdania .", self.emots.without_emoticons)

    def test_clear_non_letters(self):
        self.assertEqual(u"Tekst  formatowany   specjalnymi   znakami   ąę ", self.non_letters.without_non_alphanumeric)


