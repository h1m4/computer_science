# 연결 리스트

* 배열을 사용하는 경우 공간이 불필요하게 낭비되는 경우가 있으므로 연결 리스트를 통해 효율적으로 사용함

```c
#include<stdio.h>
# define INF 10000

int arr[INF];
int count = 0;

void addBack(int data){
  arr[count] = data;
  count++;
}

void addFirst(int data){
   for (int i = count; i>= 1; i--){
    arr[i] = arr[i-1];

    arr[0] = data;
    count ++;
  }
}

void show(){
  for (int i = 0; i < count; i++){
    printf('%d', arr[i]);

  }
}

```

* 만약 특정한 위치의 원소를 삭제하는 함수는 어떻게 만드는 법.

```c
void removeAt(int index){
  for (int i = index; i<count-1; i++){
    arr[i] = arr[i+1];
  }
  count--
}
```

## 배열 리스트의 특징
* 데이터가 들어갈 공간을 미리 메모리에 할당해야 함
* 특정한 위치의 원소에 즉시 접근 가능
* 원하는 위치로의 삽입 삭제등이 비효율적임

## 연결리스트
* 일반적으로 구조체와 포인터를 함께 사용함
* 리스트의 중간 지점에 노드를 추가하거나 삭제할 수 있어야 함
* 필요할 때 마다 메모리 공간을 할당받음

## 단일 연결 리스트
* 포인터를 이용해 단방향적으로 다음 노드를 가리킴
* 두 개의 변수가 들어감
* [참고자료](https://dojang.io/mod/page/view.php?id=645)

```c
#include<stdio.h>
#include<stdlib.h>

typeof struct{
  int data;
  struct Node *next;
} Node *head;

void addFront(Node *root, int data){
  Node *node = (Node*) malloc(sizeof(Node))
  node->data = data;
  node ->next = root -> next;
  root -> next = node;
}

void freeAll(Node *root){
  Node *cur = head -> next; //head는 할당해재 하지 않음
  while (cur != NULL){
    Node *next = cur -> next;
    free(cur);
    cur = next;
  }
 void showAll(Node *root){
   Node *cur = head ->next;
   while (cur != NULL){
     printf("%d", cur -> data);
     cur = cur -> next;
   }
 }
}
int main(void){
  head = (Node*) melloc(sizeof(Node));
  Node *node1 = (Node*) malloc(sizeof(Node));
  node->data = 1;
  Node *node2 = (Node*) malloc(sizeof(Node));
  node2 ->data = 2;
  head -> next = node1;
  node1 -> next = node2;
  node2 -> next = NULL;
  Node *cur = nead ->next;
  while(cur != NULL){
    printf("%d", cur -> data);
    cur = cur->next;
  }
  system("pause");
  return 0;
}
```

* 노드는 포인터 변수를 사용하여 동적 할당시킴
* 필요한 만큼만 메모리를 할당 받겠다는 뜻
