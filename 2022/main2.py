import os, sys
import selector
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
        self.listaPersonas = []
        self.skills = {}


class Contributor:
    

    def __init__(self, name):
        self.name = name
        self.skills = {}


class Skill:

    def __init__(self, skill_name, skill_level):
        self.skill_name = skill_name
        self.skill_level = skill_level


input = 'input/' + files[index]
output_file = 'output_' + ['a', 'b', 'c', 'd', 'e', 'f'][index] + '.out'

'''with open(input) as f_in:
    # Read first line
    n_contributors, n_projects = [int(x) for x in next(f_in).split()]
    for _ in range(n_contributors):
        # Read contributor info
        line = next(f_in)  # NEXT LINE
        contributor_name, n_skills = [x for x in line.split()]
        new_contributor = Contributor(contributor_name)
        for _ in range(int(n_skills)):
            # Read skills from contributor
            line = next(f_in)  # NEXT LINE
            skill_name, skill_level = [x for x in line.split()]
            new_contributor.skills.append(Skill(skill_name, skill_level))
        # append contributor
        contributors.append(new_contributor)
    for _ in range(n_projects):
        # Read projects info
        line = next(f_in)  # NEXT LINE
        project_name, days, score, best_before, n_roles = [x for x in line.split()]
        new_project = Project(project_name, days, score, best_before, n_roles)
        for _ in range(n_roles):
            # Read project info
            new_project.skills.append(Skill(skill_name, skill_level))
        projects.append(new_project)
        pass'''


def main():
    # Calculate solution
    Anna = Contributor("Anna")
    Anna.skills["C++"] = 2
    Bob = Contributor("Bob")
    Bob.skills["HTML"] = 5
    Bob.skills["CSS"] = 5
    Maria = Contributor("Maria")
    Maria.skills["Python"] = 3
    
    proyectos = []
    logging = Project("Logging", 5, 10, 5, 1)
    logging.skills["C++"] = 3

    webServer = Project("WebServer", 7, 10, 7, 2)
    webServer.skills["HTML"] = 3
    webServer.skills["C++"] = 2

    webChat = Project("WebChat", 10, 20, 20, 2)
    webChat.skills["HTML"] = 3
    webChat.skills["Python"] = 3

    a = selector.elegirProyecto([logging, webServer, webChat], [Anna, Bob, Maria])
    for p in a:
        print(p.name, p.listaPersonas)


if __name__ == '__main__':
    main()
