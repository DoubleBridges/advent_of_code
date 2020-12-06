with open("day_5_input.txt", "r") as seat_bins:

    def seat_row(row_code):
        high_row = 127
        low_row = 0

        for zone in row_code:
            available_range = (high_row + 1) - low_row
            half = available_range // 2

            if low_row + 1 == high_row:
                return low_row if zone == "F" else high_row

            if zone == "F":
                high_row -= half
            else:
                low_row += half

    def seat_column(column_code):
        high_column = 7
        low_column = 0

        for zone in column_code:
            available_range = (high_column + 1) - low_column
            half = available_range // 2

            if low_column + 1 == high_column:
                return low_column if zone == "L" else high_column

            if zone == "L":
                high_column -= half
            else:
                low_column += half

    def seat_id(row, column):
        return (row * 8) + column

    def all_seats(seat_codes):
        seats = []

        for code in seat_codes:
            code = code.strip("\n")
            row = code[:-3]
            column = code[7:]

            seats.append(
                {"code": code, "row": seat_row(row), "column": seat_column(column)}
            )

        return seats

    def all_seat_ids(seats):
        return {seat_id(seat["row"], seat["column"]) for seat in seats}

    formatted_seats = all_seats(seat_bins)

    print(
        set(
            range(
                min(all_seat_ids(formatted_seats)), max(all_seat_ids(formatted_seats))
            )
        )
        - all_seat_ids(formatted_seats)
    )
