#!/usr/bin/env python

import os
import sys
import argparse

from struct import unpack


def spec_to_hex(space, w, x, y, z):
    if space > 0:
        return "000000";

    r, b, g = (0, 0, 0)
    if space == 0:
        r = abs(w/256)
        b = abs(x/256)
        g = abs(y/256)

    return "%.2x%.2x%.2x" % (r, b, g)


def convert(fd):
    version, nr = unpack(">hh", fd.read(4))
    entry_nr = 1

    # seek for v2
    fd.seek(4 + (10 * nr))
    v2 = fd.read(4)
    version = 2
    if v2 == '':
        fd.seek(4)
        version = 0

    entry = fd.read(10)
    while entry != '':
        name = u"color%d" % (entry_nr)
        space, w, x, y, z = unpack(">hhhhh", entry)
        if version == 2:
            zero, ln = unpack(">hh", fd.read(4))
            assert zero == 0
            ln = ln
            name = fd.read(2 * ln)
        entry = fd.read(10)
        entry_nr += 1

        yield name, [space, w, x, y, z]



def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("file", type=argparse.FileType("r"),
                      default=sys.stdin,
                      help=".aco file path")
    args = parser.parse_args()
    gen = convert(args.file)
    out = sys.stdout.write
    for name, spec in gen:
        line = '$%s = "#%s";\n' %  (name.replace(" ", "_"), spec_to_hex(*spec))
        out(line)

if __name__ == "__main__":
    main()
