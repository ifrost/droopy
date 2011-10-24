# -*- coding: utf-8 *-*

from droopy import attr

class TextFilter(object):

    @attr
    def clear_text(self, d):
        return d.text.replace(u':)',u'.').replace( u';)',u'.').replace(u':(',u'.').replace(u';(',u'.').replace(u':P',u'.').replace(u';P',u'.').replace(u':D',u'.').replace(u';D',u'.').replace(u'-',u' ').replace(u'*',u'').replace(u'–',' ').replace(u'”',u'').replace(u'„',u'').replace(u'"',u'')
