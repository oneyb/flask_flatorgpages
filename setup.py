#!/usr/bin/env python
#

DESCRIPTION = "Hacky org-mode parsing for Flask-Flatpages"
LONG_DESCRIPTION = """\
Hacky org-mode parsing for Flask-Flatpages
"""

DISTNAME = 'flask_flatorgpages'
MAINTAINER = 'Brian J. Oney'
MAINTAINER_EMAIL = 'brian.j.oney@gmail.com'
URL = 'https://github.com/oneyb/flask_flatorgpages'
LICENSE = 'GPLv2'
DOWNLOAD_URL = 'https://github.com/oneyb/flask_flatorgpages'
VERSION = '0.1'

try:
    from setuptools import setup
    _has_setuptools = True
except ImportError:
    from distutils.core import setup


if __name__ == "__main__":

    install_requires = []

    setup(name=DISTNAME,
          author=MAINTAINER,
          author_email=MAINTAINER_EMAIL,
          maintainer=MAINTAINER,
          maintainer_email=MAINTAINER_EMAIL,
          description=DESCRIPTION,
          long_description=LONG_DESCRIPTION,
          license=LICENSE,
          url=URL,
          version=VERSION,
          download_url=DOWNLOAD_URL,
          install_requires=install_requires,
          entry_points = {
          },
          packages=['flask_flatorgpages'],
          classifiers=[
              'Intended Audience :: Entrepreneurial/Inventory',
              'Programming Language :: Python :: 2.7',
              'Programming Language :: Python :: 3.3',
              'Programming Language :: Python :: 3.4',
              'License :: OSI Approved :: GPLv2 License',
              'Topic :: Multimedia :: Graphics',
              'Operating System :: POSIX',
              'Operating System :: Unix',
              'Operating System :: MacOS'],
    )
