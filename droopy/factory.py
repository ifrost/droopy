# -*- encoding: utf-8 -*-

from droopy import Droopy

from droopy.basic import Basic
from droopy.static import Static
from droopy.readability import Readability
from droopy.filters import TextFilter

class DroopyFactory(object):

    @staticmethod
    def create_full_droopy(text, lang_bundle=None):
        """Creates droopy with all available bundles"""
        # all available bundles
        droopy = Droopy(text)
        for bundle in DroopyFactory.get_all_available_bundles():
            droopy.add_bundles(bundle)

        # add provided language bundle
        if lang_bundle:
            droopy.add_bundles(lang_bundle)

        return droopy

    @staticmethod
    def get_all_available_bundles():
        return [Basic(), Static(), Readability(), TextFilter()]
