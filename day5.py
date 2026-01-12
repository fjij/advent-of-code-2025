#!/usr/bin/env python3

import sys


def parse_input() -> tuple[list[tuple[int, int]], list[int]]:
    fresh_ranges: list[tuple[int, int]] = []
    available_ids: list[int] = []
    for line in sys.stdin:
        if line == "\n":
            break
        (a, b) = line.split("-")
        fresh_ranges.append((int(a), int(b)))
    for line in sys.stdin:
        available_ids.append(int(line))
    return fresh_ranges, available_ids


def count_fresh_available_ids(fresh_ranges: list[tuple[int, int]], available_ids: list[int]) -> int: 
    n = 0
    for id in available_ids:
        fresh = False
        for a, b in fresh_ranges:
            if a <= id and id <= b:
                fresh = True
                break
        if fresh:
            n += 1
    return n


def count_possible_fresh_ids(fresh_ranges: list[tuple[int, int]]) -> int:
    merged_ranges: list[tuple[int, int]] = []
    fresh_ranges = sorted(fresh_ranges)
    cur_range = fresh_ranges[0]
    for a, b in fresh_ranges[1:]:
        if a > cur_range[1]:
            merged_ranges.append(cur_range)
            cur_range = (a, b)
        else:
            cur_range = (cur_range[0], max(cur_range[1], b))
    merged_ranges.append(cur_range)
    return sum(b - a + 1 for a, b in merged_ranges)


if __name__ == "__main__":
    fresh_ranges, available_ids = parse_input()
    print("Part 1:", count_fresh_available_ids(fresh_ranges, available_ids))
    print("Part 2:", count_possible_fresh_ids(fresh_ranges))
