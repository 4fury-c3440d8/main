#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import cmaketools
from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    pisitools.dosed("libproxy/cmake/modules/pacrunner_mozjs.cmk", "mozjs-68", "mozjs-78")
    cmaketools.configure("-DCMAKE_INSTALL_PREFIX=/usr \
                          -DCMAKE_SKIP_RPATH=ON \
                          -DPERL_VENDORINSTALL=yes \
                          -DCMAKE_BUILD_TYPE=Release \
                          -DWITH_WEBKIT3=ON \
                          -DWITH_VALA=yes \
                          -DWITH_MOZJS=ON")

def build():
    cmaketools.make()

def install():
    cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("README", "ChangeLog", "COPYING")
