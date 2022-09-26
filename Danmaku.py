n,m = input().split()
n = int(n)
m = int(m)

minmap = {}

for x in range(n):
    z = [int(d) for d in input().split()]
    for y in range(m):
        if z[y] not in minmap:
            minmap[z[y]] = (x+1,y+1)
        else:
            continue
        if(len(minmap) == 10):
            break
    if(len(minmap)==10):
        break

calc = 0
lst = list(minmap.keys())
lst.sort()
# print(lst)
# print(minmap[1])
s = 10**12
check = s
for x in range(len(lst)-1):
    s = min(s,abs(lst[x]-lst[x+1]))
    #print(s)
    if(s != check):
        r1 = minmap[lst[x]][0]
        c1 = minmap[lst[x]][1]
        r2 = minmap[lst[x+1]][0]
        c2 = minmap[lst[x+1]][1]
        check = s
        small1 = lst[x]
        small2 = lst[x+1]



calc = abs(r1-r2) + abs(c1-c2) + abs(small1-small2)
print(calc)

