#!/usr/bin/env python3

import sys

v = 50
mod = 100
zero_count = 0

for line in sys.stdin:
    lr = line[:1]
    sign = 1 if lr == "R" else -1
    n = int(line[1:])
    v = (v + sign * n) % mod
    if v == 0:
        zero_count += 1

print(zero_count)
