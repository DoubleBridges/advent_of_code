with open("day_1/day_1_input.txt", "r+") as transactions:
    transaction_list = []

    for transaction in transactions:
        transaction_list.append(int(transaction))

    sorted_transactions = sorted(transaction_list)
    # low_pointer = 0
    # high_pointer = len(sorted_transactions) - 1

    # while low_pointer < high_pointer:
    #     transaction_sum = (
    #         sorted_transactions[low_pointer] + sorted_transactions[high_pointer]
    #     )

    #     if transaction_sum == 2020:
    #         print(sorted_transactions[low_pointer], sorted_transactions[high_pointer])
    #         break
    #     else:
    #         if transaction_sum < 2020:
    #             low_pointer += 1
    #         else:
    #             high_pointer -= 1

    # print(sorted_transactions[low_pointer] * sorted_transactions[high_pointer])

    def find3Numbers(A, arr_size, sum):

        # Sort the elements
        # A.sort()

        # Now fix the first element
        # one by one and find the
        # other two elements
        for i in range(0, arr_size - 2):

            # To find the other two elements,
            # start two index variables from
            # two corners of the array and
            # move them toward each other

            # index of the first element
            # in the remaining elements
            l = i + 1

            # index of the last element
            r = arr_size - 1
            while l < r:

                if A[i] + A[l] + A[r] == sum:
                    print(A[i] * A[l] * A[r])

                    return True

                elif A[i] + A[l] + A[r] < sum:
                    l += 1
                else:  # A[i] + A[l] + A[r] > sum
                    r -= 1

        # If we reach here, then
        # no triplet was found
        return False

    find3Numbers(sorted_transactions, len(sorted_transactions), 2020)