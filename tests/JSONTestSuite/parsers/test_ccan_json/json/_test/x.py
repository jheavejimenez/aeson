#!/usr/bin/env python

import os

with open("test-strings") as f:
    for (i,l) in enumerate(f):
        l = l.rstrip()
        filename = f"y_{i}.json" if l.startswith("valid") else f"n_{i}.json"
        try:
            l = l[l.index(" ")+1:]

            with open(os.path.sep.join(["nst_files", filename]), 'wb+') as f:
                f.write(l)
        except:
            pass
        