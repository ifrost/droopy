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
        double_o = len(re.findall(u"oo", word))
        syllables = vowels + double_o
        return syllables

    @attr
    def foggy_word_syllables(self, d):
        return 3

