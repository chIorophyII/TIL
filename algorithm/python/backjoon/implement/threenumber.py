numbers = input()
a, b, c = map(int,numbers.split(" "))

num_list = [a, b, c]
num_list = sorted(num_list)

print(num_list[1])