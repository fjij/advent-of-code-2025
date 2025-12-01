#!/usr/bin/env python3

import sys

v = 50
MOD = 100
zero_count = 0

def mod_zero_count(v: int, rot: int, mod: int) -> tuple[int, int]:
    """Returns the value after it has been rotated by `rot`, as well as the
    number of times it has crossed zero during its rotation, including if it
    ends on zero.
    """
    start_zero = v == 0
    r_mod_count = 0
    l_mod_count = 0
    v += rot
    while v >= mod:
        v -= mod
        r_mod_count += 1
    while v < 0:
        v += mod
        l_mod_count += 1
    end_zero = v == 0

    if l_mod_count == 0 and r_mod_count == 0:
        return v, 1 if end_zero and not start_zero else 0
    elif l_mod_count > 0:
        return v, l_mod_count + (1 if end_zero else 0) - (1 if start_zero else 0)
    elif r_mod_count > 0:
        return v, r_mod_count
    raise RuntimeError()

for line in sys.stdin:
    lr = line[:1]
    sign = 1 if lr == "R" else -1
    n = int(line[1:])
    v, zc = mod_zero_count(v, sign * n, MOD)
    zero_count += zc

print(zero_count)
