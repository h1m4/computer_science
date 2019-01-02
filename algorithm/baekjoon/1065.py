n = int(input())
count = 0
if n < 99:
    print(n)
elif n <= 110:
    print(99)
elif n <= 1000:
    count = 99
    for i in range(110, n + 1):
        if int(str(i)[2]) - int(str(i)[1]) == int(str(i)[1]) - int(str(i)[0]):
            count += 1
    print(count)

# 입력받은 수와 같거나 작은 한수를 출력하는 줄 알고 삽질함...ㅎㅎ... 한수의 갯수를 출력하는 것이었다...
