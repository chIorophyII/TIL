import sys

In = sys.stdin.readline
N = int(In())
stack = []

for i in range(N):
    order = In().strip()

    if order == "pop":
        if not stack:
            print(-1)
        else:
            print(stack.pop())
    elif order == "size":
        print(len(stack))
    elif order == "empty":
        if stack:
            print(0)
        else:
            print(1)
    elif order == "top":
        if not stack:
            print(-1)
        else:
            print(stack[-1])
    else:
        push, num = order.strip().split(" ")
        num = int(num)
        stack.append(num)
