# 다차원 배열과 포인터 배열

## 2차원 배열

* 행렬 데이터를 표현할 때, 그래프 알고리즘을 처리할 때, 다수의 실생활 데이터를 처리할 때 사용된다.
* 2차원 배열의 초기화
`자료형 배열이름 [행][열] = {{값, 값, 값, ...}, {값, 값, 값, ...}, ...}`

* 2차원 배열의 활용

```c
#include <stdio.h>

int a[3][3] = {{1, 2, 3}, {4, 5, 6}, {7, 8, 9}};

int main(void) {
  int i, j;
  for (i = 0; i < 3; i++) {
    for (j = 0; j < 3; j++) {
      print("%d", a[i][j]);
    }
    printf("/n");
  }
  System("pause");
  return 0;
}
```

## 포인터 배열의 구조 분석

* 배열은 포인터와 동일한 방식으로 동작한다.
* 배열의 이름은 배열의 원소의 첫번째 주소가 된다.
* 포인터는 변수이고 배열의 이름은 상수이다.

<br>

* 포인터를 배열처럼 사용하기

```c
#include <stdio.h>

int main(void) {
  int a[5] = {1, 2, 3, 4, 5};
  int *b = a;
  printf("%d\n", b[2]);
  System(pause);
  return 0;
}
```

* 여기서 배열의 이름은 배열의 첫번째 원소의 주소이다.
* 포인터는 연산을 통해 자료형의 크기만큼 이동한다.
* 따라서 정수형 포인터는 4바이트씩 이동한다.

```c
#include <stdio.h>

int main(void) {
  int a[5] = {1, 2, 3, 4, 5};
  int i;
  for (i = 0; i < 5; i++){
  printf("%d\n", *(a + 1)); //4byte만큼 증가. 이는 a[i]만큼 증가하는 것과 같다.
}
  System(pause);
  return 0;
}
```
* 크기가 double형인 배열을 선언했을 때 배열의 시작 주소가 X라고 할 때 배열의 마지막 원소의 주소는?

```c
#include <stdio.h>

int main(void) {
double b[10];
  printf("%d %d\n", b, b + 9); //답은 72
  System(pause);
  return 0;
}
```

* 프로그램의 결과 확인하기

```c
#include <stdio.h>

int main(void) {
  int a[5] = {1, 2, 3, 4, 5};
  int *p = a;
  printf("%d\n", *(p++)); //2
  printf("%d\n", *(++p)); //3
  printf("%d\n", *(p+2)); //5
  System(pause);
  return 0;
}
```

* 2차원 배열도 포인터로 처리 가능

```c
#include <stdio.h>

int main(void) {
  int a[2][5] = {{1, 2, 3, 4, 5}, {6, 7, 8, 9, 10}}
  int (*p)[5] = a[1];
  int i;
  for (i = 0; i < 5; i++){
  printf("%d", p[0][i]);
}
  System(pause);
  return 0;
}
```
