import sys
In = sys.stdin.readline
N = int(In())

for i in range(N):
    bracket = In().strip() # int로 바꾸거나 .strip()을 하거나
    stack = []
    for j in range(len(bracket)):
        if bracket[j] == "(":
            stack.append(bracket[j])
            print(stack)
        elif len(stack) == 0:
            stack.append(bracket[j])
            print(stack)
            break
        else:
            stack.pop()
            print(stack)

    # if stack:
    #     print("NO")
    # else:
    #     print("YES")