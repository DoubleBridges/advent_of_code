with open('day_4_input.txt', 'r') as passports:
    all_passports = []
    current_passport = []
    
    # Read file by line
    for line in passports:
        # if line is not empty, split on whitespace, append each to current_passport
        if line is not "\n":
            fields = line.split(' ')
            for field in fields:
                details = field.split(':')
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
        def has_four_digits(string):
            return len(string) == 4

        def in_range(low, string, high):
            return low <= int(string) <= high
        
        def get_height_format(height_string):
            length = len(height_string)
            last_two = height_string[length-2: length-1]
            return last_two 

        def get_height(height_string):
            return height_string[0: len(height_string)-2]
        
        def starts_with_hash(string):
            return string[0] = '#'
        
        def validate_byr(info):
            return has_four_digits(info) and in_range(1920, int(info), 2002)
        
        def validate_iyr(info):
            return has_four_digits(info) and in_range(2010, int(info), 2020)

        def validate_eyr(info):
            return has_four_digits(info) and in_range(2020, int(info), 2030)

        def validate_hgt(info):
            height_format = get_height_format(info)
            height = get_height(info)
            return in_range(150, int(height), 193) if height_format == 'cm' else in_range(59, int(height), 76)

        def validate_hcl(info):
            color = info[1:]
            for val in color: 
                if 
                
        
        validators = {
            'byr' : lambda info: validate_byr(info),
            'iyr' : lambda info: validate_iyr(info),
            'eyr' : lambda info: len
        }


    def validate_passport(passport):
        fields = set(passport.keys())
        required_fields = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}
        has_all_required_fields = fields.intersection(required_fields) == required_fields

        return True if has_all_required_fields else False

    formatted_passports = create_formatted_passports(all_passports)
    valid_passports = sum([1 if validate_passport(passport) else 0 for passport in formatted_passports])

    print(valid_passports)