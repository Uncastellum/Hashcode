import os
import time

'''
class Dictionary:
    def __init__(self, ):
        self.own_dic = create_dic(raw_matrix)


    def create_dic(mtx):

'''

'''
[
['char',[list]],
['char',[list]],
['char',[list]],
['char',[list]],
['char',[list]],
['char',[list]],
['char',[list]],
['char',[list]]
]
'''

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

def depurate(mtx):
    dic = []
    for elem in mtx:
        for tag in elem[1]:
            encontrado = False
            for word in dic:
                if tag == word[1]:
                    encontrado = True
                    word[0]+=1
                    break
            if encontrado:
                continue
            else:
                dic.append([1,tag])

    print("Dictionary Created. \n")

    for word in dic:
        if word[0] == 1:
            for elem in mtx:
                if word[1] in elem[1]:
                    elem[1].remove(word[1])
                    break

    print(dic)
    print(mtx)




def main():
    mtx = [['char',['1','4','5']], ['char',['3','5','4']], ['char',['1','2']]]
    depurate(mtx)
    PB = ProgressBar(300)
    i = 0
    while(PB.update(i) != 100.0):
        i+=1
        time.sleep(0.01)


if __name__ == '__main__':
    main()
