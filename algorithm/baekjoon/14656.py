n = int(input())
members = list(map(int, input().split()))
right_members = sorted(members) # 이 부분을 members.sort()로 할 경우 members가 바뀌고 right_members는 nonetype이 됨 sorted와 sort 구분 잘하기
count = 0

for i in range(n):
	if members[i] != right_members[i]:
		count += 1
print(count)
