# file = "C:\\Users\\mgreen\\code\\aoc\\01\\sample.txt"
file = "C:\\Users\\mgreen\\code\\aoc\\01\\input.txt"

class Window(object):
    def __init__(self, nums):
        self.nums = nums
        self.size = len(nums)
        self.pos = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.pos + 2 < self.size:
            i = self.pos
            window = self.nums[i] + self.nums[i+1] + self.nums[i+2]
            self.pos += 1
            return window
        raise StopIteration()

def read_input(fn):
    with open(fn) as f:
        return [int(line.rstrip()) for line in f.readlines()]

def part1():
    input = read_input(file)
    
    total = 0
    for i, it in enumerate(input):
        if i != 0:
            if it - input[i - 1] > 0:
                total += 1
    
    print(total)

def part2():
    input = read_input(file)

    w = Window(input)

    total = 0
    p = next(w)
    for it in w:
        if it - p > 0:
            total += 1
        p = it
    
    print(total)

if __name__ == "__main__":
    part1()
    part2()
    