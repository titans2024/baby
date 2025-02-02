#!/usr/bin/env python

import os
import glob
from setuptools import setup

VERSION = "0.0.1"


def find_data_files(source, target, patterns):
    """
    Locates the specified data-files and returns the matches
    in a data_files compatible format.

    source is the root of the source data tree.
        Use '' or '.' for current directory.
    target is the root of the target data tree.
        Use '' or '.' for the distribution directory.
    patterns is a sequence of glob-patterns for the
        files you want to copy.
    """
    if glob.has_magic(source) or glob.has_magic(target):
        raise ValueError("Magic not allowed in src, target")
    ret = {}
    for pattern in patterns:
        pattern = os.path.join(source, pattern)
        for filename in glob.glob(pattern):
            if os.path.isfile(filename):
                targetpath = os.path.join(
                    target, os.path.relpath(filename, source)
                )
                path = os.path.dirname(targetpath)
                ret.setdefault(path, []).append(filename)
    return sorted(ret.items())


with open('README.rst') as f:
    LONG_DESCR = f.read()


setup(
    name='Baby',
    version=VERSION,
    description='All Basic sorting and search',
    long_description=LONG_DESCR,
    author='Muthukumaran',
    author_email='titansmuthu@gmail.com',
    url='https://github.com/titans2024/easy.git',
    download_url='https://github.com/titans2024/easy/archive/refs/heads/main.zip',
    # packages=find_packages(),
    license='MIT License',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Environment :: Console',
        'Intended Audience :: End Users/Desktop',
        'Intended Audience :: Manufacturing',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Topic :: Multimedia :: Graphics :: 3D Modeling',
    ],
    keywords='Easy sorting and search',
    entry_points={
        'console_scripts': ['mandoline=mandoline:main'],
    },
    install_requires=[
        'setuptools',
        're',
        
    ],
    extras_require={
        "dev":["pytest>=7.0","twine>=4.0.2"],
    },
    python_requires=">=3.10",
)
