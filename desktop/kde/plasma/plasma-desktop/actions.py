#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import kde5
from pisi.actionsapi import pisitools

def setup():
    #shelltools.system("rm -rf po/id")
    kde5.configure("-DCMAKE_INSTALL_PREFIX=/usr \
                    -DCMAKE_INSTALL_LIBDIR=lib \
                    -DBUILD_TESTING=OFF")

def build():
    kde5.make()

def install():
    kde5.install()

    pisitools.dodoc("LICENSES/*")
