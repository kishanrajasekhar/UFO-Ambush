#This module helps convert script.py into an executable file (script.exe)

from distutils.core import setup
import py2exe

setup(windows = ['script.py'])
