# -*- coding: utf-8 -*-
"""Example shows how to create bundle that will override some processors"""

from droopy import attr
from droopy.factory import DroopyFactory
from droopy.lang.english import English

class OverrideBundle(object):

    @attr
    def nof_words(self, droopy):
        return 200

droopy = DroopyFactory.create_full_droopy("Just a simple test.", English())

print "Original number of words:", droopy.nof_words
print "Original Coleman-Liau index:", droopy.coleman_liau # index uses nof_words processor

droopy.add_bundles(OverrideBundle())

print "After override number of words (cached):", droopy.nof_words
print "After override Coleman-Liau index (cached):", droopy.coleman_liau

droopy.clear_cache()

print "After override number of words (cached cleared):", droopy.nof_words
print "After override Coleman-Liau index (cache cleared):", droopy.coleman_liau # will use overriden nof_words processor

