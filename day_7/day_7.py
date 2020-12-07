with open ('day_7_input.txt', 'r') as regulations:
    def bag_color(color_string):
        return f"{color_string.split(' ')[0]}-{color_string.split(' ')[1]} "
    
    def regulations_map(regulations):
        formatted_regs ={}
        for rule in regulations:
            outer_and_inner_bags = rule.split(' contain ')
            outer_bag = outer_and_inner_bags[0]
            inner_bags = outer_and_inner_bags[1].split(', ')
            inner_bag_map = {}

            for bag in inner_bags:
                details = bag.split(' ')
                count = details[0]
                bag = f"{details[1]}-{details[2]}"
                inner_bag_map[bag] = count

            formatted_regs[bag_color(outer_bag)] = inner_bag_map

        return formatted_regs


    rules = regulations_map(regulations)

    bags_that_can_have_gold = set()
    
    for bag in rules:
        color = 'shiny-gold'
        print(color in rules[bag])