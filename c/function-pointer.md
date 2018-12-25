# 함수 포인터

* C언어에서는 함수의 이름을 이용해 특정한 함수를 호출한다.
* 함수의 이름은 메모리 주소를 반환한다.

```c

#include<stdio.h>

void function(){
  printf("this is function");
}

int main(void) {
  printf("%d\n", function); //함수의 메모리 값이 출력된다.
  system("pause");
  return 0;
}
```

* 함수 포인터는 특정한 함수의 반환 자료형을 지정하는 방식으로 선언된다.
* 함수 포인터를 이용하면 형태가 같은 서로 다른 기능의 함수를 선언할 수 있다.
`반환자료형(*함수명)(매게변수) = 함수명;`


* 매게변수 및 반환 자료형이 없는 함수 포인터

```c

#include<stdio.h>

void myFunction(){
  printf("this is function");
}
void youtFunction(){
  printf("this is your function");
}


int main(void) {
  void(*fp)() = myFunction;
  fp();
  void(*fp)() = youtFunction;
  fp();
  system("pause");
  return 0;
}
```

* 매게변수와 반환 자료형이 있는 함수 포인터

```c

#include<stdio.h>

void add(int a, int b){
 return a+b;
}
void sub(int a, int b){
  return a-b;
}


int main(void) {
  void(*fp)(int, int) = add;
  printf("%d\n", fp(10, 3));
  fb = sub;
  printf("%d\n", fp(10, 3));
  system("pause");
  return 0;
}
```

* C언어 프로그램의 모든 함수는 내부적으로 포인터 형태로 관리할 수 있다.
* 자주 사용되지 않지만 
