#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import mesontools
from pisi.actionsapi import get

def setup():
    shelltools.export("CFLAGS", "%s -Wformat" % get.CFLAGS())
    mesontools.configure("-D docs=true")

def build():
    mesontools.build()

def install():
    mesontools.install()
    
    # Use alsa-card-profiles built with Pulseaudio
    pisitools.removeDir("/usr/share/alsa-card-profile")
    
    pisitools.dosym("/usr/share/alsa/alsa.conf.d/50-pipewire.conf", "/etc/alsa/conf.d/50-pipewire.conf")

    #shelltools.cd("..")
    pisitools.dodoc("LICENSE", "COPYING", "NEWS", "README*")
