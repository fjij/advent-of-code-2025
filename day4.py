#!/usr/bin/env python3

import sys

def parse_input() -> list[list[bool]]:
    grid: list[list[bool]] = []
    for line in sys.stdin:
        row: list[bool] = []
        for c in line:
            row.append(c == "@")
        grid.append(row)
    return grid


def get_accessible_rolls(grid: list[list[bool]]) -> list[tuple[int, int]]:
    accessible_rolls: list[tuple[int, int]] = []

    h = len(grid)
    w = len(grid[0])

    def read_grid(x: int, y: int) -> bool:
        if x < 0 or x >= w or y < 0 or y >= h:
            return False
        return grid[y][x]

    def count_grid(x: int, y: int) -> int:
        return 1 if read_grid(x, y) else 0
    
    for y in range(h):
        for x in range(w):
            if read_grid(x, y):
                adjacent_count = sum([
                    count_grid(x - 1, y),
                    count_grid(x + 1, y),
                    count_grid(x - 1, y - 1),
                    count_grid(x + 1, y - 1),
                    count_grid(x - 1, y + 1),
                    count_grid(x + 1, y + 1),
                    count_grid(x, y - 1),
                    count_grid(x, y + 1),
                ])
                if adjacent_count < 4:
                    accessible_rolls.append((x, y))
    return accessible_rolls


def remove_rolls(grid: list[list[bool]], rolls: list[tuple[int, int]]) -> list[list[bool]]:
    for (x, y) in rolls:
        grid[y][x] = False
    return grid


def day4pt1(grid: list[list[bool]]) -> int:
    return len(get_accessible_rolls(grid))


def day4pt2(grid: list[list[bool]]) -> int:
    removed_roll_count = 0
    while len(accessible_rolls := get_accessible_rolls(grid)) > 0:
        removed_roll_count += len(accessible_rolls)
        grid = remove_rolls(grid, accessible_rolls)
    return removed_roll_count


if __name__ == "__main__":
    grid = parse_input()
    print("Part 1:", day4pt1(grid))
    print("Part 2:", day4pt2(grid))
