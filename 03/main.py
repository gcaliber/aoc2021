# file = "C:\\Users\\mgreen\\code\\aoc\\03\\sample.txt"
file = "C:\\Users\\mgreen\\code\\aoc\\03\\input.txt"

def read_input(fn):
    with open(fn) as f:
        return [line.rstrip() for line in f.readlines()]

def is_set(x, n):
    return 1 if x & 1 << n != 0 else -1

def part1():
    input = read_input(file)
    n = len(input[0])
    gamma_str = ''
    for bit in range(0, n):
        total = 0
        for it in input:
            total += is_set(int(it), bit)
        gamma_str = '1' + gamma_str if total > 0 else '0' + gamma_str

    gamma = int(gamma_str, 2)
    print(gamma)
    print(bin(gamma))
    # print(n * '1')
    # print(int(n * '1', 2))
    # print(bin(int(n * '1', 2)))
    epsilon = gamma ^ int(n * '1', 2)
    print(epsilon)
    print(bin(epsilon))

    print(f"Part 1: {gamma * epsilon}")
    

                
        
# def part2():
#     commands = read_input(file)

#     a, d, h = 0, 0, 0
#     for command, n in commands:
#         if command == "forward":
#             h += n
#             d += a * n
#         elif command == "down":
#             a += n
#         elif command == "up":
#             a -= n

#     print(f"Part 2: {d * h}")

if __name__ == "__main__":
    part1()
    # part2()
    