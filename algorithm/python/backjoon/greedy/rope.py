import sys
In = sys.stdin.readline

N = int(In())
weight = []
maxi = 0

for i in range(N):
    e = int(In())
    weight.append(e)

weight.sort()

for i in range(N):
    if maxi < weight[i]*(N-i):
        maxi = weight[i]*(N-i)

print(maxi)