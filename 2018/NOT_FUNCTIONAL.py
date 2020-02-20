import os
import numpy as np

file = 'a_example.in'
#file = 'b_should_be_easy.in'


with open(file) as f:
    # read first line
    rows, colums, numvehicles, rides, bonus, steps = [int(x) for x in next(f).split()]
    totalrides = []
    for line in f: # read rest of lines
        totalrides.append([int(x) for x in line.split()])
    totalridesORIGINAL = totalrides [:]
    totalrides2 = totalrides [:]


def getKey(item):
    return item[5]

def newinstruction(car, vehicles, numrides):
    vehicles[car].append(numrides)


def newstep(vehicles, numrides):
    for car in range(numvehicles):
        if vehicles[car][1] < totalridesORIGINAL[vehicles[car][len(vehicles[car]) - 1]][0]:
            vehicles[car][1] = vehicles[car][1] + 1
        elif vehicles[car][1] > totalridesORIGINAL[vehicles[car][len(vehicles[car]) - 1]][0]:
            vehicles[car][1]= vehicles[car][1] - 1
        elif vehicles[car][1] == totalridesORIGINAL[vehicles[car][len(vehicles[car]) - 1]][0]:
            if vehicles[car][2] < totalridesORIGINAL[vehicles[car][len(vehicles[car]) - 1]][1]:
                vehicles[car][2] = vehicles[car][2] + 1
            elif vehicles[car][2] > totalridesORIGINAL[vehicles[car][len(vehicles[car]) - 1]][1]:
                vehicles[car][2] = vehicles[car][2] - 1
            #else:
                #newinstruction(car, vehicles, numrides)

def main():
    totalrides.sort(key=getKey)
    vehicles = []
    numrides = 0
    for car in range(numvehicles):
        totalrides2.pop(0)
        numrides = numrides + 1
        #vehicle = [numcoche, posx, posy, viajes , viajequeestahaciendo]
        vehicles.append([car+1, 0, 0,1, car])
    print(totalrides)
    #START STEPS
    for i in range(1,steps):
        newstep(vehicles, numrides)
    print(vehicles)

if __name__ == '__main__':
    main()
