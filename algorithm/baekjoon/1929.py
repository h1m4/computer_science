'''
M이상 N이하의 소수를 모두 출력하는 프로그램을 작성하시오.
첫째 줄에 자연수 M과 N이 빈 칸을 사이에 두고 주어진다. (1 ≤ M ≤ N ≤ 1,000,000)
에레토스테네스의 체 :
제곱근으로부터 구하면 최소의 수(소수가 되는 수)만 남고 나머지는 전부 지울 수 있어 효울적이다.
'''

import math

def isPrime(num): # 여기 잘 공부해두기
    if num == 1:
        return False

    n = int(math.sqrt(num)) # 제곱근 함수, num의 제곱근은 이미 소수가 아니므로.
    for k in range(2, n+1):
        if num % k == 0:
            return False
    return True

m, n = map(int, input().split())
for k in range(m, n+1):
    if isPrime(k):
        print(k)
