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

class Libary(object):
    """docstring for Libary."""
    def __init__(self, id, total_b, singup, books_day, books):
        self.id = id
        self.total_b = total_b
        self.singup = singup
        self.books_day = books_day
        self.books = books

    def __str__(self):
        string = '{0} {1} {2}\n{3}\n'
        return string.format(
            self.total_b,
            self.singup,
            self.books_day,
            ''.join('%s ' % i for i in self.books)
        )

with open(input) as f_in:
    #read first line
    books_norep, libs, days = [int(x) for x in next(f_in).split()]
    books_score = [int(x) for x in next(f_in).split()]
    all_libs = []
    id = 0
    for line in f_in: # read rest of lines
        b, d, s = [int(x) for x in line.split()]#next(f_in).split()]
        books = [int(x) for x in next(f_in).split()]#next(f_in).split()]
        all_libs.append(Libary(id,b,d,s,books))
        id += 0
        #matrix.append([x for x in line]) #TTTTT


def resulttofile(res):
    with open(output_file, 'w') as f_out:
        for item in res:
            f_out.write("%s" % item)
            f_out.write("\n")
            #for subitem in item:


def main():
    print(len(all_libs))
    resulttofile(all_libs)


if __name__ == '__main__':
    main()
