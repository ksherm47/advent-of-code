INPUT_FILE = 'input.txt'


def main():
    with open(INPUT_FILE) as fr:
        reports = [[int(r) for r in line.split()] for line in fr]

    # Part 1
    print(sum(1 for report in reports if is_safe(report)))

    # Part 2
    safe_count = 0
    for report in reports:
        if is_safe(report):
            safe_count += 1
        else:
            for i in range(len(report)):
                new_report = report[:i] + report[i + 1:]
                if is_safe(new_report):
                    safe_count += 1
                    break

    print(safe_count)


def is_safe(report):
    if len(report) < 2:
        return True

    is_decreasing = True
    is_increasing = True

    for i in range(len(report) - 1):
        difference = report[i + 1] - report[i]
        if not 1 <= abs(difference) <= 3 or difference == 0:
            return False
        if difference > 0:
            is_decreasing = False
        else:
            is_increasing = False

        if not is_increasing and not is_decreasing:
            return False

    return True


if __name__ == '__main__':
    main()
