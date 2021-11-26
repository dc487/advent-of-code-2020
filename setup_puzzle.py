#!/usr/bin/python

import pathlib
import sys

if __name__ == "__main__":
    puzzle_name = sys.argv[1]
    pathlib.Path(puzzle_name).mkdir()
    pathlib.Path(puzzle_name + "/input").mkdir()
    pathlib.Path(puzzle_name + "/" + puzzle_name + ".py").write_text("import pathlib\n\n\nif __name__ == \"__main__\":\n\n")
