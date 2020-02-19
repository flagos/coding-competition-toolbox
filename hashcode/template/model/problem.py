from __future__ import annotations


class Problem:

    def __init__(self, nb_lines, pictures):
        self.nb_lines = nb_lines
        self.pictures = []
        self.horizontal = []
        self.vertical = []
        index = 0
        for p in pictures:
            split = p.split(' ')
            d = {'direction': split[0], 'tags': set(split[2:])}
            self.pictures.append(d)
            if d['direction'] == 'H':
                self.horizontal.append(index)
            else:
                self.vertical.append(index)
            index += 1

    @staticmethod
    def parse_from(file_path: str, name: str) -> Problem:

        with open(file_path, "r") as file:
            nb_lines = file.read()
            pictures = []
            for line in file:
                pictures.append(line)
        return Problem(nb_lines, pictures)
