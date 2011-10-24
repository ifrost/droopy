# -*- coding: utf-8 -*-
"""Example shows basic usage of Droopy"""

from droopy.factory import DroopyFactory
from droopy.lang.polish import Polish

d = DroopyFactory.create_full_droopy(u"""
            Znudzony ciszą, idzie pomiędzy czeladkę;
            Woli w kuchennej słuchać ochmistrzyni krzyków,
            Gróźb i razów kucharza, hałasu kuchcików:
            Aż go powoli wprawił w przyjemne marzenie,
            Ruch jednostajny rożnów kręcących pieczenie.
            """, Polish())

print 'text:', d.text
print 'syllables:', d.nof_syllables
print 'words:', d.nof_words
print 'sentences:', d.nof_sentences
print 'words longer than 2 characters:', d.nof_words_longer_than(2)
print 'foggy words:', d.nof_foggy_words
print 'foggy factor:', d.foggy_factor
print 'flesch reading ease:', d.flesch_reading_ease
print 'flesch grade level:', d.flesch_grade_level
print 'coleman liau index:', d.coleman_liau
print 'automated readability index:', d.automated_readability_index
print 'SMOG index:', d.smog
