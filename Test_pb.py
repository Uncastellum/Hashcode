
from ProgressBar import ProgressBar
from time import sleep, time

t0 = time()
pb = ProgressBar(80000, eta_every=10)
for i in range(0,80000):
    #print(str(i))
    #print(str(pb))
    pb.numerator = i+1
    print(pb, end='\r')
    #sleep(1)
    pass

print("\nFINAL TIME: " + str(time()-t0))
