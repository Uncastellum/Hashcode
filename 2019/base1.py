import os
import time
import random as r


#input = 'input/a_example.txt'
#output_file = 'output_a.out'

#input = 'input/b_lovely_landscapes.txt'
#output_file = 'output_b.out'

#input = 'input/c_memorable_moments.txt'
#output_file = 'output_c.out'

input = 'input/d_pet_pictures.txt'
output_file = 'output_d.out'

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
    dict = {}
    integercounter = 0
    tags = 0
    for element in matrix:
        tags = tags + int(element[1])
        tmp = []
        tmptags = []
        tmp.append(str(integercounter))
        for i in range(int(element[1])):
            tmptags.append(element[2+i])
        for tag in tmptags:
            if tag not in dict:
                dict[tag] = 1
            else:
                dict[tag] += 1
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
    for elem in slides:
        if len(elem[1]) == 0:
            salida.append(elem)
            slides.remove(elem)
            print("+1")


    tot = len(slides)
    PB = ProgressBar(tot)
    salida.append(slides.pop(0))

    if len(salida) < 1:
        contador = len(salida)-1
    else:
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
        PB.update(tot - len(slides))

    return salida

def matching(photo1, photo2):
    matchingsi = 0
    for i in photo1[1]:
        if i in photo2[1]:
            matchingsi+= 1
            continue
    return matchingsi

def merge_list(list1,list2):
    final = []
    for elem in list1:
        if elem in list2:
            dict[elem]-=1
            continue
        final.append(elem)
    for elem in list2:
        final.append(elem)
    return final

def emparejar():
    maximo = 99999999
    #numrandom= r.randint(0,len(V)-1)
    numrandom = 0
    random = V.pop(numrandom)
    elegida = V.pop()
    for i in range(len(V)):
        numero = matching(random, V[i])
        if numero < maximo:
            maximo = numero
            V.append(elegida)
            elegida = V.pop(i)
        if maximo == 0:
            break

    final = []
    final.append(random[0] + ' ' + elegida[0])
    final.append(merge_list(random[1], elegida[1]))

    return final

def cleantags(mtx):
    print("\nCleaning tags . . .")
    print("Total tags: {}".format(tags))

    counter1 = 0
    counter2 = 0
    PB = ProgressBar(tags)
    for elem in mtx:
        borrados = 0
        for i in range(len(elem[1])):
            counter2+=1
            PB.update(counter2)
            if dict.get(elem[1][i-borrados]) == 1:
                elem[1].pop(i-borrados)
                counter1+=1
                borrados+=1

    print(counter1)

def output(res):
    with open(output_file, 'w') as f_out:
        f_out.write("%s\n" % len(res))
        for item in res:
            #f_out.write("%s " % item[0])
            f_out.write(item[0])
            f_out.write("\n")

def testoutput(mtx):
    with open("output_test.txt", 'w') as f_out:
        for item in mtx:
            for subitem in item:
                f_out.write("%s " % subitem)
            f_out.write("\n")

def main():
    #Codigo aqui
    print("\nStarting . . .")
    print("Input File: {}".format(input))

    allV = False

    tot = len(V)
    if tot > 0:
        if len(slides) == 0:
            print("Only vertical photos detected!")
            allV = True
            t_time = time.clock()
            cleantags(V)
            print((time.clock() - t_time))
        t_time = time.clock()
        print("\nMixing Vertical photos . . .")
        PB = ProgressBar(tot)
        while len(V) >= 1:
            slides.append(emparejar())
            PB.update(tot - len(V))
        print((time.clock() - t_time))
    else:
        print("\nMixing Vertical photos . . .")
        print("0 Detected.")


    if not allV:
        t_time = time.clock()
        cleantags(slides)
        print((time.clock() - t_time))

    t_time = time.clock()

    print("\nCreating Slideshow. . .")
    output_value = enlazar()

    print((time.clock() - t_time))

    print("\nExporting file. . .")
    output(output_value)

    print("Done.")
    time.sleep(2)



if __name__ == '__main__':
    main()
