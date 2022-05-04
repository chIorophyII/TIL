num = int(input())
stack = list()

for i in range(num):
    order = input().split(" ")

    if order[0] == "push":
        pushnum = order[1]
        stack.append(pushnum)
    elif order[0] == "pop":
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])
            stack.remove(stack[-1])
    elif order[0] == "size":
        print(len(stack))
    elif order[0] == "empty":
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    else:
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])