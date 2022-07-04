import sys

In = sys.stdin.readline
N = int(In())
num_list = [0] * 10001

for i in range(N):
    num_list[int(In())] += 1

for i in range(10001):
    if num_list[i] != 0:
        for j in range(num_list[i]):
            print(i)