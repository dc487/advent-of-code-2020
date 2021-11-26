import pathlib
import string

class _Passport:
    expected_keys = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    valid_eye_colours = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]

    def __init__(self, passport_details):
        values = [x.split(":") for x in passport_details.strip().split(" ")]
        self.passport_fields = { x[0]:x[1] for x in values }

    def missing_required_fields(self):
        return [x for x in _Passport.expected_keys if x not in self.passport_fields.keys()]

    def is_valid_part_1(self):
        return not self.missing_required_fields()

    def is_birth_year_valid(self):
        if "byr" not in self.passport_fields.keys():
            return False
        
        birth_year = self.passport_fields["byr"]
        return birth_year.isdigit() and int(birth_year) >= 1920 and int(birth_year) <= 2002

    def is_issue_year_valid(self):
        if "iyr" not in self.passport_fields.keys():
            return False
        
        issue_year = self.passport_fields["iyr"]
        return issue_year.isdigit() and int(issue_year) >= 2010 and int(issue_year) <= 2020 

    def is_expiration_year_valid(self):
        if "eyr" not in self.passport_fields.keys():
            return False
        
        expiration_year = self.passport_fields["eyr"]
        return expiration_year.isdigit() and int(expiration_year) >= 2020 and int(expiration_year) <= 2030 

    def is_height_valid(self):
        if "hgt" not in self.passport_fields.keys():
            return False
        
        height = self.passport_fields["hgt"]
        if height.endswith("in"):
            height_in_inches = height[:-2:]
            return height_in_inches.isdigit() and int(height_in_inches) >= 59 and int(height_in_inches) <= 76
        elif height.endswith("cm"):
            height_in_centimetres = height[:-2:]
            return height_in_centimetres.isdigit() and int(height_in_centimetres) >= 150 and int(height_in_centimetres) <= 193
        else:
            return False

    def is_hair_color_valid(self):
        if "hcl" not in self.passport_fields.keys():
            return False

        hair_color = self.passport_fields["hcl"]
        return len(hair_color) == 7 and hair_color[0] == "#" and all(x in string.hexdigits for x in hair_color[1::])

    def is_eye_color_valid(self):
        if "ecl" not in self.passport_fields.keys():
            return False

        eye_color = self.passport_fields["ecl"]
        return eye_color in _Passport.valid_eye_colours

    def is_passport_number_valid(self):
        if "pid" not in self.passport_fields.keys():
            return False

        passport_number = self.passport_fields["pid"]
        return passport_number.isdigit() and len(passport_number) == 9

    def is_valid_part_2(self):
        return self.is_valid_part_1() and \
            self.is_birth_year_valid() and \
            self.is_issue_year_valid() and \
            self.is_expiration_year_valid() and \
            self.is_height_valid() and \
            self.is_hair_color_valid() and \
            self.is_eye_color_valid() and \
            self.is_passport_number_valid()

def load_passports(passports_location):
    return [_Passport(x) for x in pathlib.Path(passports_location).read_text().replace("\n\n", "__BREAK__").replace("\n", " ").replace("__BREAK__", "\n").splitlines()]

if __name__ == "__main__":
    passports = load_passports("./input/passports.txt")

    # Part 1
    valid_passports = [x for x in passports if x.is_valid_part_1()]
    print("Part 1:\n  Total Valid Passports: {0}".format(len(valid_passports)))

    # Part 2
    valid_passports = [x for x in passports if x.is_valid_part_2()]
    print("Part 2:\n  Total Valid Passports: {0}".format(len(valid_passports)))
