from collections import Counter

with open("example.txt", "r") as answers:

    def grouped_answers(answers):
        answers_by_group = []
        group_answers = set()

        for answer_set in answers:
            if answer_set != "\n":
                for answer in answer_set:
                    group_answers.add(answer) if answer != "\n" else 0

            else:
                answers_by_group.append(group_answers)
                group_answers = set()

        answers_by_group.append(group_answers)
        return answers_by_group

    def count_answers_by_group(answers):
        return [len(answer) for answer in answers]

    # group_answers = grouped_answers(answers)

    # print(sum(count_answers_by_group(group_answers)))

    def grouped_answers_2(answers):
        answers_by_group = []
        group_answers = []
        group_members = 0

        for answer_set in answers:
            if answer_set != "\n":
                for answer in answer_set.strip("\n"):
                    group_answers.append(answer.strip("\n"))
                group_members += 1
            else:
                answers_by_group.append((group_members, dict(Counter(group_answers))))
                group_answers = []
                group_members = 0

        answers_by_group.append(group_answers)
        return answers_by_group

    def unanimous(answers):
        counts = []
        for answer_count in answers:
            group_counts = []
            members = answer_count[0]
            count_map = answer_count[1]
            for answer in count_map.keys():
                if count_map[answer] == members:
                    group_counts.append(answer)

        return counts

    print(unanimous(grouped_answers_2(answers)))
