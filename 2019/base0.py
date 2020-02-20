import os
import time
import random as r
from heapq import merge


#input = 'input/a_example.txt'
#output_file = 'output_a.out'

input = 'input/b_lovely_landscapes.txt'
output_file = 'output_b.out'

#input = 'input/c_memorable_moments.txt'
#output_file = 'output_c.out'

#input = 'input/d_pet_pictures.txt'
#output_file = 'output_d.out'

#input = 'input/e_shiny_selfies.txt'
#output_file = 'output_e.out'



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


class ProgressBar:
    def __init__(self,maxvalue):
        if not isinstance(maxvalue, int):
            raise TypeError
        self.percent = 0.0
        self.value = 0
        self.max = maxvalue
        print('\rProgress . . . 0.0% | {}/{}'.format(self.value,self.max), end='', flush=True)
    def update(self, newvalue):
        if not isinstance(newvalue, int):
            raise TypeError
        self.value = newvalue
        self.percent = newvalue*100/self.max
        if self.percent < 100.0:
            print('\rProgress . . . {:3.2f}% | {:.0f}/{:.0f}'.format(self.percent,self.value,self.max), end='', flush=True)
        else:
            self.percent = 100.0
            print('\rProgress . . . {:3.0f}% | {:.0f}/{:.0f}     '.format(self.percent,self.value,self.max), end='\n')
            print("Done.")
        return self.percent


def factor_interes(slide1, slide2):
    esta = 0
    for i in slide1[1]:
        if i in slide2[1]:
            esta += 1

    return min([esta, len(slide1[1])-esta, len(slide2[1])-esta])


def enlazar():
    salida = []
    salida.append(slides.pop(0))

    PB = ProgressBar(numfotos[0])
    contador = 0

    while len(slides) > 0:
        maximo = 0
        aux = 0
        for i in range(len(slides)):
            if len(slides[i][1]) < maximo:
                continue
            numero = matching(salida[contador], slides[i])
            if numero > maximo:
                maximo = numero
                aux = i
        salida.append(slides.pop(aux))
        contador+=1
        PB.update(numfotos[0] - len(slides))


    return salida

def matching(photo1, photo2):
    matchingsi = 0
    for i in photo1[1]:
        if i in photo2[1]:
            matchingsi+= 1
            continue
    return matchingsi

def emparejar():
    maximo = 99999999
    #numrandom= r.randint(0,len(V)-1)
    numrandom = 0
    random = V.pop(numrandom)
    elegida = V.pop()
    #numeroelegida = 0
    for i in range(len(V)):
        numero = matching(random, V[i])
        if numero < maximo:
            maximo = numero
            V.append(elegida)
            elegida = V.pop(i)


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
    start = time.clock()

    while len(V) >= 1:
        slides.append(emparejar())

    end1 = time.clock()
    print((end1 - start))

    output_value = enlazar()

    end2 = time.clock()
    print("%s \n" % (end2 - end1))

    output(output_value)

    end3 = time.clock()
    print("%s \n" % (end3 - end2))
    #testoutput()


if __name__ == '__main__':
    main()
