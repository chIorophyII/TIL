import sys
In = sys.stdin.readline
T = int(In())

# 2 13 7
# 11 103 215 290
def binary_search(array, target, start, end):
    while start < end:
        # start = 0, end = 4
        mid = (start + end) // 2
        # mid = (0+4) // 2 = 2 , array[2] = 215
        if array[mid] == target:
            return mid
        # 중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
        elif target < array[mid]:
            end = mid - 1
        # 중간점의 값보다 찾고자 하는 값이 큰 경우 오른쪽 확인
        elif array[mid] < target:
            # target = 8, array[1] = 3
            # target = 8, array[2] = 6
            start = mid + 1
            # start = 1+1 = 2
            # start = 2+1 = 3
    return start
# 2 13 7
# 11 103 215 290


for i in range(T):
    N, M = map(int, In().strip().split())
    A = list(map(int, In().strip().split()))
    B = sorted(map(int, In().strip().split()))
    cnt = 0
    for j in A:
        print("j", j)
        result = binary_search(B, j, 0, M)
        print("result", result)
        cnt += result
    print(cnt)
