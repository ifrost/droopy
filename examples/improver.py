# -*- coding: utf-8 -*-
"""Example shows how Droopy could be use for readability improving mechanism"""

from droopy import Droopy
from droopy.factory import DroopyFactory
from droopy.lang.english import English


class Improver(Droopy):
    """Object that will improve readability of text"""

    def __init__(self, *args, **kwargs):
        Droopy.__init__(self, *args, **kwargs)
        self.add_bundles(*DroopyFactory.get_all_available_bundles())
        self.add_bundles(English())

    def improve(self):
        for word in self.foggy_words:
            self.text = self.text.replace(word, "buzz")
        # clear values after improving
        self.clear_cache()


d = Improver("Text with some complicated words like onomatopoeia or carboxylation which not everyone can understand")
print "Orignal text:", d.text
print "SMOG index:", d.smog
print "---"

d.improve()
print "Improved text:", d.text
print "SMOG index:", d.smog

