import pathlib

def load_input():
    return pathlib.Path("./input.txt").read_text().strip("\n").splitlines()

def run_interpreter(input):
    accumulator = 0
    visited_instructions = set()
    index = 0
    loop_detected = False
    while index < len(input):
        if (index in visited_instructions):
            loop_detected = True
            break

        visited_instructions.add(index)

        match input[index].split(" "):
            case ["nop"]:
                # Do nothing
                pass
            case ["acc", argument]:
                accumulator = accumulator + int(argument)
            case ["jmp", argument]:
                index = index + int(argument)
                continue

        index = index + 1

    return (accumulator, loop_detected, index)

if __name__ == "__main__":
    input = load_input()

    (accumulator, loop_detected, index) = run_interpreter(input)
    print("Part 1:\n  Accumulator Value: {0}".format(accumulator))

    change_index = 0
    (accumulator, loop_detected, index) = (0, False, 0)
    while (change_index < len(input)):
        instruction = input[change_index].split(" ")[0]
        if (instruction == "nop"):
            (accumulator, loop_detected, index) = run_interpreter(input[:change_index:] + [input[change_index].replace("nop", "jmp")] + input[change_index + 1::])
        elif (instruction == "jmp"):
            (accumulator, loop_detected, index) = run_interpreter(input[:change_index:] + [input[change_index].replace("jmp", "nop")] + input[change_index + 1::])

        if not loop_detected:
            print("Part 2:\n  Accumulator Value: {0}".format(accumulator))
            break
        change_index = change_index + 1

