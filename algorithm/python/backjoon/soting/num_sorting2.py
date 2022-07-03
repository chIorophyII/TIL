import sys

In = sys.stdin.readline
N = int(In())
num_list = []

for i in range(N):
    num_list.append(int(In()))


# # [divide]
# # 리스트 요소가 1개가 될때까지 나눔 / 왼쪽,오른쪽 merge
# def merge_sort(list):
#     if len(list) < 2:
#         return list
#
#     mid = len(list) // 2
#     left = list[:mid]
#     right = list[mid:]
#     left = merge_sort(left)
#     right = merge_sort(right)
#     return merge(left, right)
#
# # [merge]
# #1. 분리한 왼쪽리스트, 오른쪽 리스트의 각각 첫번째 요소를 비교해 더 작은 값을 결과 리스트에 저장
# #2. 저장한 값은 리스트에서 지움.
# #3. 두 리스트 모두 요소가 하나도 안남을 때까지 반복
# def merge(left, right):
#     merged_list = []
#     l=h=0
#
#     while l < len(left) and h < len(right):
#         if (left[l] < right[h]):
#             merged_list.append(left[l])
#             l += 1
#         else:
#             merged_list.append(right[h])
#             h += 1
#
#     merged_list += left[l:]
#     merged_list += right[h:]
#     return merged_list
#
# sorted_list = merge_sort(num_list)
#
# for i in sorted_list: print(i)

# https://velog.io/@jguuun/%EC%A0%95%EB%A0%AC-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98
# def quick_sort(array):
#     if len(array) <= 1:
#         return array
#     pivot = len(array) // 2
#     front_arr, pivot_arr, back_arr = [], [], []
#     for value in array:
#         if value < array[pivot]:
#             front_arr.append(value)
#         elif value > array[pivot]:
#             back_arr.append(value)
#         else:
#             pivot_arr.append(value)
#     return quick_sort(front_arr) + quick_sort(pivot_arr) + quick_sort(back_arr)
#
#
# array = quick_sort(num_list)
#
# for i in array: print(i)

# https://www.youtube.com/watch?v=KGyK-pNvWos&ab_channel=%EB%8F%99%EB%B9%88%EB%82%98
# def quick_sort(array, start, end):
#     # 원소가 1개인 경우 종료
#     if start >= end:
#         return
#     # 첫 번째 원소를 피벗으로
#     pivot = start
#     left = start+1
#     right = end
#
#     while (left <= right):
#         # 피벗보다 큰 데이터를 찾을 때까지 왼쪽에서 반복
#         while (left <= end and array[left] <= array[pivot]):
#             left += 1
#         # 피벗보다 작은 데이터를 찾을 때까지 오른쪽에서 반복
#         while (right > start and array[right] >= array[right]):
#             right -= 1
#         # 엇갈렸다면 작은 데이터와 피벗을 교체
#         if (left > right):
#             array[right], array[pivot] = array[pivot], array[right]
#         # 엇갈리지 않았다면 작은 데이터와 큰 데이터를 교체
#         else:
#             array[left], array[right] = array[right], array[left]
#
#     # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행
#     quick_sort(array, start, right - 1)
#     quick_sort(array, right + 1, end)
#
# quick_sort(num_list, 0, len(num_list) - 1)
#
# for i in num_list: print(i)

# def quick_sort(array):
#     # 리스트가 하나 이하의 원소만을 담고 있다면 종료
#     if len(array) <= 1:
#         return array
#     # 피벗은 첫 번째 원소
#     pivot = array[0]
#     # 피벗을 제외한 리스트
#     tail = array[1:]
#
#     # 분할된 왼쪽 부분
#     left_side = [x for x in tail if x <= pivot]
#     # 분할된 오른쪽 부분
#     right_side = [x for x in tail if x > pivot]
#
#     # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행하고, 전체 리스트 반환
#     return quick_sort(left_side) + [pivot] + quick_sort(right_side)
#
# for i in quick_sort(num_list): print(i)

import sys
In = sys.stdin.readline
N = int(In())
num_list = []

for i in range(N):
    num_list.append(int(In()))

num_list = sorted(num_list)
for i in num_list: print(i)
