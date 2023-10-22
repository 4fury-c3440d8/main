# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import get
from pisi.actionsapi import pisitools
from pisi.actionsapi import mesontools
from pisi.actionsapi import shelltools


def setup():
    if not get.buildTYPE() == "emul32":
        options = "-Dudev=true -Dintel=enabled \
                  "
    
    if get.buildTYPE() == "emul32":
        options = " --libdir=lib32 \
                    -Dudev=false \
                    -Dintel=enabled \
                    -Dvalgrind=disabled"



    mesontools.configure(options)

def build():
    mesontools.build()

def install():
    mesontools.install()
    
    if get.buildTYPE() == "emul32":
        return
