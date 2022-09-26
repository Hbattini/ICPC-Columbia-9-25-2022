import sys
players,power1 = input().split()
players = int(players)
power1 = int(power1)

power2 = [int(z) for z in input().split()]

power2.sort()

for t in range(players):
    if(power1>power2[t]):
        power1+=power2[t]
    else:
        print("No")
        break

if(power1>power2[len(power2)-1]): print("YES")
