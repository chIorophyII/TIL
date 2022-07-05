import sys
In = sys.stdin.readline

N = int(In())
num_list = sorted(list(map(int, In().strip().split(" "))))

M = int(In())
target = list(map(int, In().strip().split(" ")))

answer = dict()
for card in num_list:
    if card in answer:
        answer[card] += 1
    else:
        answer[card] = 1

for i in target:
    if i in answer:
        print(answer[i], end = " ")
    else:
        print(0, end = " ")

# print(' '.join(str(answer[x]) if x in answer else '0' for x in M ))
