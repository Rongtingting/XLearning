"""
xlearn - 
See: https://github.com/Rongtingting/XLearning
"""

# Always prefer setuptools over distutils
from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Set __version__ for the project.
exec(open("./xlearning/version.py").read())

# Get the long description from the relevant file
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()
    
reqs = ['numpy>=1.9.0', 'scipy>=1.4.1', 'matplotlib']
#         'tensorflow>=2.0.0', 'tensorflow-probability>=0.8.0']

setup(
    name='xlearning',

    # Versions should comply with PEP440.  For a discussion on single-sourcing
    # the version across setup.py and the project code, see
    # https://packaging.python.org/en/latest/single_source_version.html
    version=__version__,

    description='X Learning',
    long_description=long_description,

    # The project's main homepage.
    url='https://github.com/Rongtingting/XLearning',

    # Author details
    author='Authors',
    author_email='rthuang@connect.hku.hk',

    # Choose your license
    license='Apache-2.0',

    # What does your project relate to?
    keywords=['Copy Number Variation', 'allelic expression', 
              'single-cell RNA-seq', 'variantional inference'],

    # You can just specify the packages manually here if your project is
    # simple. Or you can use find_packages().
    packages=find_packages(),

    # entry_points={
    #       'console_scripts': [
    #           ],
    #       }, 

    # List run-time dependencies here.  These will be installed by pip when
    # your project is installed. For an analysis of "install_requires" vs pip's
    # requirements files see:
    # https://packaging.python.org/en/latest/requirements.html
    
    install_requires=reqs,

    extras_require={
        'docs': [
            'sphinx_bootstrap_theme']},

    py_modules = ['xlearning']

    # buid the distribution: python setup.py sdist
    # upload to pypi: 
    # python3 -m twine upload dist/*
)
