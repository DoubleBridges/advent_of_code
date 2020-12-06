with open("day_6_input.txt", "r") as answers:

    def grouped_answers(answers):
        answers_by_group = []
        group_answers = set()

        for answer_set in answers:
            if answer_set != "\n":
                for answer in answer_set:
                    group_answers.add(answer) if answer != "\n" else 0

            else:
                print(group_answers)
                answers_by_group.append(group_answers)
                group_answers = set()

        answers_by_group.append(group_answers)
        return answers_by_group

    def count_answers_by_group(answers):
        return [len(answer) for answer in answers]

    group_answers = grouped_answers(answers)

    # print(sum(count_answers_by_group(group_answers)))
