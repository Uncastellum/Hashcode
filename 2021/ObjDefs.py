import math as m

class Car(object):
    """docstring for Car."""
    def __init__(self, nstr, lstr):
        super(Car, self).__init__()
        self.numstr = nstr
        self.streets = lstr

class Street(object):
    """docstring for Street."""
    def __init__(self, name, time):
        super(Street, self).__init__()
        self.name = name
        self.time = time
        self.totalcars = 0
        self.peso = 0
        self.tiempo_final = 0

    def addcar(self):
        self.totalcars += 1


class Grafo(object):
    """docstring for Grafo."""
    def __init__(self, N):
        self.mtx_street = []
        for i in range(N):
            self.mtx_street.append([None]*N)

    def __str__(self):
        final = {}
        for it1 in range(len(self.mtx_street)):
            list_streets = self.mtx_street[it1]
            list_streets = [x for x in list_streets if x is not None]
            # list_streets es una lista con instancias de Street
            on_representation = False
            for street in list_streets:
                if street.tiempo_final > 0:
                    if not on_representation:
                        final[it1] = [street]
                        on_representation = True
                    else:
                        aux = final[it1]
                        aux.append(street)
                        final[it1] = aux

        str = f"{len(final)}\n"
        for x,y in final.items():
            str = str + f"{x}\n{len(y)}\n"
            for it2 in y:
                str = str + f"{it2.name} {round(it2.tiempo_final)}\n"
        return str

    def addstr(self, begin, end, street):
        self.mtx_street[end][begin] = street

    def get_intersection_semaphores(self, i):
        return self.mtx_street[i]

    def asignar_pesos(self):
        for intersect in self.mtx_street:
            lista_calles = [x for x in intersect if x is not None]
            #lista_calles es una lista con objetos que son calles
            for calle in lista_calles:
                calle.peso = calcularPeso(calle)

def calcularPeso(street):
    return heuristica(street.time, street.totalcars)

def heuristica(time, coches):
    if coches == 0:
        return 0
    return m.log(1 + time) * m.log(coches)


def asignarTiempo(interseccion, simulation_time):

    s_time = simulation_time
    suma = 0
    # First pass - calculate weights
    for calle in interseccion:
        if(calle.peso > 0):
            suma += calle.peso
    # Second pass - normalize weights
    for calle in interseccion:
        if(calle.peso > 0):
            calle.peso = calle.peso / suma
        # Calculate seconds in green per cycle
        calle.tiempo_final = min(calle.peso * s_time, calle.time)

"""
 def asignarTiempo2(interseccion, simulation_time):

    s_time = 0
    suma = 0
    count = 0
    # First pass - calculate weights
    for calle in interseccion:
        if(calle.peso > 0):
            suma += calle.Peso
            count += 1

    if simulation_time <= count:
        s_time = simulation_time
    else:


    # Second pass - normalize weights
    for calle in interseccion:
        if(calle.peso > 0):
            calle.peso = calle.peso / suma
        # Calculate seconds in green per cycle
        calle.tiempo_final = min(calle.peso * s_time, calle.tiempo)
"""
"""
Aqui para escribir:


Lista de intersecciones:
 -> Lista de semaforos/calle entrada
    -> Nombre de la calle (ID)
    -> Tiempo de calle
    -> Total de coches que pasan por esa calle
    -> Peso (0 por defecto)

Función que calcula el peso en función de una heuristica:
->

Función heuristica:
-> Si no pasan coches, 0 puntos

Función que asigna tiempos en función del Peso
-> Si Nº coches  = 0, no se le da tiempo
-> Entrada: Interseccion, Tiempo de simulacion

Función que escribe la salida
"""
