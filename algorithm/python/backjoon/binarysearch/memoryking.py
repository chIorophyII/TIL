import sys
In = sys.stdin.readline
T = int(In())

for i in range(T):
    N = int(In())
    num_list = set(map(int, In().strip().split()))
    M = int(In())
    target = list(map(int, In().strip().split()))

    for i in target:
        if i in num_list:
            print(1)
        else:
            print(0)