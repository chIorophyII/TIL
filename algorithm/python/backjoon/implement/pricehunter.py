import sys
In = sys.stdin.readline

n = int(In())
for i in range(n):
    year_17, year_18 = map(int, In().split(" "))
    a, b = 0, 0
    if year_17 == 1: a = 500
    elif year_17 == 2 or year_17 == 3: a = 300
    elif 4 <= year_17 < 7: a = 200
    elif 7 <= year_17 < 11: a = 50
    elif 11 <= year_17 < 16: a = 30
    elif 16 <= year_17 < 22: a = 10

    if year_18 == 1: b = 512
    elif year_18 == 2 or year_18 == 3: b = 256
    elif 4 <= year_18 < 8: b = 128
    elif 8 <= year_18 < 16: b = 64
    elif 16 <= year_18 < 32: b = 32

    print(10000*(a+b))