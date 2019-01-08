
n = int(input())
sort_list = []
for i in range(n):
    sort_list.append(int(input()))

sort_list.sort()
for i in range(len(sort_list)):
    print(sort_list[i])
