INPUT_FILE = 'input.txt'
WORD_TO_SEARCH = 'XMAS'


def main():
    with open(INPUT_FILE) as fr:
        grid = [[char for char in line.strip()] for line in fr]

    # Part 1
    dirs = [(1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1)]

    count = 0
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            for x_dir, y_dir in dirs:
                if part_1_search(WORD_TO_SEARCH, grid, x, y, x_dir, y_dir):
                    count += 1
    print(count)

    # Part 2
    count = 0
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if part_2_search(grid, x, y):
                count += 1
    print(count)


def part_1_search(word, grid, x, y, x_dir, y_dir):
    if word == '':
        return True

    if not (0 <= y < len(grid) and 0 <= x < len(grid[y])):
        return False

    if grid[y][x] != word[0]:
        return False

    return part_1_search(word[1:], grid, x + x_dir, y + y_dir, x_dir, y_dir)


def part_2_search(grid, x, y):
    if grid[y][x] != 'A':
        return False

    if not (0 <= y - 1 < len(grid) and
            0 <= x - 1 < len(grid[y]) and
            0 <= y + 1 < len(grid) and
            0 <= x + 1 < len(grid[y])):
        return False

    return ((grid[y - 1][x - 1] == 'M' and grid[y + 1][x + 1] == 'S') or
            (grid[y - 1][x - 1] == 'S' and grid[y + 1][x + 1] == 'M')) and \
           ((grid[y + 1][x - 1] == 'M' and grid[y - 1][x + 1] == 'S') or
            (grid[y + 1][x - 1] == 'S' and grid[y - 1][x + 1] == 'M'))


if __name__ == '__main__':
    main()
