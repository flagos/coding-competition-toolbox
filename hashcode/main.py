import calendar
import time
from os import listdir, mkdir
from os.path import isfile, join

import click

from hashcode.template.model.problem import Problem
from hashcode.template.model.solution import Solution


@click.group()
def main():
    pass


@main.command()
@click.option("-i", "--input_path", help="Path to folder containing test cases", default="test_cases")
@click.option("-o", "--output_path", help="Path to folder to store solutions", default="out")
def compute_solutions(input_path: str, output_path: str):
    # Build directory for solutions
    sol_folder = "{}/sol_{}".format(output_path, calendar.timegm(time.gmtime()))
    mkdir(sol_folder)

    # Run test cases
    test_cases = [f for f in listdir(input_path) if isfile(join(input_path, f))]
    for test_case in test_cases:
        print("Processing test case {}".format(test_case))
        problem = Problem.parse_from(file_path=join(input_path, test_case))
        solution = Solution(problem=problem)
        sol_file_path = "{}/{}".format(sol_folder, test_case)
        solution.serialize(sol_file_path)
        print("Score on for test case {} : {} \n".format(test_case, solution.compute_score()))


if __name__ == "__main__":
    main()
