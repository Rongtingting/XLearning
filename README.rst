|PyPI| |Docs| 

.. |PyPI| image:: https://img.shields.io/pypi/v/xlearning.svg
    :target: https://pypi.org/project/xlearning
.. |Docs| image:: https://readthedocs.org/projects/xlearning/badge/?version=latest
   :target: https://xlearning.readthedocs.io

  
XLearning
===========


A small library of machine learning models and utility & plotting functions:

1. a set of utility functions, e.g., wrap function for cross-validation on 
   regression and classification models

2. a set of small models, e.g., mixture of linear regression model

3. a set of plotting functions in X-Projects, e.g., `heatmap`.


How to install?
---------------

Easy install with *pip* by ``pip install xlearning`` for released version or the 
latest version on github (less stable though).

xlearning is available through `pypi`_. To install, type the following command 
line, and add ``-U`` for upgrading:

.. code-block:: bash

  pip install -U xlearning

Alternatively, you can install from this GitHub repository for latest (often 
development) version by following command line

.. code-block:: bash

  pip install -U git+https://github.com/Rongtingting/XLearning

In either case, if you don't have write permission for your current Python 
environment, add ``--user``, but check the previous section on create your own
conda environment.

.. _pypi: https://pypi.org/project/xlearning

To remove the package, type the following command line,

.. code-block:: bash

  pip uninstall xlearning


Documentation
-------------

See the documentation_ for how to use, e.g., `cross-validation`_ and 
`plotting functions`_.

.. _documentation: https://xlearning.readthedocs.io
.. _`cross-validation`: https://xlearning.readthedocs.io/en/latest/cross_validation.html
.. _`plotting functions`: https://hilearn.readthedocs.io/en/latest/plotting.html