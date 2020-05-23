#! /usr/bin/env python
#
# Copyright (C) 2013-2015 Russell Poldrack <poldrack@stanford.edu>
# some portions borrowed from https://github.com/mwaskom/lyman/blob/master/setup.py
import os
from setuptools import setup, find_packages

descr = """autoCV: An automated CV generator"""

DISTNAME = "autoCV"
DESCRIPTION = descr
MAINTAINER = 'Russ Poldrack'
MAINTAINER_EMAIL = 'poldrack@stanford.edu'
LICENSE = 'MIT'
URL = 'http://www.poldracklab.org/'
DOWNLOAD_URL = 'https://github.com/poldrack/autoCV'
VERSION = '2020May23'


def check_dependencies():

    # Just make sure dependencies exist, I haven't rigorously
    # tested what the minimal versions that will work are
    needed_deps = [
        "pandas",
        "numpy",
        "biopython",
        "requests",
        "crossrefapi",
        "scholarly",
        "pypatent",
        "pytest"]
    missing_deps = []
    for dep in needed_deps:
        try:
            __import__(dep)
        except ImportError:
            missing_deps.append(dep)

    if missing_deps:
        missing = (", ".join(missing_deps))
        raise ImportError("Missing dependencies: %s" % missing)


if __name__ == "__main__":

    if os.path.exists('MANIFEST'):
        os.remove('MANIFEST')

    import sys
    if not (len(sys.argv) >= 2 and ('--help' in sys.argv[1:] or
            sys.argv[1] in ('--help-commands',
                            '--version',
                            'egg_info',
                            'clean'))):
        check_dependencies()

    setup(name=DISTNAME,
          maintainer=MAINTAINER,
          maintainer_email=MAINTAINER_EMAIL,
          description=DESCRIPTION,
          license=LICENSE,
          version=VERSION,
          url=URL,
          download_url=DOWNLOAD_URL,
          packages=find_packages(),
          scripts=[
              'bin/make_cv.py'],
          classifiers=[
              'Intended Audience :: Science/Research',
              'Programming Language :: Python :: 3.6',
              'License :: OSI Approved :: BSD License',
              'Operating System :: POSIX',
              'Operating System :: Unix',
              'Operating System :: MacOS'])