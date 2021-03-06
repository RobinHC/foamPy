#!/usr/bin/env python
# coding=utf-8

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup
from foampy import __version__

setup(
    name="foamPy",
    version=__version__,
    author="Pete Bachant",
    author_email="petebachant@gmail.com",
    packages=["foampy", "foampy.tests"],
    scripts=["scripts/foampy-progress-gui",
             "scripts/foampy-progress",
             "scripts/foampy-load-surfaces",
             "scripts/pvloadsurf.py",
             "scripts/foampy-reformat-foildata",
             "scripts/foampy-mirror-foildata",
             "scripts/foampy-gitignore",
             "scripts/foampy-make-template"],
    url="https://github.com/petebachant/foamPy.git",
    license="MIT",
    description="Python package for working with OpenFOAM.",
    long_description=open("README.md").read(),
    install_requires=[],
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Science/Research",
        "Natural Language :: English",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.3",
        "Topic :: Scientific/Engineering :: Physics"],
)
