# -*- coding: utf-8 *-*

import os
from setuptools import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name="droopy",
    version="0.0.3",
    author="Piotr Jamroz",
    author_email="pm.jamroz@gmail.com",
    description="Little library for text analysis",
    license="MIT",
    keywords="text analysis readability",
    packages=['droopy', 'droopy.lang', 'tests'],
    test_suite='tests',
    url="https://github.com/ifrost/droopy",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Topic :: Utilities",
    ],
)
