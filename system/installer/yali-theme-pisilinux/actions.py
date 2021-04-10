#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pythonmodules
from pisi.actionsapi import pisitools

def build():
    pisitools.dosed("setup.py", "rcc-qt5", "rcc")
    pythonmodules.compile()

def install():
    pythonmodules.install()
    
