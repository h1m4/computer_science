columns = ["이름", "나이", "주소"]

names = ["유리", "하나", "세정", "모모"]

ages = ["20", "21" , "21", "18"]

address = ["아이즈원", "구구단", "구구단", "트와이스"]

with open("ch.9.csv", "a") as f:
    column = ','.join(columns) + '\n'
    f.write(column)

    for i in range(0, len(names)):
        row = ('%s, %s, %s\n')%(names[i], ages[i], address[i])
        f.write(row)
