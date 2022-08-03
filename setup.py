from setuptools import setup, find_packages
import codecs
import os

VERSION = '0.0.1'
DESCRIPTION = 'Basic image manipulation and viewing in Python.'
LONG_DESCRIPTION = 'A package that allows users to easily display image effects rendered as videos on still photos.'

# Setting up
setup(
    name="artgen",
    version=VERSION,
    author="Owen Wardlaw",
    author_email="owen.wardlaw2017@gmail.com",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=['opencv-python', 'random', 'numpy'],
    keywords=['python', 'video', 'image', 'art', 'random'],
    classifiers=[
        "Development Status :: Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)