import re

INPUT_FILE = 'input.txt'
MUL_GROUP_REGEX = r'mul\((\d+),(\d+)\)'
MUL_REGEX = r'mul\(\d+,\d+\)'
DO_REGEX = r'do\(\)'
DONT_REGEX = r"don't\(\)"


def main():
    with open(INPUT_FILE) as fr:
        memory = ''.join([line for line in fr])

    # Part 1
    print(sum([int(x) * int(y) for x, y in re.findall(MUL_GROUP_REGEX, memory)]))

    # Part 2
    mul_sum = 0
    cmds = re.findall('|'.join([MUL_REGEX, DO_REGEX, DONT_REGEX]), memory)
    do = True
    for cmd in cmds:
        if cmd == 'do()':
            do = True
        elif cmd == "don't()":
            do = False
        else:
            match = re.match(MUL_GROUP_REGEX, cmd)
            mul_sum += int(match.group(1)) * int(match.group(2)) if do else 0

    print(mul_sum)


if __name__ == '__main__':
    main()
