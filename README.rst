======================
Stemcode
======================

.. image:: https://pyup.io/repos/github/grnydawn/stemcode/shield.svg
     :target: https://pyup.io/repos/github/grnydawn/stemcode/
     :alt: Updates

.. image:: https://travis-ci.org/grnydawn/stemcode.svg?branch=master
    :target: https://travis-ci.org/grnydawn/stemcode     

Stemcode_ template for a Python package.

* GitHub repo: https://github.com/grnydawn/stemcode/
* Documentation: https://stemcode.readthedocs.io/
* Free software: MIT license

Features
--------

.. * Testing setup with ``unittest`` and ``python setup.py test`` or ``py.test``
.. * Travis-CI_: Ready for Travis Continuous Integration testing
.. * Tox_ testing: Setup to easily test for Python 2.7, 3.4, 3.5, 3.6
.. * Sphinx_ docs: Documentation ready for generation with, for example, ReadTheDocs_
.. * Bumpversion_: Pre-configured version bumping with a single command
.. * Auto-release to PyPI_ when you push a new tag to master (optional)
.. * Command line interface using Click (optional)

.. _Stemcode: https://github.com/grnydawn/stemcode

Build Status
-------------

Linux:

.. image:: https://img.shields.io/travis/grnydawn/stemcode.svg
    :target: https://travis-ci.org/grnydawn/stemcode
    :alt: Linux build status on Travis CI

Windows:

.. image:: https://ci.appveyor.com/api/projects/status/github/grnydawn/stemcode?branch=master&svg=true
    :target: https://ci.appveyor.com/project/grnydawn/stemcode/branch/master
    :alt: Windows build status on Appveyor

Quickstart
----------

Install the latest Stemcode if you haven't installed it yet (this requires
Stemcode 0.1.0 or higher)::

    pip install -U stemcode

Generate a Python package project::

    stemcode https://github.com/grnydawn/stemcode.git

Then:

* Create a repo and put it there.
* Add the repo to your Travis-CI_ account.
* Install the dev requirements into a virtualenv. (``pip install -r requirements_dev.txt``)
* Register_ your project with PyPI.
* Run the Travis CLI command `travis encrypt --add deploy.password` to encrypt your PyPI password in Travis config
  and activate automated deployment on PyPI when you push a new tag to master branch.
* Add the repo to your ReadTheDocs_ account + turn on the ReadTheDocs service hook.
* Release your package by pushing a new tag to master.
* Add a `requirements.txt` file that specifies the packages you will need for
  your project and their versions. For more info see the `pip docs for requirements files`_.
* Activate your project on `pyup.io`_.

.. _`pip docs for requirements files`: https://pip.pypa.io/en/stable/user_guide/#requirements-files
.. _Register: https://packaging.python.org/distributing/#register-your-project

For more details, see the `stemcode tutorial`_.

.. _`stemcode tutorial`: https://stemcode.readthedocs.io/en/latest/tutorial.html

.. _Travis-CI: http://travis-ci.org/
.. _Tox: http://testrun.org/tox/
.. _Sphinx: http://sphinx-doc.org/
.. _ReadTheDocs: https://readthedocs.io/
.. _`pyup.io`: https://pyup.io/
.. _Bumpversion: https://github.com/peritus/bumpversion
.. _Punch: https://github.com/lgiordani/punch
.. _PyPi: https://pypi.python.org/pypi

.. _`Nekroze/stemcode`: https://github.com/Nekroze/stemcode
.. _`tony/stemcode-pythonic`: https://github.com/tony/stemcode-pythonic
.. _`ardydedase/stemcode`: https://github.com/ardydedase/stemcode
.. _`lgiordani/stemcode`: https://github.com/lgiordani/stemcode
.. _github comparison view: https://github.com/tony/stemcode-pythonic/compare/grnydawn:master...master
.. _`network`: https://github.com/grnydawn/stemcode/network
.. _`family tree`: https://github.com/grnydawn/stemcode/network/members
