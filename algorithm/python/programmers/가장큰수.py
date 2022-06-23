def solution(numbers):
    answer = ''
    st_list = list(map(str, numbers))
    st_list.sort(key = lambda x:x*3, reverse=True)

    for n in st_list:
        answer += n
    return str(int(answer))

numbers = [2, 6, 10]
print(solution(numbers))