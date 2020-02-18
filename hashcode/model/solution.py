from __future__ import annotations

import abc
import pickle
from hashcode.model.problem import Problem


# Required for genetic algorithm
def crossover(sol1: Solution, sol2: Solution) -> Solution:
    pizzas = set(sol1.pizzas + sol2.pizzas)
    while sum(pizzas) > sol1.problem.max_slices_to_order:
        pizzas.pop()
    return Solution(sol1.problem, pizzas)


def mutation(sol: Solution) -> Solution:
    pizzas = sol.pizzas.pop()
    sol.pizzas = pizzas
    return sol


def evaluate(sol: Solution) -> float:
    return sol.compute_score()


class Solution:

    def __init__(self, problem: Problem, pizzas=None):
        if pizzas is None:
            pizzas = []
        self.problem = problem
        self.pizzas = pizzas

    @staticmethod
    @abc.abstractmethod
    def generate_solution(problem: Problem) -> Solution:
        print("Computing solution")
        nb_slices = 0
        current_idx = 0
        pizzas = []
        while nb_slices + problem.pizza_sizes[current_idx] < problem.max_slices_to_order:
            nb_slices += problem.pizza_sizes[current_idx]
            pizzas.append(current_idx)
            current_idx += 1
        return Solution(problem, pizzas)

    def build_out_file(self, path: str):
        with open(path, "w") as file:
            file.write(str(len(self.pizzas)) + "\n")
            file.write(" ".join(map(str, self.pizzas)))

    def serialize(self, path: str):
        with open(path, "wb") as file:
            pickle.dump(self, file)

    def compute_score(self) -> float:
        return sum(self.problem.pizza_sizes[p] for p in self.pizzas)

    @staticmethod
    def crossover(sol1: Solution, sol2: Solution) -> Solution:
        return sol1

    @staticmethod
    def mutation(sol: Solution) -> Solution:
        return sol

    @staticmethod
    def evaluate(sol: Solution) -> float:
        return sol.compute_score()
