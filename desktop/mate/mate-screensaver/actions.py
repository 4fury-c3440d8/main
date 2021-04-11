#!/usr/bin/python
# -*- coding: utf-8 -*-
#

# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.autoreconf("-fiv")
    autotools.configure(" --enable-locking \
                          --libexecdir=/usr/lib/mate-screensaver \
                          --with-xf86gamma-ext \
                          --with-kbd-layout-indicator \
                          --with-systemd=no \
                          --prefix=/usr \
                          --sysconfdir=/etc \
                          --with-xscreensaverdir=/usr/share/xscreensaver/config \
                          --with-xscreensaverhackdir=/usr/lib/misc/xscreensaver")

    # for fix unused dependency
    pisitools.dosed("libtool"," -shared ", " -Wl,--as-needed -shared ")
    # patched pisi logo
    pisitools.dosed("savers/gnomelogo-floaters.desktop.in.in", "Floating GNOME", "Floating PISI")
    pisitools.dosed("po/tr.po", "Yüzen GNOME", "Yüzen PISI")
def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("README", "NEWS", "ChangeLog", "AUTHORS", "COPYING")
