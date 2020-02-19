from __future__ import annotations

import abc
import pickle
from hashcode.template.model.problem import Problem


# Required for genetic algorithm
def crossover(sol1: Solution, sol2: Solution) -> Solution:
    return sol1


def mutation(sol: Solution) -> Solution:
    return sol


def evaluate(sol: Solution) -> float:
    return sol.compute_score()


class Solution:

    def __init__(self, problem: Problem):
        self._problem = problem
        self._generate_solution()

    @abc.abstractmethod
    def _generate_solution(self):
        print("Computing solution")
        self.slide = []

    def build_out_file(self, path: str):
        with open(path, "w") as file:
            file.write("Dummy solution")

    def serialize(self, path: str):
        with open(path, "wb") as file:
            pickle.dump(self, file)

    def compute_score(self) -> float:
        return

    @staticmethod
    def crossover(sol1: Solution, sol2: Solution) -> Solution:
        return sol1

    @staticmethod
    def mutation(sol: Solution) -> Solution:
        return sol

    @staticmethod
    def evaluate(sol: Solution) -> float:
        return sol.compute_score()
