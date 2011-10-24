# -*- coding: utf-8 *-*

import math

from droopy import attr


class Readability(object):

    @attr
    def flesch_reading_ease(self, d):
        """Flesch Reading Ease.

        Higher score - easier to read
        90 - 100 - easily understandable by an average 11-year-old student
        60 -  70 - easily understandable by 13- to 15-year-old students
         0 -  30 - best understood by university graduates

        read more: http://en.wikipedia.org/wiki/Flesch%E2%80%93Kincaid_readability_test#Flesch_Reading_Ease

        """
        return (206.835 - 1.015*(float(d.nof_words)/d.nof_sentences) - 84.6*(float(d.nof_syllables)/d.nof_words))

    @attr
    def flesch_grade_level(self, d):
        """Flesch-Kincaid Grade Level.

        Translates 0-100 score to a US grade level

        read more: http://en.wikipedia.org/wiki/Flesch%E2%80%93Kincaid_readability_test#Flesch.E2.80.93Kincaid_Grade_Level

        """
        return(0.39*(float(d.nof_words)/d.nof_sentences) + 11.8*(float(d.nof_syllables)/d.nof_words) - 15.59)

    @attr
    def gaunning_fog_level(self, d):
        """Gaunning Fog Level.

        read more: http://en.wikipedia.org/wiki/Gunning_fog_index

        """
        return (0.4 * ((float(d.nof_words)/d.nof_sentences) + d.foggy_factor * 100 ))

    @attr
    def coleman_liau(self, d):
        """Coleman-Liau Index.

        Outputs approximate US grade level.

        read more: http://en.wikipedia.org/wiki/Coleman%E2%80%93Liau_Index

        """
        return (5.88 * (float(d.nof_characters)/d.nof_words) - 0.296 * (float(d.nof_sentences) / (float(d.nof_words)/100.0)) - 15.8)

    @attr
    def automated_readability_index(self, d):
        """Automated Readability Index (ARI)

        Produces approximate US grade level

        read more: http://en.wikipedia.org/wiki/Automated_Readability_Index

        """
        return (4.71*(float(d.nof_characters)/d.nof_words) + 0.5 * (float(d.nof_words)/d.nof_sentences) - 21.43)

    @attr
    def smog(self, d):
        """SMOG Index / SMOG Formula.

        formula that estimates the years of education needed to understand a piece of writing

        read more: http://en.wikipedia.org/wiki/SMOG_Index

        """
        return (1.043 * math.sqrt(30 * (float(d.nof_foggy_words)/d.nof_sentences)) + 3.1291)
