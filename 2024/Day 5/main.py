import re
from collections import defaultdict

INPUT_FILE = 'input.txt'


class Page:
    def __init__(self, page_number, rules):
        self.page_number = page_number
        self.rules = rules

    def __gt__(self, other):
        return other.page_number in self.rules[self.page_number]

    def __lt__(self, other):
        return self.page_number in self.rules[other.page_number]

    def __eq__(self, other):
        return not self.__lt__(other) and not self.__gt__(other)

    def int_value(self):
        return int(self.page_number)


def main():
    rules = defaultdict(set)
    updates = []
    with open(INPUT_FILE) as fr:
        for line in fr:
            line = line.strip()
            if re.search(r'\d+\|\d+', line):
                page1, page2 = line.split('|')
                rules[page2].add(page1)
            elif line != '':
                updates.append(line.split(','))

    updates = [[Page(page, rules) for page in update] for update in updates]
    correctly_ordered = []
    incorrectly_ordered = []

    for update in updates:
        correctly_ordered.append(update) if sorted(update) == update else incorrectly_ordered.append(update)

    # Part 1
    middle_sum = sum(update[int(len(update) / 2)].int_value() for update in correctly_ordered)
    print(middle_sum)

    # Part 2
    middle_sum = sum(sorted(update)[int(len(update) / 2)].int_value() for update in incorrectly_ordered)
    print(middle_sum)


if __name__ == '__main__':
    main()
