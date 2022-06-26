import sys
from math import ceil

In = sys.stdin.readline
room = In().strip() # 9999
cnt = [0]*9

for i in room:
    num = int(i)
    if num == 6 or num == 9:
        cnt[6] += 0.5
    else:
        cnt[num] += 1

cnt[6] = ceil(cnt[6])
print(int(max(cnt)))