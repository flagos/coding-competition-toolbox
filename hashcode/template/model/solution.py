import abc
from hashcode.template.model.problem import Problem


class Solution:

    def __init__(self, problem: Problem):
        self._problem = problem
        self._generate_solution()

    @abc.abstractmethod
    def _generate_solution(self):
        print("Computing solution")
        pass

    def serialize(self, path: str):
        with open(path, "w") as file:
            file.write("Dummy solution")

    def compute_score(self) -> float:
        return 0
