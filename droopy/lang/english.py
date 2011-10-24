
# -*- coding: utf-8 *-*

import re

from droopy import attr, op

from en_syllables_cmudict import SYLLABLES


class English(object):

    @attr
    def lang(self, d):
        return 'en_EN'

    @attr
    def vowels(self, d):
        return u"aeiouyAEIOUY"

    @attr
    def consonants(self, d):
        return u"bcdfghjklmnpqrstvwxzBCDFGHJKLMNPQRSTVWXZ"

    @attr
    def bigs(self, d):
        return u"AEIOUYBCDFGHJKLMNPQRSTVWXZ"

    @attr
    def smalls(self, d):
        return u"aeiouybcdfghjklmnpqrstvwxz"

    @op
    def count_syllables_in_word(self, d, word):
        return SYLLABLES.get(word.lower(), len(re.findall('[%s]' % d.vowels, word)))

    @attr
    def foggy_word_syllables(self, d):
        return 2

