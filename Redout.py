from multiprocessing.connection import Listener
import sys

n, q = input().split()
n = int(n)
q = int(q)
listn = [int(x) for x in input().split()]

output = []

listr = [x for x in range(n)]

for x in range(q):
    listq = [y for y in input().split()]

    if listq[0] == "sum":
        output.append(sum(listn))
    elif listq[0] == "flip":
        listv = [int(y) - 1 for y in listq[2:]]
        r = listr
        r = [x for x in r if x not in listv]
        
        for x in r:
            listn[x] *=-1
        
        
        
        
        
        
        # print(listv)


for x in output:
    print(x)
