s = input()

if s == s[::-1]:
    ops = 0
lent = len(s)
if len(s) == 1:
    ops = 0

p1 = 0
p2 = len(s) - 1
ops = 0
out = []
out2 = []
if len(s) == 2:
    ops = 1
    out.append(p1)
    out2.append("")


s = list(s)
# print(s)
while p1 < p2 and len(s) > 2:
    if s[p1] == s[p2]:
        p1 += 1
        p2 -= 1
    else:
        ops += 1
        c1 = s[p1]
        c2 = s[p2]
        s.insert(p1, c2)  # s[:p1] + c2 + s[p1:]
        # print(s)
        s.insert(p2 + 1, c1)  # s[:p2] + c1 + s[p2:]
        # print(s)
        out.append(p1)
        out2.append(c2)
        out.append(p2 + 1)
        out2.append(c1)
        ops += 1
        p1 = 0 + ops
        p2 = len(s) - 1 - ops

# print(lent)
out2 = "\n".join("{} {}".format(x, y) for x, y in zip(out, out2))
if lent == ops:
    print(ops - 1)
    print(out2)
else:
    print(ops)
    print(out2)
    # for x in out:
    #     print(x[0],x[1])

# print(s)
