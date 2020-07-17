#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

struct ListNode {
    int val;
    struct ListNode *next;
};

typedef struct {
    int size;
    struct ListNode *node;
} MyStack;

MyStack* myStackCreate();
void myStackPush(MyStack* obj, int x);
int myStackPop(MyStack *obj);
int myStackTop(MyStack *obj);
bool myStackEmpty(MyStack *obj);
int myStackSearch(MyStack *obj, int val);
int stackSize(MyStack *obj);
int myStackFree(MyStack *obj);
int ListNode_free(struct ListNode* node);
