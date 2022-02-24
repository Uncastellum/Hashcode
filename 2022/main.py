import os, sys
from ObjDefs import *

# import numpy as np

files = [
    'a_an_example.in.txt',
    'b_better_start_small.in.txt',
    'c_collaboration.in.txt',
    'd_dense_schedule.in.txt',
    'e_exceptional_skills.in.txt',
    'f_find_great_mentors.in.txt'
]

args = sys.argv[1:]
index = 0
if len(args) != 0:
    file = args[0]
    if file in ['a', 'b', 'c', 'd', 'e', 'f']:
        index = ['a', 'b', 'c', 'd', 'e', 'f'].index(file)
    elif file in ['1', '2', '3', '4', '5', '6']:
        index = ['1', '2', '3', '4', '5', '6'].index(file)

contributors = []
projects = []


class Project:

    def __init__(self, name, days, score, best_before, n_roles):
        self.name = name
        self.days = days
        self.score = score
        self.best_before = best_before
        self.n_roles = n_roles


class Contributor:
    skills = []

    def __init__(self, name):
        self.name = name


class Skill:

    def __init__(self, skill_name, skill_level):
        self.skill_name = skill_name
        self.skill_level = skill_level


input = 'input/' + files[index]
output_file = 'output_' + ['a', 'b', 'c', 'd', 'e', 'f'][index] + '.out'

with open(input) as f_in:
    # Read first line
    n_contributors, n_projects = [int(x) for x in next(f_in).split()]
    for _ in range(n_contributors):
        # Read contributor info
        line = next(f_in)  # NEXT LINE
        contributor_name, n_skills = [x for x in line.split()]
        new_contributor = Contributor(contributor_name)
        for _ in range(n_skills):
            # Read skills from contributor
            line = next(f_in)  # NEXT LINE
            skill_name, skill_level = [x for x in line.split()]
            new_contributor.skills.append(Skill(skill_name, skill_level))
        # Add contributor
        contributors.append(new_contributor)
    for _ in range(n_projects):
        # Read projects info
        # TODO
        pass


def main():
    # Calculate solution
    pass


if __name__ == '__main__':
    main()
