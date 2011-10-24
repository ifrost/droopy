# -*- coding: utf-8 *-*

import re

from droopy import attr, op


class Polish(object):

    @attr
    def lang(self, d):
        return 'pl_PL'

    @attr
    def vowels(self, d):
        return u"aąeęioóuyAĄEĘIOÓUY"

    @attr
    def consonants(self, d):
        return u"bcćdfghjklłmnńpqrsśtvwxzźżBCĆDFGHJKLŁMNŃPQRSŚTVWXZŻŹ"

    @attr
    def bigs(self, d):
        return u"AĄEĘIOÓUYBCĆDFGHJKLŁMNŃPQRSŚTVWXZŻŹ"

    @attr
    def smalls(self, d):
        return u"aąeęioóuybcćdfghjklłmnńpqrsśtvwxzźż"

    @op
    def count_syllables_in_word(self, d, word):
        vowels = len(re.findall(u"[%s]{1,2}" % d.vowels, word))
        if vowels <= 1:
            syllables = vowels
        else:
            soften_consonants = len(re.findall("[%s]i[%s]" % (d.consonants, d.vowels ), word))
            syllables = vowels # - soften_consonants
        return syllables

    @attr
    def foggy_word_syllables(self, d):
        return 3

