##!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import mesontools
from pisi.actionsapi import pisitools

def setup():
    mesontools.configure()

def build():
    mesontools.build()
    
def install():
    mesontools.install()

    #dirs = ["/usr/share/doc", "/usr/share/devhelp"]
    #for dir in dirs:
        #pisitools.removeDir(dir)

    pisitools.dodoc("ChangeLog", "COPYING*", "NEWS", "README")
