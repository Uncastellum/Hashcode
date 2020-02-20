import os
import numpy as np
import random as r
from heapq import merge

input = 'input/a_example.txt'
output_file = 'output_a.out'

#input = 'input/b_lovely_landscapes.txt'
#output_file = 'output_b.out'

#input = 'input/c_memorable_moments.txt'
#output_file = 'output_c.out'

#input = 'input/d_pet_pictures.txt'
#output_file = 'output_d.out'

#input = 'input/e_shiny_selfies.txt'
#output_file = 'output_e.out'


interes = 1

with open(input) as f_in:
    # read first line
    numfotos = [int(x) for x in next(f_in).split()]
    matrix = []
    for line in f_in: # read rest of lines
        matrix.append([x for x in line.split()])
    V = []
    slides = []
    integercounter = 0
    for element in matrix:
        tmp = []
        tmptags = []
        tmp.append(str(integercounter))
        for i in range(int(element[1])):
            tmptags.append(element[2+i])
        tmp.append(tmptags)
        if element[0] is 'V':
            V.append(tmp)
        elif element[0] is 'H':
            slides.append(tmp)
        integercounter = integercounter + 1
    del matrix


def factor_interes(slide1, slide2):
    esta = 0
    for i in slide1[1]:
        if i in slide2[1]:
            esta += 1

    return min([esta, len(slide1[1])-esta, len(slide2[1])-esta])

"""
def enlazar():
    #global slides
    salida = []
    salida.append(slides.pop(r.randint(0, len(slides)-1)))

    while len(slides) > 1:
        i = 0
        encontrado = False
        while i < len(slides) and not encontrado:
            if factor_interes(salida[-1], slides[i]) >= interes:
                #print(len(slides))
                salida.append(slides[i])
                slides.remove(slides[i])
                encontrado = True

            i+=1

    salida.append(slides[0])
    return salida
"""

def enlazar():
    #global slides
    salida = []
    salida.append(slides.pop(r.randint(0, len(slides)-1)))
    while len(slides) > 1:
        i = r.randint(0, len(slides)-1)
        j = slides[i]

        salida.append(j)
        del slides[i]

    salida.append(slides[0])
    return salida


def matching(photo1, photo2):
    matchingsi = 0
    for i in range(len(photo1[1])):
        for j in range(len(photo2 [1])):
            if(photo1[1][i] == photo2[1][j]):
                matchingsi+= 1
    return matchingsi

def emparejar():
    maximo = 99999999
    numrandom = 0
    random = V.pop(numrandom)
    elegida = V.pop()
    #numeroelegida = 0
    '''
    for i in range(0, len(V)-1):
        numero = matching(random, V[i])
        if numero < maximo:
            maximo = numero
            V.append(elegida)
            elegida = V.pop(i)
            '''


    final = []
    final.append(random[0] + ' ' + elegida[0])
    final.append(list(merge(random[1], elegida[1])))

    return final



def output(res):
    with open(output_file, 'w') as f_out:
        f_out.write("%s\n" % len(res))
        for item in res:
            #f_out.write("%s " % item[0])
            f_out.write(item[0])
            f_out.write("\n")



def testoutput():
    with open(output, 'w') as f_out:
        for item in V:
            for subitem in item:
                f_out.write("%s " % subitem)
            f_out.write("\n")
        for item in slides:
            for subitem in item:
                f_out.write("%s " % subitem)
            f_out.write("\n")


def main():
    #Codigo aqui

    while len(V) >= 1:
        slides.append(emparejar())

    output_value = enlazar()

    output(output_value2)
    #testoutput()


if __name__ == '__main__':
    main()
