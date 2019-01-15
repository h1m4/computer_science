import random
import time

input()
start = time.time()
Questions =  ["큰 목표를 이루고 싶으면 허락을 구하지 마라.",
             "일반적인 것을 잃을 위험을 감수하지 않으면 평범한 것에 만족해야 한다.",
             "늘 하던 대로 하면 늘 얻던 것을 얻는다.",
             "지옥을 겪고 있다면 계속 겪어 나가라.",
             "위대한 것으로 향하기 위해 좋은 것을 포기하는 걸 두려워하지 마라.",
             "이 세상에 재능이 있는데 성공하지 못한 사람보다 더 흔한 건 없다.",
             "성공을 갈망할 때만 성공할 수 있고, 실패해도 상관없다고 생각할 때만 실패할 수 있다.",
             "진짜 사업가는 안전망이 없는 사람이다.",
             "사람들이 인생에서 실패하는 가장 큰 이유는 친구, 가족, 이웃들의 말을 듣기 때문이다.",
             "만족스럽게 잠자리에 들려면 매일 아침 투지를 가지고 일어나야 한다.",
             "소인배는 불운에 길들여지고 눌린다. 그러나 위대한 사람들은 불운 위로 올라선다.",
             "이기기 위해서는 한 번 이상 전쟁을 치러야 할 때도 있다.",
             ]
random.shuffle(Questions)
n = 0
while True:
    print("문제{}".format(n+1))
    typing = input("{}\n".format(Questions[0]))
    start = time.time()
    if typing != Questions[0]:
        print("try again")
        print()

    elif typing == Questions[0]:
        print("통과")
        Questions.pop(0)
        n += 1
        print()

if n == 3:
    end = time.time()
    res = end - start
    print("끝났음")
    print("총 걸린 시간은 {}초 입니다.".format(res))
