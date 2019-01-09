'''
a= list(map(int, input().split()))
주어진 수 N개 중에서 소수가 몇 개인지 찾아서 출력하는 프로그램을 작성하시오.
첫 줄에 수의 개수 N이 주어진다. N은 100이하이다. 다음으로 N개의 수가 주어지는데 수는 1,000 이하의 자연수이다.
풀이 후기 : 소수가 나눠지는 수가 1과 자기자신이라는 뜻을 나머지가 1인 수 구하려고 함...하... 아프지말자...
'''


n = int(input())
nums = list(map(int, input().split(' ')))
result = 0


for i in nums:
    count = 0
    for j in range(1, nums[1]+1):
        if i % j == 0:
