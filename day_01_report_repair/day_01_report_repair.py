import pathlib

def load_expense_report(expense_report_location):
    return set([int(x) for x in pathlib.Path(expense_report_location).read_text().splitlines()])

def find_entries_summing_to(total, expense_report):
    return [x for x in expense_report if (total - x) in expense_report]

if __name__ == "__main__":
    expense_report = load_expense_report("./input/expense_report.txt")

    # Part 1 - find two numbers that add up to 2020
    entries_summing_to_2020 = find_entries_summing_to(2020, expense_report)
    answer1 = entries_summing_to_2020[0] * entries_summing_to_2020[1]
    print("Part 1: \n  Entries: {0}\n  Result: {1}".format(entries_summing_to_2020, answer1))

    # Part 2 - find three numbers that add up to 2020
    three_entries_summing_to_2020 = [x for x in expense_report if find_entries_summing_to(2020 - x, expense_report)]
    answer2 = three_entries_summing_to_2020[0] * three_entries_summing_to_2020[1] * three_entries_summing_to_2020[2]
    print("Part 2: \n  Entries: {0}\n  Result: {1}".format(three_entries_summing_to_2020, answer2))
