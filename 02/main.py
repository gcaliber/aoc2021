# file = "C:\\Users\\mgreen\\code\\aoc\\02\\sample.txt"
file = "C:\\Users\\mgreen\\code\\aoc\\02\\input.txt"

def read_input(fn):
    with open(fn) as f:
        result = []
        lines = [line.rstrip() for line in f.readlines()]
        for it in lines:
            dir, n = it.split()
            result.append((dir, int(n)))
        return result

def part1():
    commands = read_input(file)

    d, h = 0, 0
    for command, n in commands:
        if command == "forward":
            h += n
        elif command == "down":
            d += n
        elif command == "up":
            d -= n

    print(f"Part 1: {d * h}")

def part2():
    commands = read_input(file)

    a, d, h = 0, 0, 0
    for command, n in commands:
        if command == "forward":
            h += n
            d += a * n
        elif command == "down":
            a += n
        elif command == "up":
            a -= n

    print(f"Part 2: {d * h}")

if __name__ == "__main__":
    part1()
    part2()
    