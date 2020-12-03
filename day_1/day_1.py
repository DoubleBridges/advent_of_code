with open("./day_1_input.txt", "r") as transactions:
    transaction_list = []

    for transaction in transactions:
        transaction_list.append(int(transaction))

    sorted_transactions = sorted(transaction_list)
    # Day 1
    # low_pointer = 0
    # high_pointer = len(sorted_transactions) - 1

    # while low_pointer < high_pointer:
    #     transaction_sum = (
    #         sorted_transactions[low_pointer] + sorted_transactions[high_pointer]
    #     )

    #     if transaction_sum == target_sum
    #         return sorted_transactions[low_pointer] * sorted_transactions[high_pointer]
    #         
    #     else:
    #         if transaction_sum < target_sum
    #             low_pointer += 1
    #         else:
    #             high_pointer -= 1


    def threeSum(transactions, target_sum):
        num_of_transactions = len(transactions)

        for i in range(0, num_of_transactions - 2):
            low_pointer = i + 1
            high_pointer = num_of_transactions - 1

            while low_pointer < high_pointer:

                if transactions[i] + transactions[low_pointer] + transactions[high_pointer] == target_sum:
                    
                    return  transactions[i] * transactions[low_pointer] * transactions[high_pointer]

                elif transactions[i] + transactions[low_pointer] + transactions[high_pointer] < target_sum:
                    low_pointer += 1

                else: 
                    high_pointer -= 1


    print(threeSum(sorted_transactions, 2020))