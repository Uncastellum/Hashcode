import os
#import numpy as np


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


import random as r

def factor_interes(slide1, slide2, interes):
    encontrados = 0
    encontrado = False
    i = 0
    while i < slide1[1] and not encontrado:
        if slide1[2][i] in slide2[2]:
            encontrados += 1
            if encontrados >= interes:
                encontrado = True
        i += 1
    return encontrado

def enlazar():
    global slides
    salida = []
    long = len(slides)
    salida.append(slides.pop(0))

    while len(slides) > 1:
            encontrado = False
            i = 0
            interes = 8
            while i < len(slides) and not encontrado:

                if factor_interes(salida[-1], slides[i], interes):
                    salida.append(slides[i])
                    del slides[i]
                    encontrado = True

                    print(len(slides))

                i += 1

            if not encontrado:
                    salida.append(slides.pop())

    salida.append(slides[0])

    return salida

def burbuja(lista):
    num = len(lista)
    i = 0
    while i < num:
          j = i
          while j < num:
                  if lista[i] > lista[j]:
                          aux = lista[i]
                          lista[i] = lista[j]
                          lista[j] = aux
                  j = j + 1
          i = i + 1

def emparejar():

    a = V[0][0] + ' ' + V[len(V)-1][0]
    V[0][2].extend([element for element in V[len(V)-1][2] if element not in V[0][2]])
    slides.append([a,len(V[0][2]),V[0][2]])
    del V[len(V)-1]
    del V[0]

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
        tmp.append(int(element[1]))

        for i in range(int(element[1])):

            tmptags.append(element[2+i])

        tmp.append(tmptags)

        if element[0] is 'V':
            if tmp[1] > 18:

                V.append(tmp)

            else:

                V.insert(0, tmp)

        elif element[0] is 'H':

            slides.append(tmp)

        integercounter = integercounter + 1









def testoutput(salida):

    with open(output, 'w') as f_out:
        f_out.write(str(len(salida)))
        f_out.write('\n')

        for item in salida:

            f_out.write(item[0])
            f_out.write("\n")





def main():
    print(len(slides))
    '''if len(V) > 2:

        burbuja(V)
    '''
    print("emparejando")
    while len(V) > 1:
        emparejar();
    salida = []
    for i in V:
        salida.append(i)

    print("enlazando\n")
    salida.extend(enlazar())
    print(len(salida))
    print(len(slides))
    print("escribiendo\n")

    testoutput(salida)





if __name__ == '__main__':

    main()
