import sys
In = sys.stdin.readline
N = int(In())

# 110, 120, 140, 150
num_list = sorted(list(map(int, In().strip().split())))
budget = int(In())

# array = [110, 120, 140, 150]
def binary_search(array, target, start, end):
    while start <= end:
        mid = (start+end) // 2
        # target -> < budget // 4
        # target > budget // 4 break

