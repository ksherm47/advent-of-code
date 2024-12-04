from collections import Counter

INPUT_FILE = 'input.txt'


def main():
    with open(INPUT_FILE) as fr:
        left, right = zip(*[map(int, line.split()) for line in fr])

    # Part 1
    total_dist = sum(abs(l - r) for l, r in zip(sorted(left), sorted(right)))
    print(total_dist)

    # Part 2
    counts = Counter(right)
    similarity_score = sum(l * counts[l] for l in left)
    print(similarity_score)


if __name__ == '__main__':
    main()
