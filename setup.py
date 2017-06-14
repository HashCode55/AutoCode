# -*- coding: utf-8 -*-


"""setup.py: setuptools control."""


import re
from setuptools import setup


version = re.search(
    '^__version__\s*=\s*"(.*)"',
    open('autocode/run.py').read(),
    re.M
    ).group(1)

with open("README.rst", "rb") as f:
    long_descr = f.read().decode("utf-8")


setup(
    name = "autocode",
    packages = ["autocode"],
    entry_points = {
        "console_scripts": ['autocode = autocode.run:main']
        },
    version = version,
    description = "Python command line application bare bones template.",
    long_description = long_descr,
    author = "Mehul Ahuja (hashcode55)",
    author_email = "blackdragon0909@gmail.com",
    url = "http://gehrcke.de/2014/02/distributing-a-python-command-line-application",
    )
