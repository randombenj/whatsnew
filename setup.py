"""
    whatsnew
    ~~~~~~~

    Creates releasenotes out of the git history
    and additional information from user input
    and saves it to the git history.
"""

from setuptools import setup, find_packages

setup(
    name='whatsnew',
    install_requires=[
        'Click',
        'git'
    ],
    test_requires=[
        'pytest'
    ],
    packages=find_packages(),
    include_package_data=True,
    entry_points={
        'console_scripts': ['whatsnew = whatsnew.__main__:cli']
    }
)
