'''

"OOXXOXXOOO"와 같은 OX퀴즈의 결과가 있다. O는 문제를 맞은 것이고, X는 문제를 틀린 것이다.
문제를 맞은 경우 그 문제의 점수는 그 문제까지 연속된 O의 개수가 된다. 예를 들어, 10번 문제의 점수는 3이 된다.
"OOXXOXXOOO"의 점수는 1+2+0+0+1+0+0+1+2+3 = 10점이다.
OX퀴즈의 결과가 주어졌을 때, 점수를 구하는 프로그램을 작성하시오.


아 의외로 까다로웠다...

        for k in range(1, len(score[i])+1):
            count += k
이 부분을

        for k in range(len(score[i])):
            count += k + 1
로 처리하면 왜 9가 나오지?를 계속 고민함.. 사실 아직도 모르겠음....


 replace().split()은 사용할 수 없음, replace()가 list를 안받음
 split('X')로 하면 됬는데...

숏코딩:
뭔 말인지 모르겠음...
exec"print sum(i*-~i/2for i in map(len,raw_input().split('X')));"*input()
출처: http://sssunho.tistory.com/30 [SSSUNHO]
'''
n = int(input())
for j in range(n):
    a = input()
    score = a.replace('X', ' ')
    score = score.split()
    count = 0
    for i in range(len(score)):
        for j in range(1, len(score[i])+1):
            count += j
    print(count)
