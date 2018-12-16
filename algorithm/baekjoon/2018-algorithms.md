## 1001

```python
c=input().split()
a=int(c[0])
b=int(c[1])
print(a-b)
```

## 2739
```python
n = int(input())
for i in range(1, 10):
    result = i * n
    print('{0} * {1} = {2}'.format(n, i, result))
```
## 2741



```python
n = int(input())
for i in range(1, n+1):
    print(i)
```

## 10817


```python
n = map(int, input().split(" "))

print(sorted(n, reverse = True)[1])
```


## 11721

FOR문

```python
word = input().strip()

count = 0

for i in word:
    print(i,end='')
    count += 1

    if count == 10:
        print("")
        count = 0
```


## 10871

```python
n, x = map(int, input().split())
a = list(map(int,input().split()))

for i in range(n):
    if x > a[i]:
        print(a[i], end=' ')
```


map(f, iterable)은 함수(f)와 반복 가능한(iterable) 자료형을 입력으로 받는다. map은 입력받은 자료형의 각 요소가 함수 f에 의해 수행된 결과를 묶어서 리턴하는 함수이다. (출처 : 점프 투 파이썬)
