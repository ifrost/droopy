# -*- coding: utf-8 *-*

import re

from droopy import attr, op


class TextFilter(object):

    @op
    def clear_emoticons(self, d, text):
        return text.replace(u':)',u'.').replace( u';)',u'.').replace(u':(',u'.').replace(u';(',u'.').replace(u':P',u'.').replace(u';P',u'.').replace(u':D',u'.').replace(u';D',u'.')

    @op
    def clear_non_alphanumeric(self, d, text):
        return re.sub('[^%s]' % d.alphanumeric, ' ', text)

    @attr
    def without_emoticons(self, d):
        return d.clear_emoticons(d.text)

    @attr
    def without_non_alphanumeric(self, d):
        return d.clear_non_alphanumeric(d.text)

    @attr
    def cleared(self, d):
        cleared = d.without_emoticons
        return without_non_alphanumeric(d.text)

