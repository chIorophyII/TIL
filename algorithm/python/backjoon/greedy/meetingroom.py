n = int(input())
end_list = []
time_table = dict()
maxi = 0;

for i in range(n):
    time = input()
    start = int(time.split(" ")[0])
    end = int(time.split(" ")[1])
    if start in time_table:
        time_table[start].append(end)
    else:
        time_table[start] = [end]

time_table = sorted(time_table.items())

for start in range(len(time_table)):
    for end in range(len(time_table[start])):
        
print(time_table)