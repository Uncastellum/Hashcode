import os, sys
#import numpy as np
from radixsort import radixSort

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

books_norep, libs, days = 0,0,0
books_score = None
all_libs = None


class Library(object):
    """docstring for Library."""
    def __init__(self, id, total_b, singup, books_day, books):
        self.id = id
        self.total_b = total_b
        self.singup = singup
        self.books_day = books_day
        self.books = books
        self.total = (days-self.singup)*self.books_day
        self.score = 0
        for i in self.books:
            self.score += books_score[i]

    def __str__(self):
        string = '{0} {1} {2}\n{3}\n'
        return string.format(
            self.total_b,
            self.singup,
            self.books_day,
            ''.join('%s ' % i for i in self.books)
        )

    def __gt__(self, other):
        return self.score>other.score

    def __lt__(self, other):
        return self.score<other.score

    def __eq__(self, other):
        return self.id == other.id

    def _insertOrd(self, vector, dato, long):
    	i = 0
    	encontrado = False
    	while i < long and not encontrado:
    		if books_score[dato] >= books_score[i]:
    			vector.insert(i, dato)
    			encontrado = True
    		else:
    			i+=1
    	return vector

    def buscarXbest(self):
    	len = 0
    	res = []
    	for i in self.books:
    		if len == 0:
    			res.append(i)
    			len += 1
    		else:
    			res = self._insertOrd(res, i, len)
    			len += 1
    			if len >= self.total*3:
    				return res
    	return res


with open(input) as f_in:
    #read first line
    books_norep, libs, days = [int(x) for x in next(f_in).split()]
    books_score = [int(x) for x in next(f_in).split()]
    all_libs = []
    id = 0
    for line in f_in: # read rest of lines
        if len(line.replace('\n','')) is 0:
            continue
        b, d, s = [int(x) for x in line.split()]#next(f_in).split()]
        books = [int(x) for x in next(f_in).split()]#next(f_in).split()]
        all_libs.append(Library(id,b,d,s,books))
        id += 1
        #matrix.append([x for x in line]) #TTTTT

def delete_book(list_book):
    non_repeated_books = []
    for libro in list_book:
        if not repeat_book(libro):
            non_repeated_books.append(libro)

    return non_repeated_books

def resulttofile(l, res):
    with open(output_file, 'w') as f_out:
        f_out.write("%d\n" % l)
        for item in res:
            for subitem in item:
                #print(subitem)
                for subsubitem in subitem:
                    f_out.write("%d " % subsubitem)
                f_out.write("\n")
            #


def main():
    global days
    radixSort(all_libs)

    print(len(all_libs))
    #for x in all_libs:
        #print("%d " % x.id, end='')

    output = []
    libs = 0
    for i in all_libs:
        days -= i.singup
        if days < 0:
            break
        #days -= len(res)
        res = i.buscarXbest()
        output.append([[i.id, len(res)], res])
        libs +=1 
        
    resulttofile(libs, output)


if __name__ == '__main__':
    main()
