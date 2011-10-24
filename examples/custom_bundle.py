# -*- coding: utf-8 -*-
"""Example show how to create own bundles"""

from droopy import Droopy, attr, op
from droopy.static import Static

import re


class WhiteBundle(object):

    @attr
    def without_whitespace_characters(self, d):
        return re.sub('\s', '', d.text)

    @attr
    def count_whitespace_characters(self, d):
        return len(re.findall(' ', d.text))

    @op
    def join_words(self, d, joiner):
        return joiner.join(d.words)

TEXT = """ Example text
    with        some
    whitespace characters
    """

d = Droopy(TEXT)
d.add_bundles(Static(), WhiteBundle())

print "Original text:", d.text
print "---"
print "Text without whitespace characters:", d.without_whitespace_characters
print "---"
print "There are %s whitespce characters in text" % (d.count_whitespace_characters,)
print "---"
print "Orignal text does not change:", d.text
print "---"
print "Join words with space:", d.join_words(' ')

