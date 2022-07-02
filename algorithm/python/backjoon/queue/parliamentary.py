from collections import deque
import sys
In = sys.stdin.readline
N = int(In())
queue = deque()
cnt = 0

for i in range(N):
    elec = int(In())
    queue.append(elec)


print(queue)
