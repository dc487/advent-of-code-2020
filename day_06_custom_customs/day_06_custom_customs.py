import pathlib

class _GroupAnswers:
    def __init__(self, answers):
        self.answers = answers
        self.answer_parts = [set(x) for x in answers.strip().split(" ")]
        
    def get_total_yes_answers(self):
        return set(self.answers.replace(" ", ""))

    def get_unanimous_yes_answers(self):
        if (len(self.answer_parts) == 0):
            return set()
        elif (len(self.answer_parts) == 1):
            return self.answer_parts[0]
        
        return self.answer_parts[0].intersection(*self.answer_parts[1::])

def load_answers(answer_location):
    return [_GroupAnswers(x) for x in pathlib.Path(answer_location).read_text().replace("\n\n", "_BREAK_").replace("\n", " ").replace("_BREAK_", "\n").splitlines()]

if __name__ == "__main__":
    answers = load_answers("./input/form_answers.txt")

    # Part 1
    group_counts = sum([len(x.get_total_yes_answers()) for x in answers])
    print("Part 1:\n  Total Group Counts: {0}".format(group_counts))

    # Part 2
    group_counts = sum([len(x.get_unanimous_yes_answers()) for x in answers])
    print("Part 2:\n  Unanimous Group Counts: {0}".format(group_counts))
