#!/usr/bin/env python

import sys

PY2K = sys.version_info[0] == 2

if PY2K:
    print('Ni')
else:
    print('Ni!')
