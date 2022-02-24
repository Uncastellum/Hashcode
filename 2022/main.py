import os, sys

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
    skills = [Skill]

    def __init__(self, name):
        self.name = name

class Project:
    skills = [Skill]

    def __init__(self, name, days, score, best_before, n_roles):
        self.name = name
        self.days = days
        self.score = score
        self.best_before = best_before
        self.n_roles = n_roles


class ProjectProgram:
    project_name = ""
    contributors = []

    def __init__(self, project_name):
        self.project_name = project_name
        self.contributors = []

class Result:
    projects_programs = [ProjectProgram]

    def __init__(self, n_projects):
        self.n_projects = n_projects



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
            new_contributor.skills.append(Skill(skill_name, skill_level))
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
            new_project.skills.append(Skill(skill_name, skill_level))
        projects.append(new_project)
        pass


def result_to_file(res: Result):
    with open(output_file, 'w') as f_out:
        f_out.write(str(res.n_projects))
        for project_program in res.projects_programs:
            f_out.write(project_program.project_name + "\n")
            for contributor_name in project_program.contributors:
                f_out.write(contributor_name + "\n")

def main():
    print(f"Reading from {input}")
    print(f"Writing to {output_file}")
    # Calculate solution
    result = Result(n_projects)

    # Iterate through projects
    for project in projects:
        # Assign contributors to project
        print(f"Calculating {project.n_roles} contributors for project {project.name}")
        new_project_program = ProjectProgram(project.name)
        for i in range(project.n_roles):
            new_project_program.contributors.append(contributors[i].name)
        result.projects_programs.append(new_project_program)

    result_to_file(result)


if __name__ == '__main__':
    main()
