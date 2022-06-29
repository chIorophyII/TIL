import sys
In = sys.stdin.readline
N = int(In())
stack = []
add =0

for i in range(N):
    num = int(In())
    if num != 0:
        stack.append(num)
    else:
        stack.pop()

for i in stack:
    add += i
print(add)