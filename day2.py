#!/usr/bin/env python3

from typing import Callable


def parse_input() -> list[tuple[int, int]]:
    line = input()
    id_ranges: list[tuple[int, int]] = []
    for id_range_str in line.split(","):
        a_str, b_str = id_range_str.split("-")
        id_range = (int(a_str), int(b_str))
        id_ranges.append(id_range)
    return id_ranges


def compute_invalid_ids_v1(a: int, b: int) -> list[int]:
    invalid_ids = []
    for x in range(a, b + 1):
        x_str = str(x)
        if len(x_str) % 2 == 1:
            continue
        m = len(x_str) // 2
        if x_str[:m] == x_str[m:]:
            invalid_ids.append(x)
    return invalid_ids


def compute_invalid_ids_v2(a: int, b: int) -> list[int]:
    invalid_ids = []
    for x in range(a, b + 1):
        x_str = str(x)
        for d in range(2, len(x_str) + 1):
            if len(x_str) % d != 0:
                continue
            l = len(x_str) // d
            invalid = True
            for i in range(d):
                if x_str[i*l:(i+1)*l] != x_str[:l]:
                    invalid = False
                    continue
            if not invalid:
                continue
            invalid_ids.append(x)
    return list(set(invalid_ids))


def sum_of_invalid_ids(id_ranges: list[tuple[int, int]], compute_invalid_ids: Callable[[int, int],list[int]]) -> int:
    invalid_ids: list[int] = []
    for (a, b) in id_ranges:
        invalid_ids.extend(compute_invalid_ids(a, b))
    return sum(invalid_ids)
    

def day2pt1(id_ranges: list[tuple[int, int]]) -> int:
    return sum_of_invalid_ids(id_ranges, compute_invalid_ids_v1)

def day2pt2(id_ranges: list[tuple[int, int]]) -> int:
    return sum_of_invalid_ids(id_ranges, compute_invalid_ids_v2)

def main():
    id_ranges = parse_input()
    print("Part 1: ", day2pt1(id_ranges))
    print("Part 2: ", day2pt2(id_ranges))

if __name__ == "__main__":
    main()
