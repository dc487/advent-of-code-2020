import pathlib

def load_map(map_location):
    return [x for x in pathlib.Path(map_location).read_text().splitlines()]

def get_visited_locations(map, right, down):
    visited_rows = map[::down]
    visited_columns = [right*x for x in range(0, len(visited_rows))]
    return [x[0][x[1] % len(x[0])] for x in zip(visited_rows, visited_columns)]

if __name__ == "__main__":
    map = load_map("./input/map.txt")

    # Part 1
    visited_locations = get_visited_locations(map, 3, 1)
    tree_count = visited_locations.count("#")
    print(tree_count)

    # Part 2
    print(
        get_visited_locations(map, 1, 1).count("#") *
        get_visited_locations(map, 3, 1).count("#") *
        get_visited_locations(map, 5, 1).count("#") *
        get_visited_locations(map, 7, 1).count("#") *
        get_visited_locations(map, 1, 2).count("#")
    )
