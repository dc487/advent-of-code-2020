import pathlib

class _SeatNumber:
    def __init__(self, boarding_pass):
        row_number_code = boarding_pass[:7:]
        seat_number_code = boarding_pass[-3::]
        self.row_number = int(row_number_code.replace("F", "0").replace("B", "1"), 2)
        self.seat_number = int(seat_number_code.replace("L", "0").replace("R", "1"), 2)

    def get_seat_id(self):
        return self.row_number * 8 + self.seat_number

def load_boarding_passes(boarding_passes_location):
    return [_SeatNumber(x) for x in pathlib.Path(boarding_passes_location).read_text().splitlines()]

if __name__ == "__main__":
    boarding_passes = load_boarding_passes("./input/boarding_passes.txt")
    seat_ids = [x.get_seat_id() for x in boarding_passes]

    # Part 1
    highest_seat_number = max(seat_ids)
    print("Part 1:\n  Highest Seat ID: {0}".format(highest_seat_number))

    # Part 2
    seat_id_set = set(seat_ids)
    missing_ids = [x for x in range(822) if x not in seat_id_set and x - 1 in seat_id_set and x + 1 in seat_id_set]
    print("Part 2:\n  My Seat ID: {0}".format(missing_ids[0]))
