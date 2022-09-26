#2nd problem
import sys
sizeP = int(input())
dP = [list(z) for z in input().split()]

numl = 0
out = []
for x in range(sizeP-1):
    if(dP[x] > dP[x+1]):
        out.append(dP[x])

print(len(out))
for x in out:
    print(out[x] + "\n")

