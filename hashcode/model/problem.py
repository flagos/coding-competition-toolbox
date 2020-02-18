from __future__ import annotations
from typing import List


class Problem:

    def __init__(self, name: str, max_slices_to_order: int, pizza_sizes: List[int]):
        self.name = name
        self.max_slices_to_order = max_slices_to_order
        self.pizza_sizes = pizza_sizes

    @staticmethod
    def parse_from(file_path: str, name: str) -> Problem:
        with open(file_path, "r") as file:
            m, n = map(int, file.readline().split())
            pizzas = [int(p) for p in file.readline().split()]
        return Problem(name=name, max_slices_to_order=m, pizza_sizes=pizzas)
