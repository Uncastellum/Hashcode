import os, sys
#from math import ceil
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

books_norep, libs, days = 0,0,0
factor = 0.0
books_score = None
all_libs = None

def mergeSort(arr):
    if len(arr) >1:
        mid = len(arr)//2 #Finding the mid of the array
        L = arr[:mid] # Dividing the array elements
        R = arr[mid:] # into 2 halves

        mergeSort(L) # Sorting the first half
        mergeSort(R) # Sorting the second half

        i = j = k = 0

        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i+=1
            else:
                arr[k] = R[j]
                j+=1
            k+=1

        # Checking if any element was left
        while i < len(L):
            arr[k] = L[i]
            i+=1
            k+=1

        while j < len(R):
            arr[k] = R[j]
            j+=1
            k+=1

class Library(object):
    """docstring for Library."""
    def __init__(self, id, different_books, signup_days, speed, books):
        global days
        self.id = id
        self.different_books = different_books
        self.signup_days = signup_days
        self.speed = speed
        self.books = books
        self.score = 0
        self.total_books = 0
        for i in self.books:
            self.score += books_score[i]
            self.total_books += 1
        self.max_books = min(self.speed * (days-self.signup_days),self.total_books)
        self.score_alex = (self.score*self.max_books)/self.signup_days

    def getScore(self):
        return self.score_alex

    def updateScore(self):
        self.score = 0
        self.total_books = 0
        for i in self.books:
            self.score += books_score[i]
            self.total_books += 1
        self.max_books = min(self.speed * (days-self.signup_days),self.total_books)
        self.score_alex = (self.score*self.max_books)/self.signup_days

    def __str__(self):
        string = '{0} {1} {2}\n{3}\n'
        return string.format(
            self.different_books,
            self.signup_days,
            self.speed,
            ''.join('%s ' % i for i in self.books)
        )

    def __truediv__(self, other):
        #print(self.id, self.score_alex, other)
        return self.score/other
    def __floordiv__(self, other):
        return self.score//other

    def __gt__(self, other):
        return self.score_alex<other.score_alex

    def __lt__(self, other):
        return not self>other and not self==other

    def __eq__(self, other):
        return self.id == other.id

    def _insertOrd(self, vector, dato, long):
        i = 0
        encontrado = False
        while i < long and not encontrado:
            if books_score[dato] > books_score[i]:
                vector.insert(i, dato)
                encontrado = True
            else:
                i+=1

        if not encontrado:
            vector.append(dato)
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
        return res


with open(input) as f_in:
    #read first line
    books_norep, libs, days = [int(x) for x in next(f_in).split()]
    books_score = [int(x) for x in next(f_in).split()]
    all_libs = []
    id = 0
    for line in f_in: # read rest of lines
        if len(line.replace('\n','')) == 0:
            continue
        different_books, signup_days, speed = [int(x) for x in line.split()]#next(f_in).split()]
        books = [int(x) for x in next(f_in).split()]#next(f_in).split()]
        lib_it = Library(id,different_books,signup_days,speed,books)
        all_libs.append(lib_it)
        factor += lib_it.score_alex
        id += 1
        #matrix.append([x for x in line]) #TTTTT
    factor /= (libs*3/2)

repeat_book = [False]*books_norep

def delete_book(list_book):
    global repeat_book
    non_repeated_books = []
    for libro in list_book:
        if not repeat_book[libro]:
            non_repeated_books.append(libro)
            #print("Meto libro", libro)
            #repeat_book[libro] = True

    return non_repeated_books

def resulttofile(res):
    with open(output_file, 'w') as f_out:
        f_out.write(str(len(res))+"\n")
        for item in res:
            f_out.write("%d %d\n" % (item[0].id, len(item[1])))
            for element in item[1]:
                f_out.write("%d " % element)
            f_out.write("\n")

def getBestLib(all_libs):
    if(len(all_libs) == 0):
        return None, all_libs, 0
    
    best = all_libs[0]
    new_libs = []
    new_libs_len = 0
    for i in all_libs:
        if (i.signup_days >= days ):
            continue
        
        if(i.score_alex > best.score_alex):
            new_libs.append(best)
            best = i
        else:
            new_libs.append(i)
        new_libs_len += 1
    return best, new_libs, new_libs_len

def funGetBestLib(all_libs):
    if(len(all_libs) == 0):
        return None, all_libs, 0
    best = all_libs[0]
    best.books = delete_book(best.books)
    new_libs = []
    new_libs_len = 0
    del all_libs[0]
    for i in all_libs:
        if (i.signup_days >= days ):
            continue
        i.books = delete_book(i.books)
        if(i.books == []):
            continue
        i.updateScore()
        if(i.score_alex > best.score_alex):
            new_libs.append(best)
            best = i
        else:
            new_libs.append(i)
        new_libs_len += 1
    if (best.books == [] or best.signup_days >= days):
        best = None
    return best, new_libs, new_libs_len


def main():
    global days
    global all_libs
    global repeat_book
    librerias = []
    librerias_len = 0
    sigue = True
    while sigue:
        best_lib, all_libs, all_libs_len = funGetBestLib(all_libs)
        if(best_lib is None):
            sigue = False
            continue
        #print(all_libs_len)
        librerias.append([best_lib, []])
        librerias_len += 1
        days -= best_lib.signup_days

        res = best_lib.buscarXbest()

        if len(res) == 0:
            continue

        j = 0
        while j < days*best_lib.speed and j < len(res):
            librerias[librerias_len-1][1].append(res[j])
            repeat_book[res[j]] = True
            j += 1

    resulttofile(librerias)

if __name__ == '__main__':
    main()
