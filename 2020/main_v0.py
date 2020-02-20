import os, sys
#import numpy as np

files = [
    'a_example.txt',
    'b_read_on.txt',
    'c_incunabula.txt',
    'd_tough_choices.txt',
    'e_so_many_books.txt',
    'f_libraries_of_the_world.txt'
]

args = sys.argv[1:]
index = 0
if len(args) != 0:
    file = args[0]
    if file in ['a', 'b', 'c', 'd', 'e', 'f']:
        index = ['a', 'b', 'c', 'd', 'e', 'f'].index(file)
    elif file in ['1', '2', '3', '4', '5', '6']:
        index = ['1', '2', '3', '4', '5', '6'].index(file)

input = 'input/' + files[index]
output_file = 'output_' + ['a', 'b', 'c', 'd', 'e', 'f'][index] + '.out'

with open(input) as f_in:
    #read first line
    #rows, colums, miningr, maxcells = [int(x) for x in next(f_in).split()]
    matrix = []
    for line in f_in: # read rest of lines
        matrix.append([x for x in line]) #TTTTT


def resulttofile(res):
    with open(output_file, 'w') as f_out:
        for item in res:
            for subitem in item:
                f_out.write("%s " % subitem)
            f_out.write("\n")


def main():
    resulttofile(matrix)


if __name__ == '__main__':
    main()
