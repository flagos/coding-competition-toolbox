from __future__ import annotations


class Problem:

    def __init__(self, name: str):
        self.name = name

    @staticmethod
    def parse_from(file_path: str, name: str) -> Problem:
        with open(file_path, "r") as file:
            for line in file:
                print("Parsing line: {}".format(line))
        return Problem(name=name)
