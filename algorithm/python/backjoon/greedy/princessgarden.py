total = int(input())
cnt = 0
days = dict()
first = 301
last = 1130

for i in range(total):
    time = input()
    start_m = time.split(" ")[0]
    end_m = time.split(" ")[2]
    start_d = time.split(" ")[1]
    end_d = time.split(" ")[3]
    if len(time.split(" ")[1]) == 1:
        start_d = "0"+time.split(" ")[1]
    elif len(time.split(" ")[3]) == 1:
        end_d = "0" + time.split(" ")[3]

    start = int(start_m + start_d)
    end = int(end_m + end_d)

    if start in days:
        days[start].append(end)
    else:
        days[start] = [end]
days = dict(sorted(days.items()))
latest = 0
for day in days:
    if day < first and days[day][-1] < last: # 228 < 311 and 425 < 1130
        if latest < days[day][-1]: # 323 < 425
            first = days[day][-1]
            latest = days[day][-1]
            cnt += 1

print(days)
print(first)
print(latest)
print(cnt)