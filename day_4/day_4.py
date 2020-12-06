with open("day_4_input.txt", "r") as passports:
    all_passports = []
    current_passport = []

    # Read file by line
    for line in passports:
        # if line is not empty, split on whitespace, append each to current_passport
        if line != "\n":
            fields = line.split(" ")
            for field in fields:
                details = field.split(":")
                field_name = details[0]
                info = details[1]
                current_passport.append((field_name, info))
        # If line is empty, append current passport to all passports, and reset current passport to empty list
        else:
            all_passports.append(current_passport)
            current_passport = []
    # Append last passport
    all_passports.append(current_passport)
    current_passport = []

    def format_passport(fields_list):
        return {field_name: info for (field_name, info) in fields_list}

    def create_formatted_passports(passport_list):
        return [format_passport(passport) for passport in passport_list]

    def validate_field(field_name, info):
        def in_range(low, string, high):
            return low <= int(string) <= high

        def get_height_format(height_string):
            length = len(height_string)
            last_two = height_string[length - 2 :]
            acceptable_formats = {"cm", "in"}

            if last_two in acceptable_formats:
                return last_two
            else:
                return False

        def get_height(height_string):
            return height_string[: len(height_string) - 2]

        def starts_with_hash(string):
            return string[0] == "#"

        def validate_byr(info):
            return len(info) == 4 and in_range(1920, int(info), 2002)

        def validate_iyr(info):
            return len(info) == 4 and in_range(2010, int(info), 2020)

        def validate_eyr(info):
            return len(info) == 4 and in_range(2020, int(info), 2030)

        def validate_hgt(info):
            if len(info.strip()) < 4:
                return False

            height_format = get_height_format(info)

            if height_format == False:
                return False

            height = get_height(info)
            return (
                in_range(150, int(height), 193)
                if height_format == "cm"
                else in_range(59, int(height), 76)
            )

        def validate_hcl(info):
            color = info[1:]

            def check_color(color):
                for val in color:
                    if (val.isalpha() or val.isnumeric()) is not True:
                        return False
                return True

            return len(info) == 7 and starts_with_hash(info) and check_color(color)

        def validate_ecl(info):
            colors = {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"}
            return info in colors

        def validate_pid(info):
            return len(info) == 9

        def validate_cid(info):
            return True

        validators = {
            "byr": lambda info: validate_byr(info.strip("\n")),
            "iyr": lambda info: validate_iyr(info.strip("\n")),
            "eyr": lambda info: validate_eyr(info.strip("\n")),
            "hgt": lambda info: validate_hgt(info.strip("\n")),
            "hcl": lambda info: validate_hcl(info.strip("\n")),
            "ecl": lambda info: validate_ecl(info.strip("\n")),
            "pid": lambda info: validate_pid(info.strip("\n")),
            "cid": lambda info: validate_cid(info.strip("\n")),
        }

        return validators[field_name](info)

    def validate_passport(passport):
        fields = set(passport.keys())
        required_fields = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}
        has_all_required_fields = (
            fields.intersection(required_fields) == required_fields
        )

        def validate_all_fields(passport):
            validated_fields = [
                validate_field(field, passport[field]) for field in passport.keys()
            ]

            return False not in validated_fields

        return has_all_required_fields and validate_all_fields(passport)

    formatted_passports = create_formatted_passports(all_passports)
    valid_passports = sum(
        [1 if validate_passport(passport) else 0 for passport in formatted_passports]
    )

    print(valid_passports)
