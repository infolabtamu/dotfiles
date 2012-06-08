#!/usr/bin/env python
# shameless port of https://github.com/aniero/dotfiles/blob/master/install.rb

from glob import glob
from os import environ, getcwd, symlink
from os.path import exists, expanduser, join, normpath
from sys import stderr

home = expanduser(environ['HOME'])

def install_sym(src, target):
    if exists(target):
        print >>stderr, "skipping %s, already exists" % target
    else:
        print "installing %s to %s" % (src, target)
        symlink(src, target)

for f in glob('*'):
    if any((f.startswith(x) for x in ('README', 'install', 'tags'))): continue
    target = normpath(join(home, '.%s'%f))
    src = normpath(join(getcwd(), f))
    install_sym(src, target)
