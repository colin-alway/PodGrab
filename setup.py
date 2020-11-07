"""
    setup.py : Colin Alway <colin.alway@gmail.com>
    
https://docs.python.org/2/distutils/introduction.html#a-simple-example

TEST INSTALL
        sudo python setup.py -n install
INSTALL
        sudo python setup.py install
"""

from distutils.core import setup

setup(
    name='PodGrab',
    version='1.0',
    scripts=['PodGrab.py'],
    #py_modules=[''],
)
