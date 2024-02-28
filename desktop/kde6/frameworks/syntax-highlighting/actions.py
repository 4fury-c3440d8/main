#!/usr/bin/python
# -*- coding: utf-8 -*-
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import kde6
from pisi.actionsapi import pisitools

# if pisi can't find source directory, see /var/pisi/syntax-highlighting-kf6/work/ and:
# WorkDir="syntax-highlighting-kf6-"+ get.srcVERSION() +"/sub_project_dir/"

def setup():
    kde6.configure()

def build():
    kde6.make()

def install():
    kde6.install()

    pisitools.dodoc("README.md")

