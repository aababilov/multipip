#!/usr/bin/python
# vim: tabstop=4 shiftwidth=4 softtabstop=4

import os
from setuptools import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name="multipip",
    version="0.1",
    licence="Apache License (2.0)",
    description="multipip and py2rpm",
    long_description=read("README.rst"),
    author="Alessio Ababilov",
    author_email="ilovegnulinux@gmail.com",
    url="https://github.com/aababilov/multipip",
    scripts=[
        "multipip",
        "py2rpm",
    ],
    packages=[],
    py_modules=[],
    install_requires=read("requirements.txt")
)
