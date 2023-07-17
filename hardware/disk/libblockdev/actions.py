#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

shelltools.export("PYTHON", "/usr/bin/python3")

def setup():
    # shelltools.system("sed 's/g_memdup/&2/' -i             \
                            # src/lib/plugin_apis/vdo.{c,api} \
                            # src/plugins/vdo.c")

    # shelltools.system("sh ./autogen.sh")
    autotools.autoreconf("-ivf")
    # shelltools.system("sed -i 's|python2-config|python2.7-config|g' configure")
    autotools.configure("--without-gtk-doc \
                         --without-nvdimm \
                         --with-python3 \
                         --without-dm")
    
    pisitools.dosed("libtool", " -shared ", " -Wl,-O1,--as-needed -shared ")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    
    #pisitools.domove("/gi/overrides/BlockDev.py", "/usr/lib/python2.7/site-packages/gi/overrides")
    #pisitools.removeDir("/gi")

    pisitools.dodoc("LICENSE")
