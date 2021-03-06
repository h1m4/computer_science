'''
문제:
위의 그림과 같이 육각형으로 이루어진 벌집이 있다. 그림에서 보는 바와 같이 중앙의 방 1부터 시작해서 이웃하는 방에 돌아가면서 1씩 증가하는 번호를 주소로 매길 수 있다. 숫자 N이 주어졌을 때, 벌집의 중앙 1에서 N번 방까지 최소 개수의 방을 지나서 갈 때 몇 개의 방을 지나가는지(시작과 끝을 포함하여)를 계산하는 프로그램을 작성하시오. 예를 들면, 13까지는 3개, 58까지는 5개를 지난다.

입력으로 주어진 방까지 최소 개수의 방을 지나서 갈 때 몇 개의 방을 지나는지 출력한다.

풀이:
1부터 몇 개의 숫자를 지나가는지 count 해야 할 필요성이 있어보임
2~7, 8~19까지 일정한 범위 내의 일정한 숫자가 동심원을 그림.
즉, 2~7까지 도달하는 숫자가 같고 8~19까지 도달하는 숫자가 같다.

1. 각 동심원을 이루는 숫자의 갯수를 구한다.
2. 각 동심원에 일정 숫자를 부여하고 거기에 해당하는 넘버를 붙인다.
3. 하지만 더 간단한 방법이 있을 것 같음
* 2에서부터 시작하는 연속수 배열이 있음
* 한 개당 6 +6n 씩 늘어나는 배열에 다시 놓음 첫번째 배열의 거리는 1이다. (이걸 계차수열이라고 부른다고 한다;;)
* 어느 배열에 해당하는지 알면 답을 구할 수 있음
'''
 n = int(input())
 total = 1
 distance = 1
 while total < n:
     total += distance * 6 # 계차수열을 구하기 위함임
     distance += 1
 print(distance)
