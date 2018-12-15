# 구조체

* 여러개의 변수를 묶어서 하나의 객체를 표현하고자 할 때 사용한다.
* 배열 : 동일한 특성을 가지는 변수를 일렬로 나열하는 것
* 구조체 : 객체를 표현하고자 할 때 사용. (특성 표현)

* 구조체의 정의와 선언

```c
struct Student {
  char studentId[10];
  char name[10];
  int grade;
  int major;  
}
```

* 구조체 변수의 선언과 접근

```c
student Student s; //구조체 변수 선언
strcpy(s, studentId, "abc");//구조체 변수에 접근
strcpy(s.name, "Name");
s.grade = 4;
strcpy(s.major, "전공");
```

* 하나의 구조체 변수만 사용하는 경우 정의와 동시에 선언을 할 수 있다.
* 이 경우 변수는 전역변수로 사용된다.


```c
struct Student {
  char studentId[10];
  char name[10];
  int grade;
  int major;  
}

s = {"abc", "Name", 4, "전공"};
```
* `typedef`키워드를 사용하면 임의의 자료형을 만들 수 있다.
* 익명 구조체라는 것이 생겼으므로 이름을 비워놓아도 된다.

```c
typedef struct student{...}

int main(void) {
  Student s; //짧게 표현 가능  
}
```
* 구조체가 포인터 변수(동적할당)으로 사용되는 경우 ->로 표시해주어야 한다.
```
Student *s - malloc(sizeof(Student))
...
printf("%s", s->student)
```
