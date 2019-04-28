#!/usr/bin/python

# Created For Solus Operating System

from pisi.actionsapi import get, pisitools, shelltools

NoStrip = ["/opt", "/usr"]
IgnoreAutodep = True

def setup():
	shelltools.system("pwd")
	shelltools.system("ar xf XMind-ZEN-for-Linux-64bit.deb")
	shelltools.system("tar xf data.tar.xz")

def install():
	pisitools.insinto("/", "etc")
	pisitools.insinto("/", "opt")
