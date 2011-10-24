# -*- coding: utf-8 *-*

import re

from droopy import op, attr

class Static(object):
    """Bundle with static text analysis"""

    PUNCTUATION = u".?!"

    @op
    def count_characters(self, d, with_white_characters):
        if with_white_characters:
            return len(d.text)
        else:
            return len(re.findall("[%s]" % (d.bigs + d.smalls), d.text))

    @attr
    def nof_characters(self, d):
        return d.count_characters(False)

    @attr
    def words(self, d):
        words_split = re.split(u"[ .,:;!?()\-+=\"\']", d.text)
        return [word.strip() for word in words_split if word.strip()]

    @attr
    def words_set(self, d):
        return set(d.words)

    @attr
    def nof_words(self, d):
        return len(d.words)

    @op
    def nof_words_longer_than(self, d, l):
        return len([ w for w in d.words if len(w) > l ])

    @attr
    def sentences(self, d):
        PUNCTUATION_RE = u"\.\?!:"
        split_by = u"[%s]+\s+[%s]" % (PUNCTUATION_RE, d.bigs)
        return re.split(split_by, d.text)

    @attr
    def nof_sentences(self, d):
        return len(d.sentences)

    @attr
    def nof_syllables(self, d):
        nof_syllables = 0
        for word in d.words:
            syllables = d.count_syllables_in_word(word)
            nof_syllables += syllables
        return nof_syllables

    @attr
    def foggy_words(self, d):
        foggy_words = []
        for word in d.words:
            if d.count_syllables_in_word(word) > d.foggy_word_syllables:
                foggy_words.append(word)
        return foggy_words

    @attr
    def nof_foggy_words(self, d):
        return len(d.foggy_words)

    @attr
    def foggy_factor(self, d):
        return float(d.nof_foggy_words) / float(d.nof_words)

