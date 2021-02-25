import os, sys
from ObjDefs import *
#import numpy as np

files = [
    'a.txt',
    'b.txt',
    'c.txt',
    'd.txt',
    'e.txt',
    'f.txt'
]

args = sys.argv[1:]
index = 0
if len(args) != 0:
    file = args[0]
    if file in ['a', 'b', 'c', 'd', 'e','f']:
        index = ['a', 'b', 'c', 'd', 'e','f'].index(file)
    elif file in ['1', '2', '3', '4', '5','6']:
        index = ['1', '2', '3', '4', '5','6'].index(file)

input = 'input/' + files[index]
output_file = 'output_' + ['a', 'b', 'c', 'd', 'e', 'f'][index] + '.out'

with open(input) as f_in:
    # read first line
    simulation_time, n_intersections, streets, n_cars, ppcar = [int(x) for x in next(f_in).split()]
    streets_dict = {}
    cars = []
    aux = 0
    gr = Grafo(n_intersections)
    for line in f_in: # read rest of lines
        items = line.split()
        if aux < streets: # read street
            # example: 2 0 rue-de-londres 1
            streets_dict[items[2]] = Street(items[2], int(items[3]))
            gr.addstr(int(items[0]), int(items[1]), streets_dict[items[2]])
        else: # cars
            # example: 4 rue-de-londres rue-d-amsterdam rue-de-moscou rue-de-rome
            n_streets = items.pop(0)
            # now items only with street names
            streets_path = []
            for street_name in items: # get references to objects
                streets_dict[street_name].addcar()
                streets_path.append(streets_dict[street_name])
            cars.append(Car(n_streets, streets_path))
        aux += 1


def resulttofile(res):
    with open(output_file, 'w') as f_out:
        f_out.write("%s" % res)


def main():
    gr.asignar_pesos()
    for inter in gr.mtx_street:
        asignarTiempo([x for x in inter if x is not None],  simulation_time)
    resulttofile(gr)


if __name__ == '__main__':
    main()
