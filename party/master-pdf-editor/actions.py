#!/usr/bin/python

# Created For Solus Operating System

from pisi.actionsapi import get, pisitools, shelltools

NoStrip = ["/opt", "/usr"]
IgnoreAutodep = True

Version = get.srcVERSION()

def setup():
	shelltools.system("pwd")
	shelltools.system("ar xf master-pdf-editor-%s_qt5.amd64.deb" % (get.srcVERSION()))
	shelltools.system("tar xf data.tar.xz")

def install():
	pisitools.insinto("/", "opt")
	pisitools.insinto("/", "usr")
