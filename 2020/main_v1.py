import os, sys
#import numpy as np
# Python program for implementation of Radix Sort

# A function to do counting sort of arr[] according to
# the digit represented by exp.
def countingSort(arr, exp1):
	n = len(arr)
	# The output array elements that will have sorted arr
	output = [0] * (n)
	# initialize count array as 0
	count = [0] * (10)
	# Store count of occurrences in count[]
	for i in range(0, n):
		index = (arr[i].score//exp1)
		count[(index)%10] += 1

	# Change count[i] so that count[i] now contains actual
	# position of this digit in output array
	for i in range(1,10):
		count[i] += count[i-1]

	# Build the output array
	i = n-1
	while i>=0:
		index = (arr[i].score//exp1)
		output[ count[ (index)%10 ] - 1] = arr[i]
		count[ (index)%10 ] -= 1
		i -= 1

	# Copying the output array to arr[],
	# so that arr now contains sorted numbers
	i = 0
	for i in range(0,len(arr)):
		arr[i] = output[i]

# Method to do Radix Sort
def radixSort(arr):
	# Find the maximum number to know number of digits
	max1 = max(arr)
	# Do counting sort for every digit. Note that instead
	# of passing digit number, exp is passed. exp is 10^i
	# where i is current digit number
	exp = 1
	while max1.score/exp > 0:
		countingSort(arr,exp)
		exp *= 10

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
    def __init__(self, id, total_b, signup, books_day, books):
        self.id = id
        self.total_b = total_b
        self.signup = signup
        self.books_day = books_day
        self.books = books
        self.total = (days-self.signup)*self.books_day
        self.score = 0
        bookssss = 0
        for i in self.books:
            self.score += books_score[i]
            bookssss+=1
        self.score = int(self.score*self.books_day-self.signup*(self.score))
        

    def __str__(self):
        string = '{0} {1} {2}\n{3}\n'
        return string.format(
            self.total_b,
            self.signup,
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
                if len >= self.total*10:
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

repeat_book = [False]*books_norep

def delete_book(list_book):
    non_repeated_books = []
    for libro in list_book:
        if not repeat_book[libro]:
            non_repeated_books.append(libro)

    return non_repeated_books

def resulttofile(res):
    with open(output_file, 'w') as f_out:
        f_out.write(str(len(res))+"\n")
        for item in res:
            f_out.write("%d %d\n" % (item[0].id, len(item[1])))
            for element in item[1]:
                f_out.write("%d " % element)
            f_out.write("\n")
            #for subitem in item:


def main():
    global days

    radixSort(all_libs)

    ##print(len(all_libs))
    #for x in all_libs:
        ##print("%d " % x.id, end='')

    librerias = []
    librerias_len = 0
    error = 10
    for i in all_libs:

        if i.signup < days:
            ##print(i.id)

            ##print("Total", i.total_b)

            res = i.buscarXbest()


            #print("Libros reps", len(res))
            res = delete_book(res)

            if len(res) >= 50:

                librerias.append([i, []])
                librerias_len += 1
                days -= i.signup

                j = 0
                ##print(days*i.books_day, "|", len(res))
                while j < days*i.books_day and j < len(res):
                    librerias[librerias_len-1][1].append(res[j])
                    j += 1

        else:
            error -= 1
            if error == 0:
                break


    resulttofile(librerias)


if __name__ == '__main__':
    main()
