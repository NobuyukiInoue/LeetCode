#include "../include/stack.h"

typedef struct {
    Queue **queue;
    int index;
    int size;
} MyStack;

MyStack* myStackCreate(void);
void myStackPush(MyStack *stack, int element);
int myStackPop(MyStack *stack);
int myStackTop(MyStack *stack);
bool myStackEmpty(MyStack *stack);
int stackSearch_from_front(MyStack *stack, int val);
int stackSearch_from_tail(MyStack *stack, int val);
int myStackSize(MyStack *stack);
void myStackFree(MyStack *stack);
