import sys
In = sys.stdin.readline
N = int(In())
stack = []

for i in range(N):
    stack.append(int(In()))

seen = 1
last = stack.pop()
for i in range(N-1):
    before = stack.pop()
    if before > last:
        seen += 1
        last = before

print(seen)