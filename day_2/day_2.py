from collections import Counter

with open("./day_2_input.txt", "r") as passwords:

    def get_password_details(line):
        details = {}
        parts = line.split(" ")

        details['char_count'] = (int(parts[0].split('-')[0]), int(parts[0].split('-')[1]))
        details['char'] = parts[1][0]
        details['password_string'] = str(parts[2])

        return details

    # Day 1
    # def validate_password(attempt):
    #     details = get_password_details(attempt)
    #     char_counts = Counter(details["password_string"])
    #     target_char_count = char_counts[details['char']]
    #     low_count = details["char_count"][0]
    #     high_count = details["char_count"][1]
        
    #     if target_char_count in range(low_count, high_count+1):
    #         return 1
    #     else:
    #         return 0

    # Day 2        
    def validate_password(attempt):
        details = get_password_details(attempt)
        password = details["password_string"]
        target_char = details["char"]
        first_position = details["char_count"][0]-1
        second_position = details["char_count"][1]-1
        first_char = password[first_position]
        second_char = password[second_position]
        
        if (first_char == target_char or second_char == target_char) and (first_char != second_char):
            return 1
        else:
            return 0
            
    
    valid_passwords = 0

    for password_attempt in passwords:        
        valid_passwords += validate_password(password_attempt)


    print(valid_passwords)