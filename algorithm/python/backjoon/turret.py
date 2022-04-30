import math

num = int(input())

for i in range(num):
    x1, y1, r1, x2, y2, r2 = map(int, input().split(" "))
    length = math.sqrt((x2-x1)**2 + (y2-y1)**2)

    if (length == 0) and (r1 == r2):
        print(-1)
    elif length > (r1 + r2) or length < abs(r2 - r1):
        print(0)
    elif length == (r1 + r2) or length == abs(r2 - r1):
        print(1)
    else:
        print(2)
