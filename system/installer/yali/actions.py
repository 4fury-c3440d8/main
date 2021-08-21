#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import pythonmodules

def setup():
    repo_uri = "https://stable2.pisilinux.org/pisi-index.xml.xz" # FIXME
    #pisitools.dosed("yali/constants.py", "@REPO_URI@", repo_uri)
    #pisitools.dosed("yali/constants.py", "@REPO_NAME@", "Beta") # FIXME
    pisitools.dosed("conf/yali.conf", "@REPO_URI@", repo_uri)
    pisitools.dosed("conf/yali.conf", "@REPO_NAME@", "Stable2") # FIXME

    pisitools.dosed("conf/yali.conf", "@INSTALL_TYPE@", "default")

def build():
    pythonmodules.compile()

def install():
    pythonmodules.install()

    pisitools.domove("/usr/share/applications/yali.desktop", "/usr/share/display-managers/")
    pisitools.removeDir("usr/share/applications")
