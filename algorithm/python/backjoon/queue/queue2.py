from collections import deque
import sys
In = sys.stdin.readline
N = int(In())
queue = deque()

for i in range(N):
    order = In().strip()
    if order == "pop":
        if queue:
            print(queue.popleft())
        else:
            print(-1)
    elif order == "size":
        print(len(queue))
    elif order == "empty":
        if queue:
            print(0)
        else:
            print(1)
    elif order == "front":
        if queue:
            print(queue[0])
        else:
            print(-1)
    elif order == "back":
        if queue:
            print(queue[-1])
        else:
            print(-1)
    else:
        push, num = order.strip().split(" ")
        num = int(num)
        queue.append(num)