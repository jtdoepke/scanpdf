from __future__ import print_function
from setuptools import setup, find_packages

import io
import os
from scanpdf.version import __version__
from setuptools import Command


class PyTest(Command):
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        import sys, subprocess

        cwd = os.getcwd()
        os.chdir("test")
        errno = subprocess.call([sys.executable, "runtests.py"])
        os.chdir(cwd)
        raise SystemExit(errno)


def read(*filenames, **kwargs):
    encoding = kwargs.get("encoding", "utf-8")
    sep = kwargs.get("sep", "\n")
    buf = []
    for filename in filenames:
        with io.open(filename, encoding=encoding) as f:
            buf.append(f.read())
    return sep.join(buf)


packages = find_packages(exclude="tests")

long_description = read("README.rst")

with open("requirements.txt") as f:
    required = f.read().splitlines()

setup(
    name="scanpdf",
    version=__version__,
    description="Utility to use SANE/scanadf to scan to PDF",
    license="ASL 2.0",
    long_description=long_description,
    author="Virantha N. Ekanayake",
    author_email="virantha@gmail.com",  # Removed.
    package_data={"": ["*.xml"]},
    zip_safe=True,
    include_package_data=True,
    packages=packages,
    install_requires=required,
    entry_points={
        "console_scripts": ["scanpdf = scanpdf.scanpdf:main"],
    },
    options={"pyinstaller": {"packages": packages}},
    cmdclass={"test": PyTest},
)
