import os
import time


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


def main():

    a = time.clock()

    PB = ProgressBar(80000)

    for i in range(80000):
        PB.update(i+1)

    b = time.clock()
    print((b-a))

    list = [1]
    list.pop()
    print(len(list))
    return

if __name__ == '__main__':
    main()
