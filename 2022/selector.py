import random
def selector(skill, listaPersonas):
    encontrado = False
    random.seed()
    limite = 10
    i = 0
    while i < limite and len(listaPersonas) != 0:
        randomNumber = random.randint(0, len(listaPersonas) - 1)
        persona = listaPersonas[randomNumber]
        (name, lvl) = skill
        if name in persona.skills and  persona.skills[name] >= lvl:
            return listaPersonas.pop(randomNumber)
        else:
            i += 1
    return None


def proyectSelector(proyecto, listaPersonas):
    for skill in proyecto.skills:
        persona = selector((skill, proyecto.skills[skill]), listaPersonas)
        if persona == None:
            for p in proyecto.listaPersonas:
                listaPersonas.append(p)
            return False
        proyecto.listaPersonas.append(persona)
    return True


def elegirProyecto(listaProyectos, listaPersonas):
    proyectOutput = []
    for proyecto in listaProyectos:
        if proyectSelector(proyecto, listaPersonas):
            proyectOutput.append(proyecto)
    return proyectOutput
