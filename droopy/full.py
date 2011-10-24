# -*- coding: utf-8 *-*

from droopy import Droopy

from droopy.static import Static
from droopy.filters import TextFilter
from droopy.lang.polish import Polish
from droopy.lang.english import English
from droopy.readability import Readability

class FullDroopy(Droopy):

    def __init__(self, text):
        Droopy.__init__(self, text)
        self.add_processors(Static())
        self.add_processors(TextFilter())
        self.add_processors(Readability())

class FullPolishDroopy(FullDroopy):

    def __init__(self, text):
        FullDroopy.__init__(self, text)
        self.add_processors(Polish())

class FullEnglishDroopy(FullDroopy):

    def __init__(self, text):
        FullDroopy.__init__(self, text)
        self.add_processors(English())

