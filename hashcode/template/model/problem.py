from __future__ import annotations


class Problem:

    def __init__(self):
        pass

    @staticmethod
    def parse_from(file_path: str) -> Problem:
        with open(file_path, "r") as file:
            for line in file:
                print("Parsing line: {}".format(line))
        return Problem()
