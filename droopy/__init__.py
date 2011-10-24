# -*- coding: utf-8 -*-

import re

class Droopy(object):
    """Base class that will contain all text processors

    To perform text analysis you must create a Droopy object
    and add one or more processors suites:
    ex:
    droopy = Droopy("Some text here...")
    droopy.add_bundle(ProcessorsSuite1())
    droopy.add_bundle(ProcessorsSuite1())

    Processor suite is plain python class, where methods coresponds
    to "text processor" so each method could be understand as a
    text processor. There are two kinds of processors:
    * attributes (see attr decorator)
    * operators (see op decorator)

    """
    def __init__(self, text):
        # save text
        self.text = text
        # containers for bundles and cached values
        self.processors, self.values = {}, {}

    def add_bundles(self, *bundles):
        """Adds new bundle(s)"""
        for bundle in bundles:
            for processor in [getattr(bundle, p, None) for p in bundle.__class__.__dict__]:
                if hasattr(processor, '_proc'): # check if function is processor
                    self.processors[processor.func_name] = processor

    def clear_cache(self):
        """Clear cached values"""
        self.values = {}

    def __getattr__(self, attr):
        """Gets value of processor"""
        # operator - run
        if self.processors[attr].__class__ == op:
            return self.processors[attr](self)

        # attribute - cache value
        if not attr in self.values:
            self.values[attr] = self.processors[attr](self)
        # return cached attribute value
        return self.values[attr]


def attr(method):
    """Decorator for attributes"""
    method._proc = True
    return method

class op(object):
    """Decorator for operators"""
    def __init__(self, method):
        self._proc = True
        self.method = method
        self.func_name = method.func_name

    def __call__(self, droopy):
        def wrapper(*args):
            return self.method(self, droopy, *args)
        return wrapper


