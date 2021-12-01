import pathlib
import sys


def parse(puzzle_input):
    """Parse input"""
    return [int(line) for line in puzzle_input.split("\n")]


def part1(data):
    """Solve part 1"""
    depth_increase = 0
    previous_value = data[0]
    for val in data[1:]:
        if val > previous_value:
            depth_increase += 1
        previous_value = val
    return depth_increase


def part2(data):
    """Solve part 2"""
    if len(data) < 3:
        return 0
    curr_sum = prev_sum = sum(data[:3])
    slow = depth_increase = 0
    fast = 3
    while fast < len(data):
        curr_sum += data[fast] - data[slow]
        if curr_sum > prev_sum:
            depth_increase += 1
        prev_sum = curr_sum
        fast += 1
        slow += 1
    return depth_increase


def solve(puzzle_input):
    """Solve the puzzle for the given input"""
    data = parse(puzzle_input)
    solution1 = part1(data)
    solution2 = part2(data)

    return solution1, solution2


if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"{path}:")
        puzzle_input = pathlib.Path(path).read_text().strip()
        solutions = solve(puzzle_input)
        print("\n".join(str(solution) for solution in solutions))
