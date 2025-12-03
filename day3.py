#!/usr/bin/env python3

import sys
from itertools import combinations
from typing import Callable


def parse_input() -> list[list[int]]:
    valid_chars = {"1", "2", "3", "4", "5", "6", "7", "8", "9"}
    banks: list[list[int]] = []
    for line in sys.stdin:
        banks.append([int(ch) for ch in line if ch in valid_chars])
    return banks


def max_joltage_v1(bank: list[int]) -> int:
    return max(a*10 + b for (a, b) in combinations(bank, 2))


def max_joltage_v2(bank: list[int]) -> int:
    choices_remain = 12
    selected = []
    last_choice_idx = -1
    while choices_remain > 0:
        indexed_options = list(enumerate(bank))[last_choice_idx+1:len(bank)-(choices_remain - 1)]
        best_choice_idx, best_choice = sorted(indexed_options, key=lambda t: (t[1], -t[0]), reverse=True)[0]
        selected.append(best_choice)
        last_choice_idx = best_choice_idx
        choices_remain -= 1
    return int("".join(str(d) for d in selected))


def sum_max_joltage(banks: list[list[int]], max_joltage: Callable[[list[int]], int]) -> int:
    joltage_sum = 0
    for bank in banks:
        joltage_sum += max_joltage(bank)
    return joltage_sum


def day3pt1(banks: list[list[int]]) -> int:
    return sum_max_joltage(banks, max_joltage_v1)


def day3pt2(banks: list[list[int]]) -> int:
    return sum_max_joltage(banks, max_joltage_v2)


if __name__ == "__main__":
    banks = parse_input()
    print("Part 1:", day3pt1(banks))
    print("Part 2:", day3pt2(banks))
