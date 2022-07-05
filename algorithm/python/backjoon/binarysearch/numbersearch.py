import sys
In = sys.stdin.readline

def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        # 찾은 경우 중간점 인덱스 반환
        if array[mid] == target:
            return 1
        # 중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
        elif array[mid] > target:
            end = mid - 1
        # 중간점의 값보다 찾고자 하는 값이 큰 경우 오른쪽 확인
        else:
            start = mid + 1
    return 0

N = int(In())
num_list = sorted(list(map(int, In().strip().split(" "))))

M = int(In())
target_list = list(map(int, In().strip().split(" ")))

for i in target_list:
    print(binary_search(num_list, i, 0, N-1))