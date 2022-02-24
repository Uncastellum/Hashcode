import os, sys
import selector
from radixsort import *


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


class Skill:
    def __init__(self, skill_name, skill_level):
        self.skill_name = skill_name
        self.skill_level = skill_level

class Contributor:
    def __init__(self, name):
        self.name = name
        self.skills = {}

class Project:
    def __init__(self, name, days, score, best_before, n_roles):
        self.alex_score = 0
        self.name = name
        self.days = days
        self.score = score
        self.best_before = best_before
        self.n_roles = n_roles
        self.listaPersonas = []
        self.skills = {}

    def calculate_score(self):

        mean_skill = 0
        for skill in self.skills.values():
            mean_skill += skill
        mean_skill /= len(self.skills)

        self.alex_score = int(round(best_before * mean_skill))


class Result:
    #projects_programs = [ProjectProgram]

    def __init__(self, n_projects):
        self.n_projects = n_projects
        self.projects_programs = []



input = 'input/' + files[index]
output_file = 'output/output_' + ['a', 'b', 'c', 'd', 'e', 'f'][index] + '.out'

with open(input) as f_in:
    # Read first line
    n_contributors, n_projects = [int(x) for x in next(f_in).split()]
    for _ in range(n_contributors):
        # Read contributor info
        contributor_name, n_skills = [x for x in next(f_in).split()]
        n_skills = int(n_skills)
        new_contributor = Contributor(contributor_name)
        for _ in range(n_skills):
            # Read skills from contributor
            skill_name, skill_level = [x for x in next(f_in).split()]
            new_contributor.skills[skill_name] = int(skill_level)
        # Add contributor
        contributors.append(new_contributor)
    for _ in range(n_projects):
        # Read projects info
        project_name, days, score, best_before, n_roles = [x for x in next(f_in).split()]
        days = int(days)
        score = int(score)
        best_before = int(best_before)
        n_roles = int(n_roles)
        new_project = Project(project_name, days, score, best_before, n_roles)
        for _ in range(n_roles):
            # Read project info
            skill_name, skill_level = [x for x in next(f_in).split()]
            skill_level = int(skill_level)
            new_project.skills[skill_name] = int(skill_level)
        new_project.calculate_score()
        projects.append(new_project)
        pass


def result_to_file(output):
    with open(output_file, 'w') as f_out:
        f_out.write(str(len(output)) + '\n')
        for project in output:
            f_out.write(project.name + "\n")
            for person in project.listaPersonas:
                f_out.write(person.name + " ")
            f_out.write("\n")

def main():
    print(f"Reading from {input}")
    print(f"Writing to {output_file}")

    # Sort projects
    radixSort(projects, lambda x: x.alex_score)
    print([x.alex_score for x in projects])

    selector.elegirProyecto(projects, contributors)

    # Calculate solution
    result_to_file(output)


if __name__ == '__main__':
    main()
