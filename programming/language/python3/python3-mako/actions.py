#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import get
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import pythonmodules

shelltools.export("PYTHONDONTWRITEBYTECODE", "1")

WorkDir = "Mako-%s" % get.srcVERSION()

def build():
    pythonmodules.compile(pyVer="3")

def install():
    shelltools.system('sed -i "s:mako-render:&3:g" setup.py')
    pythonmodules.install(pyVer="3")

    #pisitools.dodoc("doc/*.txt")
    pisitools.dohtml("doc/*.html")
    pisitools.insinto("%s/%s" % (get.docDIR(), get.srcNAME()), "doc/build")
    pisitools.insinto("%s/%s" % (get.docDIR(), get.srcNAME()), "examples")
