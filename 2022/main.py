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

def read_file(file):
    input = 'input/' + files[index]
    output_file = 'output_' + ['a', 'b', 'c', 'd', 'e', 'f'][index] + '.out'

    with open(input) as f_in:
        # read first line
        item1, item2, item3, item4, item5 = [int(x) for x in next(f_in).split()]
        streets_dict = {}
        for line in f_in:  # read rest of lines
            items = line.split()


def main():
    pass


if __name__ == '__main__':
    main()
