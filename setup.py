import os

from setuptools import setup, find_packages

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "django-buildout-boilerplate",
    version = "0.1",
    url = "http://github.com/66laps/django-buildout-boilerplate",
    license = "LGPL v3",
    description = "Basic boilerplate for quickly creating redistributable Django apps.",
    long_description = read('README.rst'),
    author = "Martin Galpin",
    author_email = "m@66laps.com",
    packages = find_packages("src"),
    package_dir = { "": "src" },
    package_data = { "": ["LICENSE", "*.rst"] },
    install_requires = ["setuptools"],
    )
