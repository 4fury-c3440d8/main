#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import cmaketools
from pisi.actionsapi import get

def setup():
    #pisitools.flags.add("-pthread -I/usr/include/OpenEXR -I/usr/include/libdrm")
    #pisitools.ldflags.add("-lImath -lHalf -lIex -lIexMath -lIlmThread -lpthread")
    shelltools.makedirs("build")

    shelltools.cd("build")
    cmaketools.configure(sourceDir="..")
    

def build():
    shelltools.cd("build")
    cmaketools.make()

def install():
    shelltools.cd("build")
    #shelltools.cd("OpenEXR")
    # documents and examples go to "/usr/share/OpenEXR" without these parameters
    docdir = "/usr/share/doc/%s" % get.srcNAME()
    examplesdir = "%s/examples" % docdir
    cmaketools.rawInstall("DESTDIR=%s docdir=%s examplesdir=%s" % (get.installDIR(), docdir, examplesdir))
    #autotools.rawInstall("DESTDIR=%s docdir=%s examplesdir=%s" % (get.installDIR(), docdir, examplesdir))
    
    shelltools.cd("..")
    pisitools.dodoc("README*","LICENSE*")
