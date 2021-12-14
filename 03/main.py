file = "C:\\Users\\mgreen\\code\\aoc\\03\\sample.txt"
# file = "C:\\Users\\mgreen\\code\\aoc\\03\\input.txt"

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
            total += is_set(int(it, 2), bit)
        gamma_str = '1' + gamma_str if total > 0 else '0' + gamma_str

    gamma = int(gamma_str, 2)
    # print(gamma)
    # print(bin(gamma))

    epsilon = gamma ^ int(n * '1', 2)
    # print(epsilon)
    # print(bin(epsilon))

    print(f"Part 1: {gamma * epsilon}")

"""
Keep only numbers selected by the bit criteria for the type of rating value for which you are searching. Discard numbers which do not match the bit criteria.
If you only have one number left, stop; this is the rating value for which you are searching.
Otherwise, repeat the process, considering the next bit to the right.
The bit criteria depends on which type of rating value you want to find:

To find oxygen generator rating, determine the most common value (0 or 1) in the current bit position, and keep only numbers with that bit in that position. 
If 0 and 1 are equally common, keep values with a 1 in the position being considered.

To find CO2 scrubber rating, determine the least common value (0 or 1) in the current bit position, and keep only numbers with that bit in that position. 
If 0 and 1 are equally common, keep values with a 0 in the position being considered.
"""

def part2():
    input = read_input(file)

    oxygen = input
    n = len(oxygen[0])
    for bit in range(n - 1, 0, -1):
        print(oxygen)
        total = 0
        for it in oxygen:
            total += is_set(int(it, 2), bit)
        most_common_bit = '1' if total > 0 else '0'
        print(most_common_bit)
        oxygen = list(filter(lambda x : x[bit] == most_common_bit, oxygen))
    print(oxygen)
        
        

            

        


if __name__ == "__main__":
    part1()
    part2()
    