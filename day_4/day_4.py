with open('day_4_input.txt', 'r') as passports:
    all_passports = []
    current_passport = []
    # Split the file into passports
    # Read file by line
    for line in passports:
        # if line is not empty, split on whitespace, append each to current_passport
        if line is not "\n":
            fields = line.split(' ')
            for field in fields:
                current_passport.append(field)
        # If line is empty, append current passport to all passports, and reset current passport to empty list
        else:
            all_passports.append(current_passport)
            current_passport = []
    # Append last passport
    all_passports.append(current_passport)
    current_passport = []

    def format_passport(list_fields):
        passport_dict = {}
        for field in list_fields:

            details = field.split(':')
            field_name = details[0]
            info = details[1]
            passport_dict[field_name] = info
        
        return passport_dict
    
    def create_formatted_passports(passport_list):
        passports = []
        for passport in passport_list:
            passports.append(format_passport(passport))

        return passports

    def validate_passport(passport):
        fields = set(passport.keys())
        required_fields = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}
        has_all_required_fields = fields.intersection(required_fields) == required_fields

        return True if has_all_required_fields else False

    formatted_passports = create_formatted_passports(all_passports)

    valid_passports = 0

    for passport in formatted_passports:
        valid_passports += 1 if validate_passport(passport) else 0

    print(valid_passports)