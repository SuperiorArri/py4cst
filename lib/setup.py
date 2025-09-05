from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '0.1.10'
DESCRIPTION = 'Automation/Scripting library for CST Studio Suite'
LONG_DESCRIPTION = 'For more information, please visit the GitHub repository: https://github.com/Arri0/py4cst'

# Setting up
setup(
    name="py4cst",
    version=VERSION,
    author="Samuel Travnicek",
    author_email="<travnsam@fel.cvut.cz>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=['numpy', 'parse', 'matplotlib', 'typing'],
    keywords=['python', 'CST Studio Suite', 'Automation', 'Electromagnetic Field', 'Simulation'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        # "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)