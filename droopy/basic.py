# -*- coding: utf-8 *-*

import re

from droopy import op, attr

class Basic(object):
    """Bundle with basic data"""

    @attr
    def digits(self, d):
        return "01234567890"

    @attr
    def alphanumeric(self, d):
        return d.digits + d.smalls + d.bigs

