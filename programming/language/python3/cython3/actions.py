#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import get
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import pythonmodules

def build():
    # fix unused direct dependency analysis
    shelltools.export("LDSHARED", "x86_64-pc-linux-gnu-gcc -Wl,-O1,--as-needed -shared -lpthread -Wl,-O1 -Wl,-z,relro -Wl,--hash-style=gnu -Wl,--as-needed -Wl,--sort-common")
    # suppress compiler warnings
    #shelltools.export("CFLAGS", "-fno-strict-aliasing -mtune=generic -march=x86-64 -O2 -pipe -fstack-protector -D_FORTIFY_SOURCE=2 -g -fPIC -fwrapv -DNDEBUG -g -fwrapv -O3 -Wno-strict-aliasing")

    pythonmodules.compile(pyVer="3")

# Blue DeviL Note: it takes hours to run test, run with caution!
#def check():
#    pythonmodules.run("runtests.py -vv --no-pyregr", pyVer="3")

def install():
    pythonmodules.install(pyVer="3")
    
    for bin in shelltools.ls("%s/usr/bin" % get.installDIR()):
        pisitools.rename("/usr/bin/%s" % bin, "%s3" % bin)
