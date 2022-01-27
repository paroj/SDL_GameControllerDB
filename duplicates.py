# SPDX-License-Identifier: Zlib

import difflib
import sys

i = 0
cdict = {}
for i, l in enumerate(open("gamecontrollerdb.txt")):
    l = l.strip()
    if l.startswith("#") or not l:
        continue
    
    c = l.split(",")
    key = tuple([c[0]]+[ce for ce in c[1:] if "platform:" in ce])

    if key in cdict:
        print("Duplicate:", c[1], "at line", i + 1)
        out = list(difflib.unified_diff(cdict[key], sorted(c), n=0))[3:]
        out = [o for o in out if not o.startswith("@@")]
        print("\t", " ".join(out), file=sys.stderr)
        sys.exit(1)
    cdict[key] = sorted(c)