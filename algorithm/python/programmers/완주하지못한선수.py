import collections


def solution(participant, completion):

    for c in completion:
        if c in participant:
            participant.remove(c)

    return participant[0]

def solution_Hash(participant, completion):
    answer = ""
    dic = dict(collections.Counter(participant))
    for p in dic:
        if p in completion:
            dic[p] -= 1

    for p in dic:
        if dic[p] != 0:
            answer = p

    return answer

print(solution_Hash(["mislav", "stanko", "mislav", "ana"], ["stanko", "mislav", "mislav"]))
