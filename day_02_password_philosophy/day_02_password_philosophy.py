import pathlib

class _PasswordPolicy:
    def __init__(self, policy_string):
        self.policy_string = policy_string
        policy_parts = policy_string.split(": ")
        self.password = policy_parts[1]
        policy_definition_parts = policy_parts[0].split(" ")
        self.policy_letter = policy_definition_parts[1]
        policy_definition_numbers = policy_definition_parts[0].split("-")
        self.first_number = int(policy_definition_numbers[0])
        self.second_number = int(policy_definition_numbers[1])

    def is_valid_part_1(self):
        letter_count = self.password.count(self.policy_letter)
        return letter_count >= self.first_number and letter_count <= self.second_number

    def is_valid_part_2(self):
        first_character_matches_policy = self.password[self.first_number - 1] == self.policy_letter
        second_character_matches_policy = self.password[self.second_number - 1] == self.policy_letter
        return first_character_matches_policy ^ second_character_matches_policy

def load_password_policies(password_policy_location):
    return [_PasswordPolicy(x) for x in pathlib.Path(password_policy_location).read_text().splitlines()]

if __name__ == "__main__":
    password_policies = load_password_policies("./input/passwords.txt")

    # Part 1 - initial password policy rule
    valid_password_policies = [x for x in password_policies if x.is_valid_part_1()]
    print("Part 1:\n  Total valid policies: {0}".format(len(valid_password_policies)))

    # Part 2 - updated password policy rule
    valid_password_policies = [x for x in password_policies if x.is_valid_part_2()]
    print("Part 2:\n  Total valid policies: {0}".format(len(valid_password_policies)))
