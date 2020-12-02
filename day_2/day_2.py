from collections import Counter

with open("./day_2_input.txt", "r+") as passwords:
    
    valid_passwords = 0
    password_total = 0
    for password_attempt in passwords:

      def get_password_details(line):
        details = {}
        parts = line.split(" ")

        details['char_count'] = (int(parts[0].split('-')[0]), int(parts[0].split('-')[1]))
        details['char'] = parts[1][0]
        details['password_string'] = str(parts[2])

        return details

      def validate_password(attempt):
        details = get_password_details(attempt)
        char_counts = Counter(details["password_string"])
        
        if char_counts[details['char']] in range(details["char_count"][0], details["char_count"][1]+1):
            print('valid', details['char_count'], details['char'], details['password_string'], char_counts[details['char']])
            return 1
        else:
            print('invalid', details['char_count'], details['char'], details['password_string'], char_counts[details['char']])
            return 0
        
      valid_passwords += validate_password(password_attempt)
      password_total += 1


    print(password_total, valid_passwords)