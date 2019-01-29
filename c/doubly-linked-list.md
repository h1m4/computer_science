# 양방향 연결 리스트를
* 양방향 연결 리스트는 머리와 꼬리를 모두 가진다.
* 각 노드는 앞 노드와 뒷 노드의 정보를 모두 저장한다.



```c
#include<stido.h>
#include <stdlib.h>

typedef struct{
  int data;
  struct Node *prev;
  struct Node *next;
} Node;
Node *head, *tail;

void insert(int data){
  Node* node = (Node*) malloc(sizeof(Node));
  node -> data = data;
  Node* cur;
  cur = head -> next;
  while (cur -> data < data && cur != tail){
    cur = cur -> next;
  }

  void removeFront(){
    Node* node = head -> next;
    head -> next = node -> next;
    Node* next = node -> next;
    next -> prev = head;
    free(node);
  }
  void show(){
    Node* cur = head -> next;
    while (cur != tail){
      printf("%d", cur-> data);
      cur = cur -> next;
    }
  }
  Node* prev = cur -> prev;
  prev -> next = node;
  node -> prev = prev;
  cur -> prev = node;
  node -> next = cur;
}
```
