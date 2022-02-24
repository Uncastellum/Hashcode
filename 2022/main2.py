def main():
    print(f"Reading from {input}")
    print(f"Writing to {output_file}")

    # Sort projects
    radixSort(projects, lambda x: x.best_before)
    print([x.best_before for x in projects])
    indiceWhile = 0
    activeProjects = []
    output = []
    while(len(projects) != 0):

        for project in activeProjects:
            if project.days <= 0:
                for persona in project.personas:
                    contributors.append(persona)

                output.append(project)
            else:
                project.days -= 1


        (activeProjects,projects) = selector.elegirProyecto(projects, contributors)

        for i in range(len(projects), 0):
            if projects[i].best_before < indiceWhile - projects[i].days:
                projects.pop(i)


        indiceWhile += 1

